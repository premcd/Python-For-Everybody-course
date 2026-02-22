#exercice qui vise a recuperer les orgs des emails sender d'un fichier .txt en ligne et de remplir une database (sqlite) avec le nbre d'email par org

import sqlite3
import re
conn = sqlite3.connect('email_db.sqlite')

cur = conn.cursor()

cur.execute('''DROP
TABLE IF EXISTS Counts''')

cur.execute ('''CREATE TABLE Counts
(org TEXT, count INTEGER)''')

file = input('enter file name')
if len(file)<1:
    file = 'mbox.txt'
fhandle = open(file)
#test the content of only the first line: firstline=fhandle.readlines()[0]
#print(firstline)
for line in fhandle:
#    print(line.strip())
    list=re.findall('^From [^ ]+@([a-z.]+)', line)
#    if list != []:
#        print(line)
    for org in list:
#        print(email)
        cur.execute('SELECT count FROM Counts WHERE org = ?',(org,))
        row = cur.fetchone()
#        print(row)
        if row is None:
            cur.execute('INSERT INTO Counts (org,count) VALUES (?,1)',(org,))
        else:
            cur.execute('UPDATE Counts SET count = count+1 WHERE org = ?',(org,))
conn.commit()
sqlstr = 'SELECT org,count FROM Counts ORDER BY count DESC'
for row in cur.execute(sqlstr):
    print(row[0],row[1])
