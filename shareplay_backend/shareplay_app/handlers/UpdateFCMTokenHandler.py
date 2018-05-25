import json
from shareplay_app.models import User
from ipware import get_client_ip


def passOff(json_data):
    user_id = json_data['user']['id']
    refresh_token = json_data['refresh_token']

    user = None
    try:
        user = User.objects.get(id=user_id)
        user.fcm_token = refresh_token
        party = user.current_party
        user.current_party = None
        user.save()

        if party is not None and user.id is party.host_id:  # this means the host is leaving the party
            performPartySwitch(party, user)


    except User.DoesNotExist:
        return HttpResponse("Object does't exist", content_type='application/json', status=418)

    return HttpResponse({}, content_type='application/json', status=200)
