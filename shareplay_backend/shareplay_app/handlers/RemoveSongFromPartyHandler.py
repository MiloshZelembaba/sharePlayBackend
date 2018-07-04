from django.http import HttpResponse
import json
from shareplay_app.models import Party
from shareplay_app.models import Song
from ClientRequests import NotifyPartyUpdated

# should be renamed, this is more for the "next" function in the client than it is simply removing a song from a party


def passOff(json_data):
    song_id = None
    if 'song' in json_data:  # happens when the currently playing song in a party finished playing. Hacky, I know.
        song_id = json_data['song']['id']

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
        else:  # when song is None, we pass in the partyId from the client
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
        result = send_update(party)

        if result is not 0:
            return result
        else:
            return HttpResponse(json.dumps(response, indent=4, sort_keys=True, default=str), content_type='application/json',
                                status=200)
    except Exception:
        return HttpResponse("Error sending party update to clients", content_type='application/json', status=418)


def send_update(party):
    try:
        NotifyPartyUpdated.run(party)
        return 0
    except Exception:
        return HttpResponse("Error sending party update to clients", content_type='application/json', status=418)
