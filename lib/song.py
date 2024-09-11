class Song:
    # Class attributes
    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        # Instance attributes
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Increment song count when a new song is created
        Song.add_song_to_count()
        
        # Add artist and genre to respective class attributes
        Song.add_to_artists(self.artist)
        Song.add_to_genres(self.genre)
        
        # Add to artist and genre counts
        Song.add_to_artist_count(self.artist)
        Song.add_to_genre_count(self.genre)

    @classmethod
    def add_song_to_count(cls):
        """Increment the total song count."""
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        """Add a new genre to the genres list if it's not already present."""
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        """Add a new artist to the artists list if not already present."""
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        """Update the genre count by adding to the genre histogram."""
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        """Update the artist count by adding to the artist histogram."""
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

