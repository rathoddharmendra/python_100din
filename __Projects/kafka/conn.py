import sqlite3, os

db_path = os.path.join(os.path.dirname(__name__),"bucket.db" )

# ONE TIME


def generate_cursor():
    con = sqlite3.connect(db_path)
    cursor = con.cursor()
    return cursor, con


if __name__ == '__main__':
    cursor, con = generate_cursor()
    cursor.execute('create table dumps(id int, text text)')
