import sqlite3

def create_database():
    # connect to sqlite database if on doesn't exist
    conn = sqlite3.connect('EquipmentManager\\EquipmentLogs.db')

    # create cursor object
    cursor = conn.cursor()

    # create query for Contacts, Equipment, and Login Info
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
        DateInstalled TEXT NOT NULL,
        Decomissioned TEXT NOT NULL,
        DecomissionedDate TEXT NOT NULL,
        EquipmentAge TEXT NOT NULL,
        MaintenanceDate TEXT NOT NULL,
        Department TEXT NOT NULL,
        FOREIGN KEY (contact_id) REFERENCES contact(id)
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

    print('Equipment database created successfully.')

if __name__ == '__main__':
    create_database()