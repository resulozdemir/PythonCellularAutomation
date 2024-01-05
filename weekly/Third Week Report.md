# Weekly Report - Week 3

## Tasks and Progress Status

### Serial Port Customization
- Developed a comprehensive `ModemCommunicator` class in Python for flexible serial port communication.
- Implemented methods to dynamically customize serial port settings including baud rate, parity, stop bits, bytesize, and flow control.

![seri port1](https://github.com/resulozdemir/PythonCellularAutomation/assets/102479969/f1301972-6b56-4878-b541-7cdca9bc20b5)
![seri port 2](https://github.com/resulozdemir/PythonCellularAutomation/assets/102479969/644c0ea6-fb43-487a-9a89-5516853c769c)

### AT Command Processing
- Focused on processing specific AT commands (`AT+CSQ`, `AT+CREG`, `AT+CGSN`, `AT+COPS`) to gather critical modem information.
- Created functions within the `ModemCommunicator` class to send AT commands and parse the responses effectively.
- Extracted and displayed vital information such as signal strength (`+CSQ`), IMEI number (`+CGSN`), network registration status (`+CREG`), and network operator details (`+COPS`).

![at 1](https://github.com/resulozdemir/PythonCellularAutomation/assets/102479969/01fe97c3-f536-4803-b759-f50c65eaefba)
![at 2](https://github.com/resulozdemir/PythonCellularAutomation/assets/102479969/b0e53225-6596-4d72-bad9-19164a69028b)

### Unit Testing and Mocking
- Implemented unit testing for the `ModemCommunicator` class to ensure the reliability and correctness of the serial port customization and AT command processing functionalities.
- Utilized the `unittest` module and mocking to isolate and test individual components of the class without the need for actual serial port connections.
- Created tests to validate the setting of serial port parameters such as baud rate, parity, stop bits, bytesize, and flow control.
- Developed tests to confirm the proper parsing and handling of various AT command responses.

![test 1](https://github.com/resulozdemir/PythonCellularAutomation/assets/102479969/86cb9ae4-f863-49e3-bab5-a6507c63db84)
![test 2](https://github.com/resulozdemir/PythonCellularAutomation/assets/102479969/97ef8b47-9233-4f5f-a2d8-b2ab029e0f06)

### Challenges and Solutions
- Encountered an `(22, 'Invalid argument')` error while setting parity to `serial.PARITY_EVEN`.
- Overcame issues related to accurately testing the response parsing functionality by using mock objects and assertions.

![error](https://github.com/resulozdemir/PythonCellularAutomation/assets/102479969/8078bc3c-3677-4cef-97c2-d9865d10e9e5)

## References
- [String Strip Method in Python - Programiz](https://www.programiz.com/python-programming/methods/string/strip)
- [String Split Method in Python - Programiz](https://www.programiz.com/python-programming/methods/string/split)
- [PySerial API Documentation](https://pyserial.readthedocs.io/en/latest/pyserial_api.html)
- [Unittest: What is This Mock? - Python Notebook](https://selcukcihan.com/blog/unittest-nedir-bu-mock/)
- [unittest — Unit testing framework — Python Documentation](https://docs.python.org/3/library/unittest.html)
- [A Beginner’s Guide to Unit Tests in Python - Dataquest](https://www.dataquest.io/blog/unit-tests-python/)
- [Python Unit Test Objects Patching - GeeksforGeeks](https://www.geeksforgeeks.org/python-unit-test-objects-patching-set-1/)
