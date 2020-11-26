import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (name, comment) VALUES (?, ?)",
            ('Simona G.', 'Wonderful startup place')
            )

cur.execute("INSERT INTO posts (name, comment) VALUES (?, ?)",
            ('Ivan G.', 'Love that it is understandable.')
            )

connection.commit()
connection.close()
