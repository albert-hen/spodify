
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

    artists = df[['artist.id', 'artist.name']].copy().drop_duplicates()

    artistTuples = list(artists.itertuples(index=False, name=None))

    for a,b in artistTuples:
        artistList.append((a,b, 'United States'))
    
    return artistList

#get songs with id, name, year, tempo, duration, language, genre

def generateSongs():
    get_music_csv()

    songList = []
    df = pd.read_csv('music.csv')

    songs = df[['song.id', 'song.title', 'song.year', 'song.tempo', 'song.duration', 'artist.terms']].copy().drop_duplicates()

    songsTuples = list(songs.itertuples(index=False, name=None))

    for id,b,year,tempo,duration, genre in songsTuples:
        if year != 0:
            songList.append((id,id[:5]+"SONG", year, int(tempo), int(duration), "English"))

    return songList


#generate fake users with username, account creation date

#from https://stackoverflow.com/questions/553303/generate-a-random-date-between-two-other-dates    
def random_date_between(start, end):
    """Get a time at a proportion of a range of two formatted times.
    """
    time_format = '%m/%d/%Y'
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
        userJoinDate = random_date_between("1/1/2008", "1/1/2030")
        if userName not in userList:
            userList.add((userName, userJoinDate))
    
    return sorted(list(userList))


#generate fake friends

#generate fake playlist




#generate fake plays 