from django.http import HttpResponse
import json
from shareplay_app.models import Song
from shareplay_app.models import Party
from ClientRequests import NotifyPartyUpdated


# TODO: DB look ups are case sensitive, should store all lowercase or whatever
def passOff(json_data):
    song_id = json_data['song']['id']

    try:
        song = Song.objects.get(id=song_id)
        song.vote_count += 1
        song.save()
        party = Party.objects.get(id=song.party.id)
    except Song.DoesNotExist:
        return HttpResponse("Object does't exist", content_type='application/json', status=418)

    try:
        NotifyPartyUpdated.run(party)
        return HttpResponse({}, content_type='application/json')
    except Exception:
        return HttpResponse("Error sending party update to clients", content_type='application/json', status=418)
