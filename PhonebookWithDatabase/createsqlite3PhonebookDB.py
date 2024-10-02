import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('phonebook.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create the 'person' table with columns: FName, LName, and Phone
create_table_query = '''
CREATE TABLE IF NOT EXISTS person (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    FName TEXT NOT NULL,
    LName TEXT NOT NULL,
    Phone TEXT NOT NULL
);
'''

# Execute the table creation query
cursor.execute(create_table_query)

# Commit the changes to the database
conn.commit()

# Close the connection
conn.close()

print("Phonebook database and person table created successfully.")