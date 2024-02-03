from ModemCommunicator import ModemCommunicator

broker = "broker.hivemq.com"
port = 1883
client_id = "clientExample"
topic = "topic/example"
message = "Hello MQTT!"

modem = ModemCommunicator()

modem.setup_mqtt(broker, port, client_id)

modem.mqtt_action('subscribe', topic)

modem.mqtt_action('publish', topic, message)

response = modem.mqtt_action('receive', topic)
print("Received MQTT message: ",response)

modem.disconnect_mqtt(topic)
modem.close() 