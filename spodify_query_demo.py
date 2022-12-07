from spodify import *

dbfile = "spodify.sqlite"
connection = create_connection(dbfile)

#demo top_songs_of_year

year = 2020
out = execute_read_query(connection, top_songs_year(year))

print(f"\nTop 10 songs in {year}\n")

print(f"{'Song':30}| {'Artist':30}| {'Plays':10}")
for sname, playcount, artist in out:
   print(f"{sname:30}| {artist:30}| {playcount:10}")

#demo most_listened_artist_year
year = 2028
out = execute_read_query(connection, most_listened_artist_year(year))

print(f"\nTop 10 artists in {year}\n")

print(f"{'Artist':30}| {'Plays':10}")
for a,b in out:
   print(f"{a:30}| {b:10}")

"""
Top 10 artists in 2028

Artist                        | Plays     
Michael Jackson               |          3
Sofia Karlsson                |          2
J. B. Lenoir                  |          2
Eddie Turner                  |          2
Cobra Killer                  |          2
Carl Smith                    |          2
Backstreet Boys               |          2
themselves                    |          1
Wolfmother                    |          1
Winifred Phillips             |          1
"""

#demo most_popular_users_query
out = execute_read_query(connection, most_popular_users_query())
print(f"\nTop 10 Users with most friends\n")

print(f"{'Users':30}| {'Friends':10}")
for a,b in out:
   print(f"{a:30}| {b:10}")

"""
Top 10 Users with most friends

Users                         | Friends   
fortunately288                |         17
banged295                     |         16
scorning755                   |         16
approachers606                |         15
janet876                      |         15
magnified735                  |         15
obscures315                   |         15
plate366                      |         15
brightener462                 |         14
clonic922                     |         14
"""

#demo top_friend_played_genres_query
user = "fortunately288"
out = execute_read_query(connection, top_friend_played_genres_query(user))
print(f"\nTop 10 Genres played among friends of user: {user}\n")

print(f"{'Genre':30}| {'Plays':10}")
for a,b in out:
   print(f"{a:30}| {b:10}")

"""
Top 10 Genres played among friends of fortunately288

Genre                         | Plays     
blues-rock                    |         10
neo soul                      |          4
dancehall                     |          4
western swing                 |          3
grunge                        |          3
dance pop                     |          3
ccm                           |          3
alternative metal             |          3
technical death metal         |          2
tango                         |          2
"""

#demo user song plays timeline for a year

user = "dates348"
year = 2020
out = execute_read_query(connection, song_play_year_timeline_query(user, 2020))

print(f"\nAll song plays by {user} in {year}: \n")
print(f"{'Song Name':15}| {'Artist':20}| {'Date':10}")
for a,b,c in out:
   print(f"{a:15}| {b:20}| {c:10}")
