# Python-Based Modem Communication Library Project

## Technical Details

### Project Requirements
- Develop a Python library for communicating with a modem, capable of sending AT commands and processing responses.
	- Extra: Automatic detection of the modem serial port.
	- Extra: Customization of serial port settings like baud rate and parity.
- Write sample code to send HTTP GET and POST requests to webhook.site via the modem, using the previously developed library.
- Create example code to send and receive MQTT messages on a topic via a free and open MQTT broker hivemq, using the library.
- Enable Raspberry Pi to access the internet through the modem using:
    - PPP protocol
	- QMI/RMNET protocol
	- ECM protocol
- Measure the speed of connections established through these three protocols and compare them.

### Technologies and Methods Used
- Python: Used as the development language in the project.
- AT Commands: Utilized for communication with the modem.
- Serial Library: Employed for serial communication between devices.
- HTTP (Hypertext Transfer Protocol): The basic web protocol used for data exchange.
- MQTT (Message Queuing Telemetry Transport): A lightweight and simple messaging protocol.
- PPP (Point-to-Point Protocol): A protocol used for establishing a point-to-point connection over the internet.
- QMI (Qualcomm MSM Interface): Used in mobile devices and data cards for 3G and 4G LTE connections.
- ECM (Ethernet Control Model): A protocol for sending control signals over Ethernet.

### System Architecture 
- ModemCommunicator Class: The class used for communicating with the modem.
- Examples of communication over HTTP and MQTT protocols.
- Establishing internet connection on Raspberry Pi using various network protocols.

### Development Process
- **Stage 1:** Development of the basic library for communication with the modem.
- **Stage 2:** Addition of functions to the library for sending and receiving data using the HTTP protocol and the development of an example application that facilitates communication through these functions.
- **Stage 3:** Incorporation of functions into the library for publishing and subscribing to messages using the MQTT protocol and the development of an example application that communicates through these functions.
- **Stage 4:** Establishing internet connection using PPP, QMI, and ECM protocols, conducting speed tests, and comparing the protocols.

