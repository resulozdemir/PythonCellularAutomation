# Week 2 Report

## Tasks and Progress Status

### 1. Learning the Basics of Python Programming
- Completed introductory tutorials on Python programming.
- Practiced basic Python syntax, data types, and control structures.

### 2. Understanding and Learning AT Commands
- Researched what AT commands are and how they are used in telecommunications.
- Learned about basic AT commands and their purposes.

### 3. Attempting Communication with Modem Using Basic AT Commands
- Conducted trials for sending and receiving basic AT commands to the modem.
- Successfully sent simple commands and received responses from the modem.

  ```python
  import serial
  import time

  signal = serial.Serial(
    port='/dev/ttyUSB3',
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

  signal.close()```

### 4. Researching Python Libraries for Serial Port Communication
- Investigated Python libraries suitable for serial port communication.
- Focused on understanding the usage of `pySerial` library.

### 5. Weekly Reporting and Documentation
- Documented the progress and findings of the week.
- Prepared the weekly report in a clear and concise format.

## References
- [Python Programming Tutorials](https://www.youtube.com/playlist?list=PLWctyKyPphPiul3WbHkniANLqSheBVP3O)
- [An Introduction to Cellular AT Commands - Cavli Wireless](https://www.cavliwireless.com/blog/nerdiest-of-things/an-introduction-to-cellular-at-commands.html)
- [Sending AT Commands - Sixfab Docs](https://docs.sixfab.com/page/sending-at-commands)
- [Modem AT Command - The Geek Stuff](https://www.thegeekstuff.com/2013/05/modem-at-command/)
- [Read Response AT Command with PySerial - Stack Overflow](https://stackoverflow.com/questions/23532038/read-response-at-command-with-pyserial)
- [Raspberry Pi Forum Discussion on PySerial](https://forums.raspberrypi.com/viewtopic.php?t=113664)
- [Python Forum Discussion on PySerial](https://python-forum.io/thread-35651.html)
- [PySerial Short Introduction](https://pyserial.readthedocs.io/en/latest/shortintro.html)
- [PySerial API Documentation](https://pyserial.readthedocs.io/en/latest/pyserial_api.html)
