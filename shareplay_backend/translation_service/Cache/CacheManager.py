import pylru

APPLE_MUSIC = 'APPLE_MUSIC'
SPOTIFY = 'SPOTIFY'
GOOGLE_PLAY = 'GOOGLE_PLAY'


class CacheManager:

    class __CacheManager:
        cache_size = 1024

        def __init__(self):
            self.cache = pylru.lrucache(self.cache_size)

    instance = None

    def __init__(self):
        if not CacheManager.instance:
            CacheManager.instance = CacheManager.__CacheManager()

    # t1 and t2 are tuples of the form (ID_TYPE, id)
    # todo(1)
    def put_id(self, t1, t2):
        if t1 in self.instance.cache:
            self.instance.cache[t1].add_id(t2)
        else:
            cacheItem = CacheItem()
            cacheItem.add_id(t2)
            self.instance.cache[t1] = cacheItem

        if t2 in self.instance.cache:
            self.instance.cache[t2].add_id(t1)
        else:
            cacheItem = CacheItem()
            cacheItem.add_id(t1)
            self.instance.cache[t2] = cacheItem

    def get_id(self, id_tuple, requested_platform):
        if id_tuple in self.instance.cache:
            return self.instance.cache[id_tuple].get_id(requested_platform)

        return None


class CacheItem:
    def __init__(self):
        self.dict = {}

    def add_id(self, id_tuple):
        self.dict[id_tuple[0]] = id_tuple[1]

    def get_id(self, requested_platform):
        if requested_platform is APPLE_MUSIC:
            return self.__get_apple_id()
        elif requested_platform is SPOTIFY:
            return self.__get_spotify_id()
        elif requested_platform is GOOGLE_PLAY:
            return self.__get_google_play_id()
        else:
            return None

    def __get_apple_id(self):
        return self.dict[APPLE_MUSIC]

    def __get_spotify_id(self):
        return self.dict[SPOTIFY]

    def __get_google_play_id(self):
        return self.dict[GOOGLE_PLAY]



# TODO(1): currently when we add elements to the cache, we store TWO values (a -> b, and b -> a) so that they can both
# be access quickly. We need to figure out a way to achieve the same effect without storing 2 elements

