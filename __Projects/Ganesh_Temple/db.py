import sqlite3, os

db_path = os.path.join(os.path.dirname(__file__),"temple.db" )

# ONE TIME


def generate_cursor():
    con = sqlite3.connect(db_path, check_same_thread=False)
    cursor = con.cursor()
    return cursor, con


if __name__ == '__main__':
    cursor, con = generate_cursor()
    cursor.execute('create table BOOKINGS (id int, name text, email text, phone text, from_address text, to_address text, booking_date date)')
    con.close()