import sqlite3

conn = sqlite3.connect('champions.db')

cursor = conn.cursor()

cursor.execute("DROP TABLE top")
cursor.execute("DROP TABLE jungle")
cursor.execute("DROP TABLE mid")
cursor.execute("DROP TABLE adc")
cursor.execute("DROP TABLE support")
