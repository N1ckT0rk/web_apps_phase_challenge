from lib.artist import Artist

class ArtistRepository:
    
    def __init__(self, connection):
        self.connection = connection

    def all_artists(self):
        rows = self.connection.execute('SELECT * FROM artists')
        artists = []
        for row in rows:
            item = Artist(row['id'], row['artist_name'], row['genre'])
            artists.append(item)
        return artists

    def add_artist(self, artist):
        self.connection.execute('INSERT INTO artists (artist_name, genre) VALUES (%s, %s)', [
            artist.artist_name, artist.genre])
        return None
    
    def get_by_id(self, id):
        rows = self.connection.execute('SELECT * FROM artists WHERE id = %s', [id])
        row = rows[0]
        return Artist(row['id'], row['artist_name'], row['genre'])
