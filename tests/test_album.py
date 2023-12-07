from lib.album import Album

# Test that album constructs with id, title, release year
# and artist id
def test_init():
    album = Album(1, 'title', 1998, 1)
    assert album.id == 1
    assert album.title == 'title'
    assert album.release_year == 1998
    assert album.artist_id == 1


# We can format books to strings nicely
def test_albums_format_nicely():
    album = Album(1, 'title', 1998, 1)
    assert str(album) == "Album(1, title, 1998, 1)"


# We can compare two identical books
# And have them be equal
def test_albums_are_equal():
    album1 = Album(1, 'title', 1998, 1)
    album2 = Album(1, 'title', 1998, 1)
    assert album1 == album2
