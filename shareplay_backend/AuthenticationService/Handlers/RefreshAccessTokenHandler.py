# import requests
from urlfetch import post
import AuthInfoStore
import json
from django.http import HttpResponse

__CLIENT_ID = AuthInfoStore.CLIENT_ID
__CLIENT_SECRET = AuthInfoStore.CLIENT_SECRET
__REDIRECT_URI = AuthInfoStore.REDIRECT_URI


def pass_off(request_data):
    refresh_token = request_data['refresh_token']

    response = post("https://accounts.spotify.com/api/token",
                    headers={'content_type': 'application/x-www-form-urlencoded'},
                    data={'grant_type': 'refresh_token',
                          'refresh_token': refresh_token,
                          'client_id': __CLIENT_ID,
                          'client_secret': __CLIENT_SECRET})

    if response.status_code != 200:
        return HttpResponse(response.text, content_type='application/json', status=response.status_code)

    return_response = json.loads(response.text)
    if 'user' in request_data:
        return_response['user'] = request_data['user']

    return_response['client_id'] = __CLIENT_ID

    return HttpResponse(json.dumps(return_response), content_type='application/json', status=response.status_code)
