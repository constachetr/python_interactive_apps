
import sqlite3

# Connect to database (creates file if it doesn't exist)
conn = sqlite3.connect('student.db')

# Create a cursor
c = conn.cursor()

# Create a table
c.execute("""CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            grade TEXT,
            address TEXT,
            course_name TEXT
            )""")

# Commit changes and close the connection
conn.commit()
conn.close()
