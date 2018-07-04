from django.http import HttpResponse
import json
from shareplay_app.models import User
from shareplay_app.models import Party
from shareplay_app.models import Song
from django.db import transaction
from ClientRequests import NotifyPartyUpdated


def passOff(json_data):
    user_id = json_data['user']['id']
    party_id = json_data['party']['id']
    jsonArray = json.loads(json_data['songs'])

    party = Party.objects.get(id=party_id)
    user = User.objects.get(id=user_id)
    result = addMultipleSongs(jsonArray, user, party)
    if result is not 0:  # this is when addMultipleSongs errors out
        return result

    data = {}
    data['party'] = party.to_dict(addSongs=True)

    try:
        NotifyPartyUpdated.run(party)
        return HttpResponse({}, content_type='application/json')
    except Exception:
        return HttpResponse("Error sending party update to clients", content_type='application/json', status=418)


@transaction.atomic
def addMultipleSongs(jsonArray, user, party):
    if user.current_party.id != party.id:
        return HttpResponse("Can't add songs to a party your not in", content_type='application/json', status=418)

    for song in jsonArray:
        uri = song['uri']
        song_name = song['song_name']
        artists = song['artists']
        image_url = song['image_url']
        addSong(uri, song_name, artists, image_url, party)

    return 0

def addSong(uri, song_name, artists, image_url, party):
    ## We don't check song duplicates in the sevrver because i don't have an efficient way of doing it.
    ## So this task has been given to the client and it's assumed we'll get a list of unique songs here

    # add song to party
    try:
        song = Song(spotify_uri=uri, party=party, vote_count=1,
                    song_name=song_name, artists=artists, image_url=image_url)
        song.save()
    except Party.DoesNotExist:
        return HttpResponse("Object does't exist", content_type='application/json', status=418)