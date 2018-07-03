from django.http import HttpResponse
import json
from shareplay_app.models import User
import LeavePartyHandler


def passOff(json_data):
    email = json_data['email']
    product_flavour = json_data['product']

    spotify_refresh_token = None
    if 'spotify_refresh_token' in json_data:
        spotify_refresh_token=json_data['spotify_refresh_token']

    display_name = ""
    if 'display_name' in json_data:
        display_name = json_data['display_name']

    refresh_token = None
    if 'refresh_token' in json_data:
        refresh_token = json_data['refresh_token']

    try:
        user = User.objects.get(email=email)

        # LeavePartyHandler.passOff(json_data)
        user.current_party_id = None
        user.spotify_refresh_token = spotify_refresh_token
        user.display_name = display_name
        user.product = product_flavour

        if refresh_token is not None:
            user.fcm_token = refresh_token

        user.save()
        data = user.to_dict()
    except User.DoesNotExist:
        new_user = User(display_name=display_name, email=email, address="nothing yet",
                        port=0, product=product_flavour, spotify_refresh_token=spotify_refresh_token)

        if refresh_token is not None:
            new_user.fcm_token = refresh_token

        new_user.save()
        data = new_user.to_dict()

    return HttpResponse(json.dumps(data, indent=4, sort_keys=True, default=str), content_type='application/json')



