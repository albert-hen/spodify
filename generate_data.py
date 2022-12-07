
import pandas as pd
from os.path import exists
import urllib.request
import random
import time

#download music csv
def get_music_csv():
    musicCSVURL = "https://corgis-edu.github.io/corgis/datasets/csv/music/music.csv"

    if not exists("music.csv"):
        print('hi')
        urllib.request.urlretrieve(musicCSVURL, 'music.csv')
    return

#get artists with id, name, genre
def generateArtists():

    get_music_csv()

    artistList = []
    df = pd.read_csv('music.csv')

    artists = df[['artist.id', 'artist.name']].copy().drop_duplicates(subset=['artist.id'])

    artistTuples = list(artists.itertuples(index=False, name=None))

    for a,b in artistTuples:
        artistList.append((a,b.replace("\"",""), 'United States'))
    
    return artistList

#get songs with id, name, year, tempo, duration, language, genre
def generateSongs():
    get_music_csv()

    songList = []
    df = pd.read_csv('music.csv')

    songs = df[['song.id', 'song.title', 'song.year', 'song.tempo', 'song.duration', 'artist.terms', 'artist.id']].copy().drop_duplicates()

    songsTuples = list(songs.itertuples(index=False, name=None))
    songToArtist = dict()

    for id, b, year, tempo, duration, genre, artistid in songsTuples:
        if year != 0:
            songList.append((id,id[:5]+" SONGNAME", year, int(tempo), int(duration), "English", genre, artistid))
            songToArtist[id] = artistid

    return songList


#generate fake users with username, account creation date  
def random_date_between(start, end):
    """
    from https://stackoverflow.com/questions/553303/generate-a-random-date-between-two-other-dates
    Get a time at a proportion of a range of two formatted times.
    """
    time_format = '%Y-%m-%d'
    proportion = random.random()

    #start and end should be strings specifying times formatted in the given format (strftime-style), giving an interval [start, end].
    #proportion specifies how a proportion of the interval to be taken after start
    #the returned time will be in the specified format.
    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + proportion * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))
    

def generateUsers(count = 10, wordfile = "/usr/share/dict/cracklib-small", seed = 0):
    random.seed(seed)
    
    userList = set()

    WORDS = open(wordfile).read().splitlines()
    alphaWORDS = [w for w in WORDS if w.isalpha()]

    while len(userList) != count:
        word = random.choice(alphaWORDS).lower()
        number = random.randint(100,999)

        userName= word + str(number)
        userJoinDate = random_date_between("2008-01-01", "2030-01-01")
        if userName not in userList:
            userList.add((userName, userJoinDate))
    
    return sorted(list(userList))

#generate fake friends

def generateFriends(userList, count = 500):
    friendpairs = set()

    for i in range(count):
        (a,b), (c,d) = random.sample(userList,k=2)
     
        if (a,c) not in friendpairs and (c,a) not in friendpairs:
            friendpairs.add((a,c))

    return list(friendpairs)

#generate song plays

def generateSongPlays(userlist, songlist, count=1000):
    #user song date
    songplays = []
    random.seed(0)

    for i in range(count):
        user, userjoin = random.choice(userlist)
        songid = random.choice(songlist)[0]
        date = random_date_between(userjoin, "2030-01-01")

        songplays.append((user,songid,date))

    return songplays
