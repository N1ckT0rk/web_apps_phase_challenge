from lib.artist import Artist

# Test that artist constructs with id, artist_name
# and genre
def test_construct():
    artist = Artist(1, 'Fake name', 'Fake genre')
    assert artist.id == 1
    assert artist.artist_name == 'Fake name'
    assert artist.genre == 'Fake genre'

# We can compare two indentical artists
# and have them be equal
def test_artists_are_equal():
    artist1 = Artist(1, 'Fake name', 'Fake genre')
    artist2 = Artist(1, 'Fake name', 'Fake genre')
    assert artist1 == artist2

# Test formating 
def test_artists_format_nicely():
    artist = Artist(1, 'Fake name', 'Fake genre')
    assert str(artist) == "Artist(1, Fake name, Fake genre)"
