import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (name, comment) VALUES (?, ?)",
            ('First person name', 'Comment of first person')
            )

cur.execute("INSERT INTO posts (name, comment) VALUES (?, ?)",
            ('Second person name', 'Comment of second person')
            )

connection.commit()
connection.close()
