import sqlite3


def create_database():
    connection = sqlite3.connect("tracker.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company TEXT,
            position TEXT,
            date_applied TEXT,
            status TEXT,
            notes TEXT
        )
    """)

    connection.commit()
    connection.close()

    print("Database created successfully!")


create_database()

