from django.http import HttpResponse
import json
import AuthInfoStore as AuthInfoStore
from shareplay_app.models import User
# import requests
from urlfetch import post
import spotipy
from requests_toolbelt.adapters import appengine
appengine.monkeypatch() ## needed for appengine and requests to behave

__CLIENT_ID = AuthInfoStore.CLIENT_ID
__CLIENT_SECRET = AuthInfoStore.CLIENT_SECRET
__REDIRECT_URI = AuthInfoStore.REDIRECT_URI


def pass_off(request_data):
    auth_code = request_data['auth_code']
    firebase_refresh_token = None
    if 'firebase_refresh_token' in request_data:
        firebase_refresh_token = request_data['firebase_refresh_token']

    response = post("https://accounts.spotify.com/api/token",
                    headers={'content_type': 'application/x-www-form-urlencoded'},
                    data={'grant_type': 'authorization_code',
                    'code': auth_code,
                    'redirect_uri': __REDIRECT_URI,
                    'client_id': __CLIENT_ID,
                    'client_secret': __CLIENT_SECRET})

    if response.status_code != 200:
        return HttpResponse(response.text, content_type='application/json', status=response.status_code)

    result = json.loads(response.text)
    sp = spotipy.Spotify(auth=result['access_token'])
    spotify_user_data = sp.current_user()  # figure out what this gives
    email = spotify_user_data['email']
    result['email'] = email

    user = updateUser(email, spotify_user_data, result, firebase_refresh_token )

    result['user'] = user.to_dict()
    del result['refresh_token']  # remove it from the respone back to the server
    return HttpResponse(json.dumps(result), content_type='application/json', status=response.status_code)


def updateUser(email, spotify_user_data, result, firebase_refresh_token):
    try:
        user = User.objects.get(email=email)
        user.spotify_refresh_token = result['refresh_token']
        user.fcm_token = firebase_refresh_token
        user.save()
        return user
    except User.DoesNotExist:
        user = User(email=email, display_name=spotify_user_data['display_name'], product=spotify_user_data['product'],
                        spotify_refresh_token=result['refresh_token'], address="removeThisShit", port=0)
        user.fcm_token = firebase_refresh_token
        user.save()
        return user
