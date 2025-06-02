import sqlite3, os

db_path = os.path.join(os.path.dirname(__file__),"events.db" )

# ONE TIME


def generate_cursor():
    con = sqlite3.connect(db_path, check_same_thread=False)
    cursor = con.cursor()
    return cursor, con

def init_db():
    cursor, con = generate_cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS events (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        summary TEXT,
        description TEXT,
        event_date DATE NOT NULL,
        event_time TIME NOT NULL,
        location TEXT NOT NULL,
        meeting_point TEXT,
        distance FLOAT,
        difficulty TEXT CHECK(difficulty IN ('Easy', 'Medium', 'Hard')),
        event_type TEXT CHECK(event_type IN ('Hiking', 'Camping', 'Photography', 'Wildlife', 'Adventure')),
        max_participants INTEGER,
        what_to_bring TEXT,
        contact_info TEXT,
        organizer_name TEXT NOT NULL,
        image_path TEXT,
        status TEXT DEFAULT 'Open',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    con.commit()
    con.close()

if __name__ == '__main__':
    init_db()