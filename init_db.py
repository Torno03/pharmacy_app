import sqlite3

conn = sqlite3.connect('medicine.db')
c = conn.cursor()

c.execute('''CREATE TABLE medicine (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    generic_name TEXT NOT NULL,
    quantity INTEGER NOT NULL CHECK(quantity >= 0),
    price REAL NOT NULL
)''')

conn.commit()
conn.close()

