import sqlite3, os

db_path = os.path.join(os.path.dirname(__file__), 'books-collection.db')

db = sqlite3.connect(db_path)
cursor = db.cursor()


cursor.execute("CREATE TABLE IF NOT EXISTS books \
               (id INTEGER PRIMARY KEY, \
               title TEXT NOT NULL UNIQUE, \
               author TEXT NOT NULL, \
               rating FLOAT NOT NULL)")

cursor.execute("INSERT INTO books (title, author, rating) VALUES ('Kartar sing', 'Abhay Kumar', '3.3')")
cursor.execute("INSERT INTO books (title, author, rating) VALUES ('Nilam Sing', 'kita-su', '9.1')")

db.commit()