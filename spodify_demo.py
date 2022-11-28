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


#load artists into database
count = len(artists)
for n, (id, name, country) in enumerate(artists):
    break
    print(f"{n+1}/{count} artists loaded")
    #print(id, name, country)
    execute_query(connection, add_artist_query(artistName=name, artistID=id, artistCountry=country))


#load users into database
count = len(users)
for n, (username, joindate) in enumerate(users):
    break
    print(f"{n+1}/{count} users loaded")
    execute_query(connection, add_user_query(userName=username, joinDate=joindate))


#load songs into database
count = len(songs)
for n, (id, name, year, tempo, duration, lang, genre, artistid) in enumerate(songs):
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


print('done loading data')

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

#execute_query(connection, add_user_query('albert', '2030-05-01'))
#execute_query(connection, add_friend_query(2,3))
#execute_query(connection, add_song_like_query(1, 'that song'))
#execute_query(connection, add_song_play_query(1, "that song", '2030-05-02'))