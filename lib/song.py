class Song:
     # Class attribute to track the number of songs
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count ={}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        #update class attributes
        self.add_song_to_count()
        self.add_to_genre(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)

     #method to add everytime a song is instantiated  
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    #method to add genre to genres array but checks first if exists
    @classmethod
    def add_to_genre(cls, genre):
        #validation check here
        if genre not in cls.genres:
            cls.genres.append(genre)

    #method to add artist to artists array but checks first if exists    
    @classmethod
    def add_to_artists(cls, artist):
        #validation check
        if artist not in cls.artists:
            cls.artists.append(artist)
    
    #method to count artist name, only unique artists
    def add_to_artist_count(cls, artist):
        if artist not in cls.artist_count:
            cls.artist_count[artist] = 1
        else:
            cls.artist_count[artist] += 1
        
    #method to count genres , only unique genres
    def add_to_genre_count(cls,genre):
        if genre not in cls.genre_count:
            cls.genre_count[genre] =1
        else:
            cls.genre_count[genre] += 1


SongMaria = Song("Maria", "MN", "Hiphop")

