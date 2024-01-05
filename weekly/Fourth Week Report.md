# Week 4 Report

## Tasks and Progress Status

### Development of Serial Port Auto-Detection Feature
- Implemented an advanced function in Python for automatically detecting serial ports. 
- Utilized the `serial.tools.list_ports` module to scan and identify available ports.
- Integrated a method to filter ports based on specific USB device identifiers (VID and PID), ensuring the correct modem is selected for communication.
- Conducted tests to ensure the function accurately identifies the desired modem among multiple connected devices.

### Crafting HTTP GET and POST Request Functions
- Developed function to handle HTTP GET and POST requests through AT commands.
- Used AT+QHTTPCFG and AT+QHTTPURL commands for setting up HTTP sessions. These work for both GET and POST requests. 
- For GET requests, used AT+QHTTPGET and AT+QHTTPREAD commands. AT+QHTTPGET starts the GET request, and AT+QHTTPREAD lets us read what the server sends back.
- For POST requests, used AT+QHTTPPOST with AT+QHTTPREAD. AT+QHTTPPOST sends data to the server, and AT+QHTTPREAD helps us see the server's response.
- A class that uses the ModemCommunicator library and sends HTTP requests has been developed.
- Added a `filter_response` function to process and clean up the responses received from the server.
.
### Improvements in AT Command Communication
- Improved the send_at_command method by adding a flag parameter. This helps to manage different kinds of responses and the time it takes to receive them.

### Challenges and Solutions
- Faced '+CME ERROR 703' messages at HTTP GET. Fixed this by waiting longer for responses in our code.

## References
- [Sixfab HTTP AT Commands Manual](https://sixfab.com/wp-content/uploads/2018/09/Quectel_EC2xEG9xEM05_HTTPS_AT_Commands_Manual_V1.0.pdf)
- [Sixfab AT Commands Manual](https://sixfab.com/wp-content/uploads/2021/06/Quectel_EC2xEG9xEG2x-GEM05_Series_AT_Commands_Manual_V2.0.pdf)