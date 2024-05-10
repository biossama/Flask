import sqlite3

connection = sqlite3.connect("database.db")

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("insert into posts (title, content) VALUES(?, ?)", ('first post', 'content for the first post'))
cur.execute("insert into posts (title, content) VALUES(?, ?)", ('seconde post', 'content for the seconde post'))
# cur.execute("insert into posts (title, content) VALUES(?, ?)", ('thirt post', 'content for the thirt post'))
# cur.execute("insert into posts (title, content) VALUES(?, ?)", ('fouth post', 'content for the fouth post'))

connection.commit()
connection.close()
