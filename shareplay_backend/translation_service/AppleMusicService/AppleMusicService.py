from applepymusic import AppleMusicClient


class AppleMusicService:
    TEAM_ID = '6BCJZ32J9J'
    CLIENT_ID = '69LAC68SX4'  # no one is allowed to this, keep secure
    CLIENT_SECRET = '-----BEGIN PRIVATE KEY-----\nMIGTAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBHkwdwIBAQQgCo1oD8JsYfAfWgsiTjmZcVhxUYT2k9mVkuSCY7ZR76egCgYIKoZIzj0DAQehRANCAAQShTVlsVFQD1/nnOLGxmEIhSbhdx1Ezn1tKCIAXEXZodzuOAuZqaTUwYDYj+1sUqYiTmTmMaMPMeLBJUrKqAxH\n-----END PRIVATE KEY-----'  # no one is allowed to this, keep secure

    class __AppleMusicService:
        apple_music_instance = None

        def __init__(self):
            self.herro = 'herro'

    instance = None

    def __init__(self):
        if not AppleMusicService.instance:
            AppleMusicService.instance = AppleMusicService.__AppleMusicService()

    def authorize(self):
        self.instance.apple_music_instance = AppleMusicClient(self.TEAM_ID, self.CLIENT_ID, self.CLIENT_SECRET)

    def get_id_for_query(self, query):
        result_json = self.instance.apple_music_instance.search(query, limit=1)

        if 'results' in result_json:
            result_json = result_json['results']
            if 'songs' in result_json:
                result_json = result_json['songs']
                if 'data' in result_json:  # data is an array
                    result_json = result_json['data'][0]
                    if 'id' in result_json:
                        return result_json['id']

        return None


