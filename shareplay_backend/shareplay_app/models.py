from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    display_name = models.CharField(max_length=50, null=False)
    product = models.CharField(max_length=100, null=True)
    fcm_token = models.CharField(max_length=300,null=True)
    email = models.CharField(max_length=100, null=False)
    password = models.CharField(max_length=30, null=True)
    last_login = models.DateField(null=True)
    address = models.CharField(max_length=100, null=False)
    port = models.IntegerField(null=False)
    current_party = models.ForeignKey(
                'Party',
                null=True)

    def to_dict(self):
        _dict = {}
        _dict['id'] = self.id
        _dict["first_name"] = self.first_name
        _dict["last_name"] = self.last_name
        _dict["email"] = self.email
        _dict["last_login"] = self.last_login
        _dict["display_name"] = self.display_name
        _dict["product"] = self.product
        # _dict["current_party"] = self.current_party

        return _dict

class Party(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, null=False)
    current_song_uri = models.CharField(max_length=100, null=True)
    host = models.ForeignKey(
                'User',
                null=False,
                on_delete=models.CASCADE)

    def get_songs(self):
        songs = Song.objects.filter(party_id=self.id)
        songs = [song.to_dict() for song in songs]

        return songs

    def get_party_members(self):
        party_members = User.objects.filter(current_party_id=self.id)
        party_members = [member.to_dict() for member in party_members]

        return party_members

    def to_dict(self, addSongs=False):
        _dict = {}
        _dict['id'] = self.id
        _dict['party_name'] = self.name
        _dict['host'] = self.host.to_dict()
        _dict['current_song_uri'] = self.current_song_uri
        _dict['party_members'] = self.get_party_members()

        if addSongs:
            _dict['songs'] = self.get_songs()

        return _dict

class Song(models.Model):
    id = models.AutoField(primary_key=True)
    spotify_uri = models.CharField(max_length=100, null=False)
    song_name = models.CharField(max_length=100, null=False)
    artists = models.CharField(max_length=100, null=False)
    image_url = models.CharField(max_length=1000, null=False)
    party = models.ForeignKey(
                'Party',
                null=False,
                on_delete=models.CASCADE)
    vote_count = models.IntegerField()

    def to_dict(self):
        _dict = {}
        _dict['id'] = self.id
        _dict['uri'] = self.spotify_uri
        _dict['song_name'] = self.song_name
        _dict['artists'] = self.artists
        _dict['image_url'] = self.image_url
        _dict['vote_count'] = self.vote_count

        return _dict