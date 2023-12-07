import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist_repository import ArtistRepository
from lib.artist import Artist

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==


# == Example Code Below ==

# GET /emoji
# Returns a smiley face in HTML
# Try it:
#   ; open http://localhost:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    # We use `render_template` to send the user the file `emoji.html`
    # But first, it gets processed to look for placeholders like {{ emoji }}
    # These placeholders are replaced with the values we pass in as arguments
    return render_template('emoji.html', emoji=':)')


@app.route('/albums', methods=['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    return render_template('albums/index.html', albums=albums)
    # return "\n".join(f"{album}" for album in repository.all())

@app.route('/albums/<id>', methods=['GET'])
def get_album_by_id(id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = repository.get_by_id(id)
    return render_template('albums/album_by_id.html', album=album)



@app.route('/albums', methods=['POST'])
def post_albums():
    if 'title' not in request.form or 'release_year' not in request.form or 'artist_id' not in request.form:
        return "You need to submit a title, release_year and artist_id", 400
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = Album(None, request.form['title'], request.form['release_year'], request.form['artist_id'])
    repository.add(album)
    return '', 200


@app.route('/artists', methods=['GET'])
def get_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artists = repository.all_artists()
    return render_template('artists/index.html', artists=artists)
    # return ", ".join(f"{artist}" for artist in repository.all_artists())


@app.route('/artists/<id>', methods=['GET'])
def get_artist_by_id(id):
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artist = repository.get_by_id(id)
    return render_template('artists/artist_by_id.html', artist=artist)


@app.route('/artists', methods=['POST'])
def post_artists():
    if 'artist_name' not in request.form or 'genre' not in request.form:
        return "You need to submit an artist_name and a genre", 400
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artist = Artist(None, request.form['artist_name'], request.form['genre'])
    repository.add_artist(artist)
    return '', 200


# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
