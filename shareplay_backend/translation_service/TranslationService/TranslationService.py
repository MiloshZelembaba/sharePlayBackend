import translation_service.AppleMusicService.AppleMusicService as AMS
import translation_service.Cache.CacheManager as CACHE
import translation_service.SpotifyService.SpotifyService as SS


class TranslationService:
    class __TranslationService:
        cache = CACHE.CacheManager()
        apple_music_service = AMS.AppleMusicService()
        spotify_service = SS.SpotifyService()

        def __init__(self):
            self.apple_music_service.authorize()
            self.spotify_service.authorize()

    instance = None

    def __init__(self):
        if not TranslationService.instance:
            TranslationService.instance = TranslationService.__TranslationService()

    def convert(self, id_tuple, requested_platform, query):
        cached_result = self.instance.cache.get_id(id_tuple, requested_platform)
        if cached_result:
            return cached_result

        result = None
        if requested_platform is CACHE.APPLE_MUSIC:
            result = self.instance.apple_music_service.get_id_for_query(query)
        elif requested_platform is CACHE.SPOTIFY:
            result = self.instance.spotify_service.get_id_for_query(query)
        elif requested_platform is CACHE.GOOGLE_PLAY:  # not supported yet
            result = None
        else:
            result = None

        self.instance.cache.put_id(id_tuple, (requested_platform, result))
        return result
