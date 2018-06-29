import socket
import json
import logging
import requests
import requests_toolbelt.adapters.appengine
from urlfetch import post

def send_request(data, fcm_token, port):
    try:
        send_using_fcm(data, fcm_token)
    except Exception:
        logging.info("error occured")
        print("Error sending packet to %s at port %s", str(fcm_token), int(port))

def send_using_fcm(data, fcm_token):
    # requests_toolbelt.adapters.appengine.monkeypatch()
    url = 'https://fcm.googleapis.com/fcm/send'
    # create the body
    body = {'data': {'body': data, 'url': 'myurl', 'title': 'hello'}, 'registration_ids': [fcm_token]}
    # fix this to not hardcode the API key
    headers = {'Content-Type': 'application/json', 'Authorization': 'key=AAAA6v_4v3I:APA91bEh9-JDKVAZlA7VSSng9wYiF1TMu9ydUwZk6MtWTsAsraQ0x4uDWP1khfxqX6QfQecTte14K8fcz7iZ9ufYamPE5CthCJZO-gqDuDbrVH8q57AaLEicDc1mfcbgkfhmOYjIfLYD'}
    # requests.post(url, data=json.dumps(body), headers=headers)
    # print(fcm_token)
    result = post(url,
                  headers=headers,
                  data=json.dumps(body))
    #
    # import pdb;
    # pdb.set_trace()
    # print(result)

# not currently being used
def send_using_tcp(data, address, port):
    if (address.count(':') is 7):
        s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM, 0)
        s.connect((address, int(port), 0, 0))
        logging.info("ipv6 detected and successfully connected")
    else:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((address, int(port)))
        logging.info("ipv4 detected and successfully connected")

    data = json.dumps(data)
    s.sendall(data + "\n")
    logging.info("sent data")
    s.close()
