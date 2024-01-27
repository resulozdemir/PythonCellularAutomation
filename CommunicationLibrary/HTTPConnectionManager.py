from ModemCommunicator import ModemCommunicator

url = "https://webhook.site/fbe25b48-2ea0-48a8-bf78-eece26eacf58"
post_data = "data=deneme"

modem = ModemCommunicator()
modem.http_configure()

response = modem.http_request(url, method='GET')
print("GET İsteği Sonucu:", response)

response = modem.http_request(url, method='POST', data=post_data)
print("POST İsteği Sonucu:", response)

modem.close()