from ModemCommunicator import ModemCommunicator

url = "https://webhook.site/0f1c1f14-1773-48d2-b5eb-93751e2c218b"
post_data = "data=test"

modem = ModemCommunicator()
modem.http_configure()

response = modem.http_request(url, method='GET')
print("GET Request Result: ", response)

response = modem.http_request(url, method='POST', data=post_data)
print("POST Request Result: ", response)

modem.close()