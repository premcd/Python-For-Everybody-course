#this program aims at creating a multi-table normalized database storing a song library coming from a csv file
import sqlite3

conn = sqlite3.connect('songs_db.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Artist')
cur.execute('DROP TABLE IF EXISTS Genre')
cur.execute('DROP TABLE IF EXISTS Album')
cur.execute('DROP TABLE IF EXISTS Tracks')


cur.executescript('''CREATE TABLE Artist
    (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
    name  TEXT UNIQUE
);
CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);
CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);
CREATE TABLE Tracks (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    rating INTEGER,
    len INTEGER,
    count INTEGER,
    album_id INTEGER,
    genre_id INTEGER
);
''')


handle = open('tracks.csv')
for line in handle:
#    print (line.split())
    print (line)
    row = line.split(',')
    if len(row) < 6 : continue
    print(row)
    title = row[0]
    artist = row[1]
    album = row[2]
    rating = row[3]
    leng = row[4]
    count = row[5]
    genre = row[6]
    
    print('voici la liste:',title, artist, album, rating, leng, count, genre)

    cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)', (artist,))
    cur.execute('SELECT * FROM Artist WHERE name = ?', (artist,))
    a=cur.fetchone()
    print(a[0])
    cur.execute('INSERT OR IGNORE INTO Album (artist_id,title) VALUES(?,?)', (a[0],album))

    cur.execute('SELECT * FROM Album WHERE title = ?', (album,))
    b=cur.fetchone()
    print(b[0])
    
    cur.execute('INSERT OR IGNORE INTO Genre (name) VALUES (?)',(genre,))
    cur.execute('SELECT * FROM Genre WHERE name = ?', (genre,))
    c=cur.fetchone()
    print(c[0])
    cur.execute('INSERT OR IGNORE INTO Tracks (title,rating,len,count,album_id,genre_id) VALUES (?,?,?,?,?,?)',(title,rating,leng,count,b[0],c[0]))
conn.commit()

conn.close()
