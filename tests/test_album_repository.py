from lib.album_repository import AlbumRepository
from lib.album import Album


# When we call AlbumRepository#all
# We get a list of Album objects in the album table
# def test_all(db_connection): # See conftest.py to learn what `db_connection` is.
#     db_connection.seed("seeds/records.sql") # Seed our database with some test data
#     repository = AlbumRepository(db_connection) # Create a new AlbumRepository

#     albums = repository.all() # Get all albums

#     # Assert on the results
#     assert albums == [
#         Album(1, 'Lateralus', 2000, 1)
#     ]

# def test_add(db_connection):
#     # db_connection.seed("seeds/records.sql")
#     repository = AlbumRepository(db_connection)
#     album = Album(None, "title", 2022, 2)
#     repository.add(album)
#     albums = repository.all()
#     assert albums == [
#         Album(1, 'Lateralus', 2000, 1), Album(2, "title", 2022, 2)
#     ]


# When we call AlbumRepository#get_by _id
# We get the object of an album for that id
# def test_get_by_id(db_connection):
#     db_connection.seed("seeds/records.sql")
#     repository = AlbumRepository(db_connection)
#     album = repository.get_by_id(1)
#     assert album == [
#         Album(1, 'Lateralus', 2000, 1)
#     ]

def test_get_by_id(db_connection):
    db_connection.seed("seeds/records.sql")
    repository = AlbumRepository(db_connection)
    album = repository.get_by_id(1)
    assert album == Album(1, 'Lateralus', 2000, 1, 'Tool')