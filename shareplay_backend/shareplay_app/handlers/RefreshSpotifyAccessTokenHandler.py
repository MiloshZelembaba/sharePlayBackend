from django.http import HttpResponse
import json
from shareplay_app.models import User
from shareplay_app.models import Party
import requests


def passOff(json_data):
    user_id = json_data['user']['id']

    result=None
    try:
        user = User.objects.get(id=user_id)
        spotify_refresh_token=user.spotify_refresh_token

        result = requests.post("https://accounts.spotify.com/api/token", data={"grant_type":"refresh_token",
                                                                               "refresh_token":spotify_refresh_token,
                                                                               "client_id":"75cc7c4b4c6d49388044414a5ba6aaa6",
                                                                               "client_secret":"01c3be40faec40cda92fe6af6810ce2c"})

    except User.DoesNotExist, Party.DoesNotExist:
        return HttpResponse("Object does't exist", content_type='application/json', status=418)

    data = result.text
    import pdb;pdb.set_trace()
    return HttpResponse(data, content_type='application/json', status=200)
