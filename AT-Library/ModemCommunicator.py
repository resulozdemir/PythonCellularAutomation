import serial
import serial.tools.list_ports
import time

class ModemCommunicator:
    def __init__(self, port=None, baudrate=115200, timeout=1, parity=serial.PARITY_NONE):
        self.port = port or self.find_modem_port()
        if not self.port:
            raise Exception("Modem port not found.")
        self.ser = serial.Serial(self.port, baudrate=baudrate, timeout=timeout, parity=parity)
   
    @staticmethod
    def find_modem_port():
        ports = list(serial.tools.list_ports.comports())
        for port in ports:
            if "VID:PID=2C7C:0125" in port.hwid.upper():
                return port.device
        return None

    def send_at_command(self, command, flag): 
        self.ser.write((command + '\r\n').encode())
    
        if flag in [0, 2]:
            time.sleep(1)
        elif flag == 1:
            time.sleep(4)

        response = self.ser.read(self.ser.in_waiting).decode()
        if flag == 2:
            time.sleep(1)
        return response
        
    def close(self):
        self.ser.close()

    def http_request(self, url, method='GET', data=None):
        self.send_at_command('AT+QHTTPCFG="contextid",1', 0)
        self.send_at_command(f'AT+QHTTPURL={len(url)},80', 0)
        self.send_at_command(url, 0)

        if method == 'GET':
            response = self.send_at_command('AT+QHTTPGET=80', 2)
        else:
            self.send_at_command(f'AT+QHTTPPOST={len(data)},80,80', 0)
            response = self.send_at_command(data, 0)

        response += self.send_at_command('AT+QHTTPREAD=80', 1)
        return self.filter_response(response)
        
    def filter_response(self, response):
        lines = response.replace('\r', '').split('\n')
        filtered_response = {'response': [], 'status': 0}
        search_terms = ('+QHTTPGET', '+QHTTPPOST', '+QHTTPREAD', 'Request successful', 'OK', 'CONNECT')

        for line in lines:
            line = line.strip()
            if line.startswith(search_terms):
                filtered_response['response'].append(line)

        return filtered_response
