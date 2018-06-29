from threading import Thread

from django.http import HttpResponse
import json
from shareplay_app.models import Party
from shareplay_app.models import Song
from ClientRequests import NotifyPartyUpdated


def passOff(json_data):

    song_id = None

    if 'song' in json_data:
        song_id = json_data['song']['id']

    party = None
    try:
        if song_id is not None:
            song = Song.objects.get(id=song_id)
            party = song.party
            party.current_song_uri = json_data['song']['uri']
            party.current_song_name = json_data['song']['song_name']
            party.current_song_artists = json_data['song']['artists']
            party.current_song_imageUrl = json_data['song']['image_url']
            party.save()
            song.delete()
        else: ## when song is None, we pass in the partyId from the client
            party_id = json_data['party_id']
            party = Party.objects.get(id=int(party_id))
            party.current_song_uri = ""
            party.current_song_name = ""
            party.current_song_artists = ""
            party.current_song_imageUrl = ""
            party.save()


    except Song.DoesNotExist:
        return HttpResponse("Object does't exist", content_type='application/json', status=418)

    response = {}
    response['party'] = party.to_dict(addSongs=True)

    # the thread implementation below is how i should be doing it
    # thread = Thread(target=send_update, args=(party))
    # thread.start()
    try:
        send_update(party)
        return HttpResponse(json.dumps(response, indent=4, sort_keys=True, default=str), content_type='application/json',
                            status=200)
    except Exception:
        return HttpResponse("Error sending party update to clients", content_type='application/json', status=418)


def send_update(party):
    try:
        NotifyPartyUpdated.run(party)
    except Exception:
        return HttpResponse("Error sending party update to clients", content_type='application/json', status=418)
