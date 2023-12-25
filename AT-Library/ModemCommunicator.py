import serial
import time

signal = serial.Serial(
  port='/dev/ttyUSB3',
  baudrate=115200,
  baudrate=115200,
  bytesize=8,
  parity='N',
  timeout=1,
  stopbits=1,
  rtscts=False,
  dsrdtr=False
)
 
signal.write(("AT\r\n").encode())
time.sleep(1)
response = signal.read(signal.in_waiting).decode()
print("Response: ", response)

signal.close()
