from django.http import HttpResponse
import json
from shareplay_app.models import User
from shareplay_app.models import Party


def passOff(json_data):
    user_id = json_data['user']['id']
    party_id = trim_zeros(json_data['party_id'])

    user = None
    try:
        user = User.objects.get(id=user_id)
        print(int(party_id))
        party = Party.objects.get(id=int(party_id))
        user.current_party = party
        user.save()

    except User.DoesNotExist, Party.DoesNotExist:
        return HttpResponse("Object does't exist", content_type='application/json', status=418)

    data = {}
    data['party_id'] = party.id
    return HttpResponse(json.dumps(data, indent=4, sort_keys=True, default=str), content_type='application/json', status=200)


def trim_zeros(party_id):
    while party_id[0] == '0':
        party_id = party_id[1:]

    return party_id