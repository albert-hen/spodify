from sqlite_setup import create_connection, execute_query, execute_read_query
import random
import string

#USERS

create_users_table = """
CREATE TABLE IF NOT EXISTS users (
    uID INTEGER PRIMARY KEY AUTOINCREMENT,
    uName TEXT NOT NULL,
    uJoinDate STRING NOT NULL
);
"""

def add_user_query(userName, joinDate=None):
    query = f"""
    INSERT INTO
        users (uName, uJoinDate)
    VALUES( "{userName}", "{joinDate}");
    """

    return query

#ARTISTS

create_artists_table = """
CREATE TABLE IF NOT EXISTS artists (
    aID STRING PRIMARY KEY,
    aName TEXT NOT NULL,
    aCountry TEXT NOT NULL
);
"""

get_aid_list_query = """
    SELECT aID from artists
"""

def generate_artist_id():

    x = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(17))
    return 'A' + x

def add_artist_query(artistName, artistID = None, artistCountry = None):
    #generate id
    if artistID is None:

        #used to check if generated key does not already exist
        idCol = execute_read_query(connection, get_aid_list_query)
        print(idCol)
        existing_aid = {a[0] for a in idCol}

        while True:
            artistID = generate_artist_id()
            if artistID not in existing_aid:
                break

    if artistCountry is None:
        artistCountry = "New Zealand"

    query = f"""
    INSERT INTO
        artists (aID, aName, aCountry)
    VALUES( "{artistID}", "{artistName}", "{artistCountry}");
    """

    return query

#SONGS

create_song_table = """
CREATE TABLE IF NOT EXISTS songs (
    sID TEXT PRIMARY KEY,
    sYear INTEGER,
    sName TEXT  NOT NULL,
    sTempo INTEGER NOT NULL,
    sDuration INTEGER NOT NULL,
    sLang TEXT NOT NULL,
    sGenre TEXT NOT NULL,
    sArtist TEXT NOT NULL,
    FOREIGN KEY (sArtist) REFERENCES artists (aID)
    
);
"""

def generate_song_id():

    x = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(17))
    return 'S' + x

get_sid_list_query = """
    SELECT sID from songs
"""
def add_song_query(songName, songYear, songTempo, songDuration, songLanguage, songGenre, songArtist, songID = None):
    
    #generate id
    if songID is None:
        idCol = execute_read_query(connection, get_sid_list_query)
        print(idCol)
        existing_sid = {a[0] for a in idCol}
        while True:
            songID = generate_artist_id()
            if songID not in existing_sid:
                break

    query = f"""
    INSERT INTO
        songs (sID, sYear, sName, sTempo, sDuration, sLang, sGenre, sArtist)
    VALUES( "{songID}",{songYear} ,"{songName}", {songTempo}, {songDuration}, "{songLanguage}", "{songGenre}", "{songArtist}");
    """

    return query

#FRIENDS table

create_friends_table = """
CREATE TABLE IF NOT EXISTS friends(
    fID INTEGER PRIMARY KEY AUTOINCREMENT,
    friendA INTEGER NOT NULL,
    friendB INTEGER NOT NULL,
    FOREIGN KEY (friendA) REFERENCES users (uID),
    FOREIGN KEY (friendB) REFERENCES users (uID)
);
"""
#SONG LIKES table

create_song_likes_table = """
CREATE TABLE IF NOT EXISTS songlikes(
    songlikeID INTEGER PRIMARY KEY AUTOINCREMENT,
    userID INTEGER NOT NULL,
    songID TEXT NOT NULL,
    FOREIGN KEY (userID) REFERENCES USERS (uID),
    FOREIGN KEY (songID) REFERENCES SONGS (sID)
);
"""
#USER PLAYS song table count

create_song_plays_table = """
CREATE TABLE IF NOT EXISTS songplays(
    songPLAYID INTEGER PRIMARY KEY AUTOINCREMENT,
    userID INTEGER NOT NULL,
    songID TEXT NOT NULL,
    playDATE STRING NOT NULL,
    FOREIGN KEY (userID) REFERENCES USERS (uID),
    FOREIGN KEY (songID) REFERENCES SONGS (sID)
);
"""

#PLAYLIST table (with owner rel)

create_playlist_table = """
CREATE TABLE IF NOT EXISTS playlists(
    plID INTEGER PRIMARY KEY AUTOINCREMENT,
    plOwner INTEGER NOT NULL,
    plDesc TEXT NOT NULL,
    FOREIGN KEY (plOwner) REFERENCES USERS (uID)
);

"""
#playlist includes song table

create_playlist_includes_table = """
CREATE TABLE IF NOT EXISTS playlists(
    inclID INTEGER PRIMARY KEY AUTOINCREMENT,
    playlist INTEGER NOT NULL,
    song TEXT NOT NULL,
    FOREIGN KEY (playlist) REFERENCES PLAYLISTS (plID),
    FOREIGN KEY (song) REFERENCES songs (sID)
);

"""

#user follows playlist table

create_user_follows_playlist_table = """
CREATE TABLE IF NOT EXISTS playlistfollows(
    plFollowID INTEGER PRIMARY KEY AUTOINCREMENT,
    user INTEGER NOT NULL,
    playlist INTEGER NOT NULL,
    FOREIGN KEY (user) REFERENCES USERS (uID),
    FOREIGN KEY (playlist) REFERENCES playlists (plID)
);
"""


dbfile = "spodify.sqlite"
connection = create_connection(dbfile)



execute_query(connection, create_users_table)
execute_query(connection, create_artists_table)
execute_query(connection, create_song_table)
execute_query(connection, create_friends_table)
execute_query(connection, create_song_likes_table)
execute_query(connection, create_song_plays_table)
execute_query(connection, create_playlist_table)
execute_query(connection, create_playlist_includes_table)
execute_query(connection, create_user_follows_playlist_table)

#execute_query(connection, add_artist_query(artistID = "1234HJL", artistName ="my band",
#                                            artistCountry = "United States"))

"""
execute_query(connection, add_song_query(
    songName = "newid1234",
    songYear = 2003,
    songTempo = 123,
    songDuration = 300,
    songLanguage = "French",
    songGenre = "rock",
    songArtist = "1234HJL",
    songID = "DEEZNUTS"
))
"""



#execute_query(connection, create_artists_table)
#execute_query(connection, create_users_table)
#execute_query(connection, add_user_query('albertc123', '2034-06-01'))




