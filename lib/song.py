class Song:
    #keeps track of added song
    count = 0
    #stores unique genres,artists,genre_count,artist_count
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        
        Song.add_song_to_count()
        Song.add_to_genres(genre) 
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1


#instances of the Song class with real artist and song names
song1 = Song("Thriller", "Michael Jackson", "Pop")
song2 = Song("Where Do Broken Hearts Go", "Whitney Houston", "R&B")
song3 = Song("Billie Jean", "Michael Jackson", "Pop")
song4 = Song("Said I Loved You...But I Lied", "Michael Bolton", "Pop")
song5 = Song("We Found Love ft. Calvin Harris", "Ria", "R&B")
song6 = Song("One & Only ft. T Donna", "B", "Pop")

# Display genre, artist, and total counts
print("Genre counts:", Song.genre_count)
print("Artist counts:", Song.artist_count)
print("Total songs created:", Song.count)
