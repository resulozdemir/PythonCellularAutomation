import serial
import serial.tools.list_ports
import time


class ModemCommunicator:
    def __init__(
        self, port=None, baudrate=115200, timeout=2, parity=serial.PARITY_NONE
    ):
        self.port = port or self.find_modem_port()
        if not self.port:
            raise Exception("Modem port not found.")
        self.ser = serial.Serial(
            self.port, baudrate=baudrate, timeout=timeout, parity=parity
        )

    @staticmethod
    def find_modem_port():
        ports = list(serial.tools.list_ports.comports())
        for port in ports:
            if "VID:PID=2C7C:0125" in port.hwid.upper():
                return port.device
        return None

    def send_at_command(self, command, flag=-1):
        self.ser.write((command + "\r\n").encode())
        if flag in [0, 1]:
            time.sleep(1)

        response = self.ser.read(self.ser.in_waiting).decode()
        if flag in [1, 2]:
            time.sleep(1)

        return response

    def close(self):
        self.ser.close()

    # ----------------------------------------------------------------------

    def http_configure(self):
        self.send_at_command('AT+CGDCONT=1,"IP","super"')
        self.send_at_command('AT+QICSGP=1,1,"super","","",1')
        self.send_at_command("AT+QIACT=1")
        self.send_at_command('AT+QHTTPCFG="contextid",1')
        self.send_at_command('AT+QHTTPCFG="responseheader",1', 0)

    def http_request(self, url, method="GET", data=None):
        self.send_at_command(f"AT+QHTTPURL={len(url)},80", 0)
        self.send_at_command(url, 0)

        if method == "GET":
            response = self.send_at_command("AT+QHTTPGET=80", 1)
        else:
            self.send_at_command(f"AT+QHTTPPOST={len(data)},80,80", 0)
            response = self.send_at_command(data, 0)

        time.sleep(1)
        response += self.send_at_command("AT+QHTTPREAD=80", 0)
        return self.filter_response(response)

    # ----------------------------------------------------------------------

    def setup_mqtt(self, broker, port, client_id):
        self.send_at_command('AT+QMTCFG="recv/mode",0,0,1', 0)
        self.send_at_command(f'AT+QMTOPEN=0,"{broker}",{port}', 0)
        self.send_at_command(f'AT+QMTCONN=0,"{client_id}"', 0)

    def mqtt_action(self, action, topic, message=None):
        if action == "subscribe":
            self.send_at_command(f'AT+QMTSUB=0,1,"{topic}",2', 0)

        elif action == "publish":
            msg_length = len(message)
            self.send_at_command(f'AT+QMTPUBEX=0,0,0,0,"{topic}",{msg_length}', 0)
            self.send_at_command(message, 2)

        elif action == "receive":
            response = self.send_at_command("AT+QMTRECV=0")
            return self.filter_response(response)

    def disconnect_mqtt(self, topic):
        self.send_at_command(f'AT+QMTUNS=0,2,"{topic}"', 1)
        self.send_at_command(f"AT+QMTDISC=0")

    # ----------------------------------------------------------------------

    def filter_response(self, response):
        lines = response.replace("\r", "").split("\n")
        filtered_response = []
        terms = (
            "+QHTTPGET",
            "+QHTTPPOST",
            "+QHTTPREAD",
            "Request successful",
            "OK",
            "CONNECT",
            "+QMTSUB",
            "+QMTPUBEX",
            "+QMTRECV",
            "+QMTUNS",
            "ERROR",
        )

        for line in lines:
            line = line.strip()
            for term in terms:
                if term in line:
                    filtered_response.append(line)
                    break

        return filtered_response

    # ----------------------------------------------------------------------
