# Weekly Report - Week 3

## Tasks and Progress Status

### Serial Port Customization
- Developed a comprehensive `ModemCommunicator` class in Python for flexible serial port communication.
- Implemented methods to dynamically customize serial port settings including baud rate, parity, stop bits, bytesize, and flow control.

### AT Command Processing
- Focused on processing specific AT commands (`AT+CSQ`, `AT+CREG`, `AT+CGSN`, `AT+COPS`) to gather critical modem information.
- Created functions within the `ModemCommunicator` class to send AT commands and parse the responses effectively.
- Extracted and displayed vital information such as signal strength (`+CSQ`), IMEI number (`+CGSN`), network registration status (`+CREG`), and network operator details (`+COPS`).

### Unit Testing and Mocking
- Implemented unit testing for the `ModemCommunicator` class to ensure the reliability and correctness of the serial port customization and AT command processing functionalities.
- Utilized the `unittest` module and mocking to isolate and test individual components of the class without the need for actual serial port connections.
- Created tests to validate the setting of serial port parameters such as baud rate, parity, stop bits, bytesize, and flow control.
- Developed tests to confirm the proper parsing and handling of various AT command responses.

### Challenges and Solutions
- Encountered an `(22, 'Invalid argument')` error while setting parity to `serial.PARITY_EVEN`.
- Overcame issues related to accurately testing the response parsing functionality by using mock objects and assertions.

## References
- [String Strip Method in Python - Programiz](https://www.programiz.com/python-programming/methods/string/strip)
- [String Split Method in Python - Programiz](https://www.programiz.com/python-programming/methods/string/split)
- [PySerial API Documentation](https://pyserial.readthedocs.io/en/latest/pyserial_api.html)
- [Unittest: What is This Mock? - Python Notebook](https://selcukcihan.com/blog/unittest-nedir-bu-mock/)
- [unittest — Unit testing framework — Python Documentation](https://docs.python.org/3/library/unittest.html)
- [A Beginner’s Guide to Unit Tests in Python - Dataquest](https://www.dataquest.io/blog/unit-tests-python/)
- [Python Unit Test Objects Patching - GeeksforGeeks](https://www.geeksforgeeks.org/python-unit-test-objects-patching-set-1/)
- [Understanding Python unittest - Cars.com](https://www.cars.com/vehicledetail/06503773-2179-4282-9a3a-1dce54640d4d/)