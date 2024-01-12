# Week 5 Report

## Tasks and Progress Status

### MQTT Protocol Integration and Management
- Set up the setup_mqtt function to make the modem work with MQTT. This connects it to an MQTT broker using AT commands like AT+QMTCFG, AT+QMTOPEN, and AT+QMTCONN.

   ```python
   def setup_mqtt(self, broker, port, client_id):
        self.send_at_command('AT+QMTCFG="recv/mode",0,0,1', 0) 
        self.send_at_command(f'AT+QMTOPEN=0,"{broker}",{port}', 0) 
        self.send_at_command(f'AT+QMTCONN=0,"{client_id}"', 0) 
 
- Made the mqtt_action method for MQTT tasks. It can subscribe to topics with AT+QMTSUB, send messages using AT+QMTPUBEX, and receive messages with AT+QMTRECV.

   ```python
   def mqtt_action(self, action, topic, message=None):
        if action == 'subscribe':
            self.send_at_command(f'AT+QMTSUB=0,1,"{topic}",2', 0) 
        elif action == 'publish':
            msg_length = len(message)
            self.send_at_command(f'AT+QMTPUBEX=0,0,0,0,"{topic}",{msg_length}', 0) 
            self.send_at_command(message, 2) 
        elif action == 'receive':
            response = self.send_at_command('AT+QMTRECV=0') 
            return response


- Used disconnect_mqtt for a safe MQTT disconnection. It unsubscribes from topics, disconnects from the broker, and closes the MQTT session using commands such as AT+QMTUNS, AT+QMTDISC, and AT+QMTCLOSE.

   ```python
   def disconnect_mqtt(self, topic):
        self.send_at_command(f'AT+QMTUNS=0,2,"{topic}"', 0) 
        self.send_at_command('AT+QMTDISC=0')  


- Code was written using MQTT functions in the ModemCommunicator library to send messages and subscribe to hivemq.

   ```python
   from ModemCommunicator import ModemCommunicator

   broker = "broker.hivemq.com"
   port = 1883
   client_id = "clientExample"
   topic = "“topic/example"
   message = "Hello MQTT!"
   
   modem = ModemCommunicator()
   
   modem.setup_mqtt(broker, port, client_id)
   
   modem.mqtt_action('subscribe', topic)
   
   modem.mqtt_action('publish', topic, message)
   
   response = modem.mqtt_action('receive', topic)
   print(response)
   
   modem.disconnect_mqtt(topic)
   modem.close() 

![mqtt](https://github.com/resulozdemir/PythonCellularAutomation/assets/102479969/99f5830a-403e-449d-8cb9-4a6bf02c4508)


### Better Handling of Responses
- 'filter_response' now correctly organizes MQTT and HTTP responses, helping clearer understanding.

  ```python
  def filter_response(self, response):
        lines = response.replace('\r', '').split('\n')
        filtered_response = {'response': [], 'status': 0}
        http_terms = ('+QHTTPGET', '+QHTTPPOST', '+QHTTPREAD', 'Request successful', 'OK', 'CONNECT')
        mqtt_terms = ('+QMTOPEN', '+QMTCONN', '+QMTSUB', '+QMTPUB', '+QMTRECV', '+QMTUNS', '+QMTDISC', '+QMTCLOSE')

        for line in lines:
            line = line.strip()
            for term in http_terms or mqtt_terms:
                if term in line:
                    filtered_response['response'].append(line)

        return filtered_response

### Resolution of Deficiencies in HTTP Request Code
- Fixed problems in the code for sending HTTP requests to match it with the proper standards.

   ```python
   def http_configure(self):
        self.send_at_command('AT+CGDCONT=1,"IP","super"')
        self.send_at_command('AT+QICSGP=1,1,"super","","",1')
        self.send_at_command('AT+QIACT=1')
        self.send_at_command('AT+QHTTPCFG="contextid",1')
        self.send_at_command('AT+QHTTPCFG="responseheader",1', 0)       
    

### Revision of the `send_at_command` Function
- Updated 'send_at_command' to make it faster. This has made sending both HTTP and MQTT commands quicker and more responsive.

  ```python
     def send_at_command(self, command, flag = -1): 
         self.ser.write((command + '\r\n').encode())
         if flag in [0, 1]:
             time.sleep(1) 
         response = self.ser.read(self.ser.in_waiting).decode() 
         if flag in [1, 2]:
             time.sleep(1)
 
         return response

## References
- [Quectel EC2xEG9xEM05 HTTPS AT Commands Manual V1.0](https://sixfab.com/wp-content/uploads/2018/09/Quectel_EC2xEG9xEM05_HTTPS_AT_Commands_Manual_V1.0.pdf)
- [Quectel EC2xEG9xEM05 MQTT Application Note V1.1](https://sixfab.com/wp-content/uploads/2020/08/Quectel_EC2xEG9xEM05_MQTT_Application_Note_V1.1.pdf)

