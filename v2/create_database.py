import sqlite3

conn = sqlite3.connect('champions.db')

cursor = conn.cursor()

cursor.execute("""CREATE TABLE top (
        id integer PRIMARY KEY AUTOINCREMENT,
        name text,
        tier integer,
        winrate real,
        pickrate real,
        banrate real,
        counters text
    )
""")
cursor.execute("""CREATE TABLE jungle (
        id integer PRIMARY KEY AUTOINCREMENT,
        name text,
        tier integer,
        winrate real,
        pickrate real,
        banrate real,
        counters text
    )
""")
cursor.execute("""CREATE TABLE adc (
        id integer PRIMARY KEY AUTOINCREMENT,
        name text,
        tier integer,
        winrate real,
        pickrate real,
        banrate real,
        counters text
    )
""")
cursor.execute("""CREATE TABLE support (
        id integer PRIMARY KEY AUTOINCREMENT,
        name text,
        tier integer,
        winrate real,
        pickrate real,
        banrate real,
        counters text
    )
""")
cursor.execute("""CREATE TABLE mid (
        id integer PRIMARY KEY AUTOINCREMENT,
        name text,
        tier integer,
        winrate real,
        pickrate real,
        banrate real,
        counters text
    )
""")
