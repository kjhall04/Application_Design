import sqlite3

def create_database():
    # Connect to sqlite database if on doesn't exist
    conn = sqlite3.connect('EquipmentManager\\EquipmentLogs.db')

    # Create cursor object
    cursor = conn.cursor()

    # Create query for Contacts, Equipment, and Login Info
    create_tables_query = '''
    CREATE TABLE IF NOT EXISTS contact (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Fname TEXT NOT NULL,
        Lname TEXT NOT NULL,
        PhoneNumber TEXT NOT NULL,
        Email TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS equipment (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        contact_id INTEGER NOT NULL,
        Ename TEXT NOT NULL,
        Department TEXT NOT NULL,
        DateInstalled TEXT NOT NULL,
        MaintenanceDate TEXT NOT NULL,
        Decomissioned TEXT NOT NULL,
        DecomissionedDate TEXT NOT NULL,
        FOREIGN KEY (contact_id) REFERENCES contact(id) ON DELETE CASCADE
    );

    CREATE TABLE IF NOT EXISTS login_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Fname TEXT NOT NULL,
        Lname TEXT NOT NULL,
        Username TEXT NOT NULL,
        Password TEXT NOT NULL
    );
    '''

    # Execute table creation query
    cursor.executescript(create_tables_query)

    # Commit changes to database
    conn.commit()

    # Exit database
    conn.close()

# Test if needed
if __name__ == '__main__':
    create_database()