import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    username TEXT,
    password TEXT
)
''')

cursor.execute("INSERT INTO users (username, password) VALUES ('admin', '1234')")
cursor.execute("INSERT INTO users (username, password) VALUES ('user1', 'pass1')")

conn.commit()
conn.close()

print("✅ Fresh DB created with admin and user1")
