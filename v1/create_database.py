import sqlite3

conn = sqlite3.connect('champions.db')

cursor = conn.cursor()

cursor.execute("""CREATE TABLE champions (
        id integer PRIMARY KEY AUTOINCREMENT,
        name text,
        tier integer,
        winrate real,
        pickrate real,
        banrate real,
        counters text
    )
""")
