import serial
import time

class ModemCommunicator:
    def __init__(self, port='/dev/ttyUSB3', baudrate=115200, timeout=1, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, flowcontrol=None):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.parity = parity
        self.stopbits = stopbits
        self.bytesize = bytesize  
        self.flowcontrol = flowcontrol
        self.ser = None
        self.setup_serial()
        
    def setup_serial(self):
        if self.port is not None:
            self.ser = serial.Serial(self.port, baudrate=self.baudrate, timeout=self.timeout, parity=self.parity, stopbits=self.stopbits, bytesize=self.bytesize)
            if self.flowcontrol == 'hardware':
                self.ser.rtscts = True
            elif self.flowcontrol == 'software':
                self.ser.xonxoff = True
        else:
            raise Exception("Wrong modem port.")
            
            
    def send_at_command(self, command):
        self.ser.write((command + '\r\n').encode())
        time.sleep(1)
        response = self.ser.read(self.ser.in_waiting).decode()
        self.parse_at_response(command, response)

    def close(self):
        self.ser.close()
        
    def parse_at_response(self, command, response):
        cleaned_response = response.strip().split('\r\nOK')[0]

        if command == 'AT+CSQ':
            value = cleaned_response.split(':')[1].strip()
            print(value)
        
        elif command == 'AT+CGSN':
            print(cleaned_response.strip())

        elif command == 'AT+CREG?':
            value = cleaned_response.split(':')[1].strip()
            print(value)

        elif command == 'AT+COPS?':
            value = cleaned_response.split(',')
            if len(value) > 2:
                operator_name = value[2].replace('"', '').strip()
                print(operator_name)

        else:
            print(response)

        
    def set_baudrate(self, baudrate):
        self.baudrate = baudrate
        self.setup_serial()
        
    def set_parity(self, parity):
        self.parity = parity
        self.setup_serial()
        
    def set_stopbits(self, stopbits):
        self.stopbits = stopbits
        self.setup_serial()

    def set_bytesize(self, bytesize):
        self.bytesize = bytesize
        self.setup_serial()

    def set_flowcontrol(self, flowcontrol):
        self.flowcontrol = flowcontrol
        self.setup_serial()



modem = ModemCommunicator()
    
modem.set_baudrate(9600) 
#modem.set_parity(serial.PARITY_ODD) #22 invalid argument error received
modem.set_stopbits(serial.STOPBITS_ONE)
modem.set_bytesize(serial.EIGHTBITS)
modem.set_flowcontrol('software')
    
modem.send_at_command('AT+COPS?')
modem.close()
