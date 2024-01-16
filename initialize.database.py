import sqlite3

# Connect to the SQLite database (creates a new database file if it doesn't exist)
conn = sqlite3.connect('your_database.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Define the Table Structure (SQL Statements)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Vulnerabilities (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        description TEXT,
        severity TEXT,
        affected_system TEXT,
        date_discovered DATE
        -- Add more columns as needed
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

