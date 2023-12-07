from playwright.sync_api import Page, expect

# Tests for your routes go here

# === Example Code Below ===

def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed('seeds/records.sql')
    page.goto(f"http://{test_web_address}/albums")
    list_tags = page.locator("li")
    expect(list_tags).to_have_text([
        "Lateralus",
        "Aenima",
        "Toxicity",
        "System Of A Down"
    ])

# def test_get_album_by_id(page, test_web_address, db_connection):
#     db_connection.seed('seeds/records.sql')
#     page.goto(f"http://{test_web_address}/albums/1")
#     header_tag = page.locator('h1')
#     paragraph_tag = page.locator('p')
#     expect(header_tag).to_have_text([
#         'Lateralus'
#     ])
#     expect(paragraph_tag).to_have_text([
#         'Release year: 2000',
#         'Artist: Tool'
#     ])

    # The page returned by GET /albums should contain a link for each album listed. 
    # It should link to /albums/<id>, where <id> is the corresponding album's id. 
    # That page should then show information about the specific album.
def test_get_albums_with_link(page, test_web_address, db_connection):
    db_connection.seed('seeds/records.sql')
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Lateralus'")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Lateralus")


# Add a route GET /artists/<id> which returns an HTML page showing details for a single artist.
# Add a route GET /artists which returns an HTML page with the list of artists. This page should 
# contain a link for each artist listed, linking to /artists/<id> where <id> needs to be the corresponding 
# artist id.

# Test GET /artists returns an html page with a list of all the artists
def test_get_artists(page, test_web_address, db_connection):
    db_connection.seed('seeds/records.sql')
    page.goto(f"http://{test_web_address}/artists")
    list_tags = page.locator("li")
    expect(list_tags).to_have_text([
        "Tool",
        "System Of A Down",
        "Taylor Swift",
        "Nina Simone"
    ])



# Test GET /artists has a list of artists as links that return an HTML page from the id
# with all the corresponsding information about the artist.
def test_get_artist_with_link(page, test_web_address, db_connection):
    db_connection.seed('seeds/records.sql')
    page.goto(f"http://{test_web_address}/artists")
    page.click("text='Tool'")
    h1_tag = page.locator("h1")
    p_tag = page.locator("p")
    expect(h1_tag).to_have_text("Tool")
    expect(p_tag).to_have_text("Genre: Metal")

