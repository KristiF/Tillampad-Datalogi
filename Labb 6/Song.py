class Song(object):
    def __init__(self, trackid, songid, artist, title):
        self.trackid = trackid
        self.songid = songid
        self.artist = artist
        self.title = title

    def __le__(self, other):
        return self.title <= other.title

    def __lt__(self, other):
        return self.title < other.title

    def __str__(self):
        return self.title

    def __eq__(self, other):
        return self.title == other.title

