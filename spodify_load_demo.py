from spodify import *
from generate_data import *

#create db and create tables

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
print('tables init done')


#get data

#id name country
artists = generateArtists()
#id name year tempo, duration, language, genre, artistid
songs = generateSongs()
#username joindate
users = generateUsers(count = 100)
#friendpair
friendpairs = generateFriends(users)


#load artists into database
count = len(artists)
for n, (id, name, country) in enumerate(artists):
    #break
    print(f"{n+1}/{count} artists loaded")
    #print(id, name, country)
    execute_query(connection, add_artist_query(artistName=name, artistID=id, artistCountry=country))


#load users into database
count = len(users)
for n, (username, joindate) in enumerate(users):
    #break
    print(f"{n+1}/{count} users loaded")
    execute_query(connection, add_user_query(userName=username, joinDate=joindate))


#load songs into database
count = len(songs)
for n, (id, name, year, tempo, duration, lang, genre, artistid) in enumerate(songs):
    #break
    print(f"{n+1}/{count} songs loaded")
    execute_query(connection, add_song_query(
                                            songID=id,
                                            songName = name,
                                            songYear=year,
                                            songTempo=tempo,
                                            songDuration=duration,
                                            songLanguage=lang,
                                            songGenre=genre,
                                            songArtist=artistid))

#load friends into database
count = len(friendpairs)
for n, (fA, fB) in enumerate(friendpairs):
    #break
    print(f"{n+1}/{count} friendpairs loaded")
    execute_query(connection, add_friend_query(friendA=fA, friendB=fB))

#load song plays into database

songplays = generateSongPlays(users, songs, count=6000)
count = len(songplays)
for n, (user, song, date) in enumerate(songplays):
    #break
    print(f"{n+1}/{count} songplays loaded")
    execute_query(connection, add_song_play_query(user, song, date))


#manually generate playlists to demo song reccomendation

playlist1 = (users[0][0],"myplaylist 1", "this is a playlist")

playlist2 = (users[1][0], "very good playlist", "songs i like")
playlist3 = (users[2][0], "playlisttt", "hhhhhdesc")
playlists = [playlist1, playlist2, playlist3]

for o, n, desc in playlists:
    execute_query(connection, add_playlist_query(o, n, desc))

#add songs to playlists
playlist1Songs = songs[0:10]
playlist2Songs = songs[0:15]
playlist3Songs = songs[0:5]
playlistSongs = [playlist1Songs, playlist2Songs, playlist3Songs]

for i, pls in enumerate(playlistSongs):
    for song in pls:
        execute_query(connection, add_playlist_includes(i+1, song[0]))
