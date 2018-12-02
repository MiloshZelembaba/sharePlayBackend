import AuthCredsHandler
import RefreshAccessTokenHandler
from shareplay_app.models import User

def pass_off(request_data):
    email = request_data['email']

    if len(email) is 0:
        return AuthCredsHandler.pass_off(request_data)
    else:
        user = User.objects.get(email=email)  # todo: need to add in product to the user table. theres a task associated with it
        if 'firebase_refresh_token' in request_data:
            user.fcm_token = request_data['firebase_refresh_token']
            user.save()
        spotify_refresh_token = user.spotify_refresh_token
        data = {}
        data['refresh_token'] = spotify_refresh_token
        data['user'] = user.to_dict()
        return RefreshAccessTokenHandler.pass_off(data)
