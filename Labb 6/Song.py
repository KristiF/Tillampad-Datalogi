class Song(object):
    def __init__(self, trackid, songid, artist, title):
        self.trackid = trackid
        self.songid = songid
        self.artist = artist
        self.title = title

    def __lt__(self, other):
        return self.artist < other.artist

    def __str__(self):
        return self.title

