import requests

def send_http_request(url):
    res = requests.get(url)
    return res

def check_status_code(code):
    if 200 <= code < 400:
        return True
    else:
        return False
