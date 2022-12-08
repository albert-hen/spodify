from flask import Flask,render_template,request,redirect
from spodify import *

dbfile = "spodify.sqlite"


app = Flask(__name__)

@app.route('/data')

def HelloWorld():

    return render_template('userlist.html', users = [("name", "dataeee"), ("hell yeah", "no")])



@app.route('/index')

def Index():

    return render_template('index.html')

@app.route('/users')

def GetUserList():
    connection = create_connection(dbfile)
    u = execute_read_query(connection, "select * from users")
    return render_template('userlist.html', users = u)

@app.route('/topsongs',methods = ['GET','POST'])
def GetTopSongs():

    if request.method == 'POST':
        year = request.form['year']
        connection = create_connection(dbfile)
        topsongs = execute_read_query(connection, top_songs_year(year))
        return render_template('toplist.html', topsongs = topsongs)
    
    return render_template('top.html')

@app.route('/topartists',methods = ['GET','POST'])
def GetTopArtists():

    if request.method == 'POST':
        year = request.form['year']
        connection = create_connection(dbfile)
        artists = execute_read_query(connection, most_listened_artist_year(year))
        return render_template('toplistartists.html', artists = artists)
    
    return render_template('top_artists.html')

@app.route('/songs',methods = ['GET'])
def GetSongs():

    query = "select sID, sName, aID, aName from songs join artists on artists.aID = songs.sArtist"
        
    connection = create_connection(dbfile)
    songs = execute_read_query(connection, query)
    return render_template('songlist.html', songs = songs)

@app.route('/playsong',methods = ['GET','POST'])
def PlaySong():

    if request.method == 'POST':
        user = request.form['user']
        song = request.form['song']
        date = request.form['date']
        connection = create_connection(dbfile)
        artists = execute_query(connection, add_song_play_query(user,song,date))
        return 'song played!'
    
    return render_template('playform.html')


app.run(host='localhost', port=5000)