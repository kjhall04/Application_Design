import sqlite3

# Retrieve all login data
def get_login_data() -> list:
    # Connect to database
    conn = sqlite3.connect('EquipmentManager\\EquipmentLogs.db')
    conn.execute("PRAGMA foreign_keys = ON;")
    cursor = conn.cursor()

    # Query for getting username and password
    search_query = '''
    SELECT Username, Password FROM login_data
    '''
    # Get data and put into a list
    cursor.execute(search_query)
    rows = cursor.fetchall()
    data = []
    for row in rows:
        data.append(row)

    # Close database and return the data list
    conn.close()
    return data

# Retrieve contact data
def get_contact_data() -> list:
    # Connect to database
    conn = sqlite3.connect('EquipmentManager\\EquipmentLogs.db')
    conn.execute("PRAGMA foreign_keys = ON;")
    cursor = conn.cursor()

    # Search query for contact info
    search_query = '''
    SELECT Fname, Lname, PhoneNumber, Email FROM contact
    '''
    # Put data into a list
    cursor.execute(search_query)
    rows = cursor.fetchall()
    data = []
    for row in rows:
        data.append(row)

    # Close database
    conn.close()
    return data

# Retrieve equipment data
def get_equipment_data() -> list:
    # Connect to database
    conn = sqlite3.connect('EquipmentManager\\EquipmentLogs.db')
    conn.execute("PRAGMA foreign_keys = ON;")
    cursor = conn.cursor()

    # Search query for all the equipment values
    search_query = '''
    SELECT contact_id, Ename, DateInstalled, Decomissioned, DecomissionedDate,
    MaintenanceDate, Department FROM equipment
    '''
    # Retrieve data and put into a list
    cursor.execute(search_query)
    rows = cursor.fetchall()
    data = []
    for row in rows:
        data.append(row)

    # Exit database
    conn.close()
    return data

# Add login data to database
def add_login(fname:str, lname:str, username:str, password:str) -> str | bool | None:
    # Connect to database
    conn = sqlite3.connect('EquipmentManager\\EquipmentLogs.db')
    conn.execute("PRAGMA foreign_keys = ON;")
    cursor = conn.cursor()

    # Data to insert
    insert_query = '''
    INSERT INTO login_data (Fname, Lname, Username, Password)
    VALUES (?, ?, ?, ?);
    '''
    data = fname, lname, username, password

    if validate_database_entry('login_data', data):
        return 'This user data is already in use.'
    else:
        cursor.execute(insert_query, data)
        conn.commit()
    
    conn.close()

    return True

# Add contact data to database
def add_contact(fname:str, lname:str, phone_number:str, email:str) -> str | bool | None:
    # Connect to database
    conn = sqlite3.connect('EquipmentManager\\EquipmentLogs.db')
    conn.execute("PRAGMA foreign_keys = ON;")
    cursor = conn.cursor()

    # Data to insert
    insert_query = '''
    INSERT INTO contact (Fname, Lname, PhoneNumber, Email)
    VALUES (?, ?, ?, ?);
    '''
    data = fname, lname, phone_number, email

    if validate_database_entry('contact', data):
        return 'This data is already in the database.'
    else:
        cursor.execute(insert_query, data)
        conn.commit()
    
    conn.close()

    return True

# Add equipment data to database
def add_equipment(fname:str, lname:str, ename:str, date_installed:str, decomissioned:str, decomisioned_date:str, 
                  maintenance_date:str, department:str) -> str | bool | None:
    # Connect to database
    conn = sqlite3.connect('EquipmentManager\\EquipmentLogs.db')
    conn.execute("PRAGMA foreign_keys = ON;")
    cursor = conn.cursor()

    # Data to insert
    insert_query = '''
    INSERT INTO equipment (contact_id, Ename, DateInstalled, Decomissioned, DecomissionedDate, MaintenanceDate, Department)
    VALUES (?, ?, ?, ?, ?, ?, ?);
    '''
    # Get the contact id from the contact list to connect equipment to contact
    contact_id = get_contact_id(fname, lname)

    data = contact_id, ename, date_installed, decomissioned, decomisioned_date, maintenance_date, department

    if validate_database_entry('equipment', data):
        return 'This data is already in the database.'
    else:
        cursor.execute(insert_query, data)
        conn.commit()
    
    conn.close()

    return True

# Retireve the contact id for the equipment table
def get_contact_id(fname:str, lname:str) -> int:
    # Connect to database
    conn = sqlite3.connect('EquipmentManager\\EquipmentLogs.db')
    conn.execute("PRAGMA foreign_keys = ON;")
    cursor = conn.cursor()

    # Where to search
    search_query = '''
    SELECT id FROM contact WHERE Fname = ? AND Lname = ?
    '''
    # If search for the id where there is a specific first name and last name
    cursor.execute(search_query, (fname, lname))
    contact_id = cursor.fetchone()

    if contact_id is None:
        # Either return a default value or raise an exception
        conn.close()
        return f"No contact found with first name '{fname}' and last name '{lname}'"
    
    # return the first value from the fetchone tuple (this is the id for the proper contact)
    conn.close()
    return contact_id[0]

def validate_database_entry(table_name:str, data:list) -> bool:
    # Connect to database
    conn = sqlite3.connect('EquipmentManager\\EquipmentLogs.db')
    conn.execute("PRAGMA foreign_keys = ON;")
    cursor = conn.cursor()

    # Build a query that matches the specific columns of the table
    if table_name == 'login_data':
        validate_query = '''SELECT Fname, Lname, Username, Password FROM login_data WHERE Fname = ? 
                            AND Lname = ? AND Username = ? AND Password = ?'''
    elif table_name == 'contact':
        validate_query = '''SELECT Fname, Lname, PhoneNumber, Email FROM contact WHERE Fname = ? 
                            AND Lname = ? AND PhoneNumber = ? AND Email = ?'''
    elif table_name == 'equipment':
        validate_query = '''SELECT contact_id, Ename, DateInstalled, Decomissioned, DecomissionedDate, 
                            MaintenanceDate, Department FROM equipment WHERE contact_id = ? 
                            AND Ename = ? AND DateInstalled = ? AND Decomissioned = ? AND DecomissionedDate = ? 
                            AND MaintenanceDate = ? AND Department = ?'''
    else:
        return False  # Invalid table name

    # Execute the validation query
    cursor.execute(validate_query, data)
    result = cursor.fetchone()

    # If the result is None, the data doesn't exist, so we return False
    if result is None:
        return False
    return True  # If the result is not None, the data already exists

def get_all_data_for_menu() -> list:
    conn = sqlite3.connect('EquipmentManager\\EquipmentLogs.db')
    conn.execute("PRAGMA foreign_keys = ON;")
    cursor = conn.cursor()

    # Use LEFT JOIN to include all contacts, even if they don't have equipment
    query = '''
    SELECT
        contact.Fname,
        contact.Lname,
        equipment.Ename,
        equipment.Department
    FROM
        contact
    LEFT JOIN
        equipment
    ON
        contact.id = equipment.contact_id
    ORDER BY
        contact.Fname, contact.Lname;
    '''
    cursor.execute(query)

    results = cursor.fetchall()

    data_list = []
    for row in results:
        # Append each record as a list
        data_list.append({
            "Fname": row[0],
            "Lname": row[1],
            "Ename": row[2] if row[2] else "No Equipment",  # Handle NULL values
            "Department": row[3] if row[3] else "N/A",  # Handle NULL values
        })

    conn.close()

    return data_list

# Test functionality here
if __name__ == '__main__':

    # print(add_contact('John', 'Estes', '601-987-4566', 'jestes@gmail.com'))
    # print(add_equipment('John', 'Estes', 'Desktop', '10/04/2024', 'False', 'N/A', '01/01/2025', 'I.T.'))

    # print(get_login_data())
    # print(get_contact_data())
    # print(get_equipment_data())
    
    print(get_all_data_for_menu())
    # print(add_login('Kaleb', 'Hall', 'manager4', '12345678'))

    pass