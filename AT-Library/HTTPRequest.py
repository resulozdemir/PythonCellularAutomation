from ModemCommunicator import ModemCommunicator

def send_http_get(url):
    modem = ModemCommunicator()
    try:
        response = modem.http_request(url, method='GET')
        return response
    finally:
        modem.close()

def send_http_post(url, data):
    modem = ModemCommunicator()
    try:
        response = modem.http_request(url, method='POST', data=data)
        return response
    finally:
        modem.close()

if __name__ == "__main__":
    get_url = "https://webhook.site/fbe25b48-2ea0-48a8-bf78"
    post_url = "https://webhook.site/fbe25b48-2ea0-48a8-bf78"
    post_data = "data=deneme"
    
    print("GET İsteği Sonucu:", send_http_get(get_url))
    print("POST İsteği Sonucu:", send_http_post(post_url, post_data))
