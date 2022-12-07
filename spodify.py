from sqlite_setup import create_connection, execute_query, execute_read_query
import random
import string

#USERS

create_users_table = """
CREATE TABLE IF NOT EXISTS users (
    uName TEXT PRIMARY KEY,
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

def add_artist_query(artistName, artistID = None, artistCountry = None, connection=None):
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
def add_song_query(songName, songYear, songTempo, songDuration, songLanguage, songGenre, songArtist, songID = None, connection=None):
    
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
    friendA TEXT NOT NULL,
    friendB TEXT NOT NULL,
    FOREIGN KEY (friendA) REFERENCES users (uName),
    FOREIGN KEY (friendB) REFERENCES users (uName),
    PRIMARY KEY (friendA, friendB)
);
"""

def add_friend_query(friendA, friendB):
    query = f"""
    INSERT INTO
        friends (friendA, friendB)
    VALUES
        ("{friendA}", "{friendB}"),
        ("{friendB}", "{friendA}")
    """

    return query

#SONG LIKES table

create_song_likes_table = """
CREATE TABLE IF NOT EXISTS songlikes(
    songlikeID INTEGER PRIMARY KEY AUTOINCREMENT,
    userName TEXT NOT NULL,
    songID TEXT NOT NULL,
    FOREIGN KEY (userName) REFERENCES USERS (uName),
    FOREIGN KEY (songID) REFERENCES SONGS (sID)
);
"""

def add_song_like_query(user, song):
    query = f"""
    INSERT INTO
        songlikes (userName, songID)
        VALUES ("{user}", "{song}")
    """
    return query
    
#USER PLAYS song table count

create_song_plays_table = """
CREATE TABLE IF NOT EXISTS songplays(
    songPLAYID INTEGER PRIMARY KEY AUTOINCREMENT,
    userName TEXT NOT NULL,
    songID TEXT NOT NULL,
    playDATE TEXT DEFAULT (CURRENT_DATE),
    FOREIGN KEY (userName) REFERENCES USERS (uName),
    FOREIGN KEY (songID) REFERENCES SONGS (sID)
);
"""

def add_song_play_query(user, song, date=None):
    if date is None:

        query = f"""
        INSERT INTO
            songplays (userName, songID)
            VALUES ("{user}", "{song}")
        """
        return query
    else:
        query = f"""
        INSERT INTO
            songplays (userName, songID, playDATE)
            VALUES ("{user}", "{song}", "{date}")
        """
        return query

#PLAYLIST table (with owner rel)

create_playlist_table = """
CREATE TABLE IF NOT EXISTS playlists(
    plID INTEGER PRIMARY KEY AUTOINCREMENT,
    plOwner TEXT NOT NULL,
    plName TEXT NOT NULL,
    plDesc TEXT NOT NULL,
    FOREIGN KEY (plOwner) REFERENCES USERS (uName)
);

"""

def add_playlist_query(owner, name, description):
    query = f"""
        INSERT INTO
            playlists (plOwner, plName, plDesc)
            VALUES ("{owner}", "{name}", "{description}")
        """
    return query




#playlist includes song table

create_playlist_includes_table = """
CREATE TABLE IF NOT EXISTS playlistincludes(
    playlist INTEGER NOT NULL,
    song TEXT NOT NULL,
    FOREIGN KEY (playlist) REFERENCES PLAYLISTS (plID),
    FOREIGN KEY (song) REFERENCES songs (sID)
    PRIMARY KEY (playlist, song)
);

"""

def add_playlist_includes(playlist, song):
    query = f"""
        INSERT INTO
            playlistincludes (playlist, song)
            VALUES ({playlist}, "{song}")
        """
    return query

#user follows playlist table

create_user_follows_playlist_table = """
CREATE TABLE IF NOT EXISTS playlistfollows(
    plFollowID INTEGER PRIMARY KEY AUTOINCREMENT,
    user TEXT NOT NULL,
    playlist INTEGER NOT NULL,
    FOREIGN KEY (user) REFERENCES USERS (uName),
    FOREIGN KEY (playlist) REFERENCES playlists (plID)
);
"""

def add_playlist_follow(user, playlist):
    query = f"""
        INSERT INTO
            playlistfollows (user, playlist)
            VALUES ("{user}", "{playlist}")
        """
    return query


#complex queries


#find the top 10 genres played among friends of a user
def top_friend_played_genres_query(user):

    query = f"""
    select sGenre, count(sGenre)

    from friends

    join songplays on friends.friendB = songplays.userName

    join songs on songplays.songID=songs.sID

    where friendA = "{user}"

    group by sGenre

    order by count(sGenre) desc

    limit 10
    
    """

    return query


#returns top 10 users with the most friends
def most_popular_users_query():
    query = """
    select friendA, count(friendA)
    from friends
    group by friendA

    order by count(friendA) desc

    limit 10

    """

    return query

#artists with most plays in a given year
def most_listened_artist_year(year):
    query = f"""
    select artists.aName "Artist", count(artists.aName) "Listens"
    from songplays

    join songs on songs.sID=songplays.songID
    join artists on songs.sArtist=artists.aID
    where date(songplays.playDate) between "{year}-01-01" and "{year}-12-31"

    group by artists.aName
    order by count(artists.aName) desc
    limit 10
    
    """

    return query

def top_songs_year(year):
    query = f"""
    
    select songs.sName, count(songs.sName), artists.aName

    from songplays

    join songs on songplays.songID=songs.sID
    join artists on songs.sArtist=artists.aID

    where date(songplays.playDate) between "{year}-01-01" and "{year}-12-31"

    group by songs.sName

    order by count(songs.sName) desc

    limit 10
    """

    return query

# get songs played by user in order of date

def song_play_year_timeline_query(user, year):
    query = f"""
    
    SELECT sName, aName, playDATE FROM songplays
    JOIN songs on songs.sID = songplays.songID
    JOIN artists on artists.aID = songs.sArtist
    WHERE songplays.userName = "{user}"
    and playDATE BETWEEN "{year}-1-1" AND "{year}-12-31"
    ORDER BY playDATE ASC
    
    """
    return query

#get songs in playlist







