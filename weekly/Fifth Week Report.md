# Week 5 Report

## Tasks and Progress Status

### MQTT Protocol Integration and Management
- Set up the setup_mqtt function to make the modem work with MQTT. This connects it to an MQTT broker using AT commands like AT+QMTCFG, AT+QMTOPEN, and AT+QMTCONN.
- Made the mqtt_action method for MQTT tasks. It can subscribe to topics with AT+QMTSUB, send messages using AT+QMTPUBEX, and receive messages with AT+QMTRECV.
- Used disconnect_mqtt for a safe MQTT disconnection. It unsubscribes from topics, disconnects from the broker, and closes the MQTT session using commands such as AT+QMTUNS, AT+QMTDISC, and AT+QMTCLOSE.
- Code was written using MQTT functions in the ModemCommunicator library to send messages and subscribe to hivemq.

### Better Handling of Responses
- 'filter_response' now correctly organizes MQTT and HTTP responses, helping clearer understanding.

### Resolution of Deficiencies in HTTP Request Code
- Fixed problems in the code for sending HTTP requests to match it with the proper standards.
 

### Revision of the `send_at_command` Function
- Updated 'send_at_command' to make it faster. This has made sending both HTTP and MQTT commands quicker and more responsive.

## References
- [Quectel EC2xEG9xEG2x GEM05 Series AT Commands Manual V2.0](https://sixfab.com/wp-content/uploads/2021/06/Quectel_EC2xEG9xEG2x-GEM05_Series_AT_Commands_Manual_V2.0.pdf)
- [Quectel EC2xEG9xEM05 HTTPS AT Commands Manual V1.0](https://sixfab.com/wp-content/uploads/2018/09/Quectel_EC2xEG9xEM05_HTTPS_AT_Commands_Manual_V1.0.pdf)
- [Quectel EC2xEG9xEM05 MQTT Application Note V1.1](https://sixfab.com/wp-content/uploads/2020/08/Quectel_EC2xEG9xEM05_MQTT_Application_Note_V1.1.pdf)

