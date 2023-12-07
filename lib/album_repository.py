from lib.album import Album

class AlbumRepository:
    
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute('SELECT * from albums')
        albums = []
        for row in rows:
            item = Album(row["id"], row["title"], row["release_year"], row["artist_id"])
            albums.append(item)
        return albums

    def add(self, album):
        self.connection.execute('INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s)', [
            album.title, album.release_year, album.artist_id])
        return None
    
    def get_by_id(self, id):
        rows = self.connection.execute('SELECT albums.id, albums.title, albums.release_year, albums.artist_id, artists.artist_name FROM albums JOIN artists ON albums.artist_id = artists.id WHERE albums.id = %s', (id,))
        albums = []
        for row in rows:
            album = Album(row["id"], row["title"], row["release_year"], row["artist_id"], row['artist_name'])
            albums.append(album)
        
        return albums[0]
    