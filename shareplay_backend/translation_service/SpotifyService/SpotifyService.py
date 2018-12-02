import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from requests_toolbelt.adapters import appengine
appengine.monkeypatch() ## needed for appengine and requests to behave


class SpotifyService:
    CLIENT_ID = '75cc7c4b4c6d49388044414a5ba6aaa6'  # no one is allowed to this, keep secure
    CLIENT_SECRET = '01c3be40faec40cda92fe6af6810ce2c'  # no one is allowed to this, keep secure

    class __SpotifyService:
        spotipy_instance = None

        def __init__(self):
            self.herro = 'herro'

    instance = None

    def __init__(self):
        if not SpotifyService.instance:
            SpotifyService.instance = SpotifyService.__SpotifyService()

    def authorize(self):
        client_credentials_manager = SpotifyClientCredentials(client_id=self.CLIENT_ID, client_secret=self.CLIENT_SECRET)
        self.instance.spotipy_instance = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    def get_id_for_query(self, query):
        result_json = self.instance.spotipy_instance.search(q=query, limit=1)

        if 'tracks' in result_json:
            result_json = result_json['tracks']
            if 'items' in result_json:
                return result_json['items'][0]['uri']

        return None
