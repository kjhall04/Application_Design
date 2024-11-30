import sqlite3

class DatabaseManager:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.conn.execute("PRAGMA foreign_keys = ON;")
        self.conn.execute("PRAGMA busy_timeout = 5000;")  # Wait 5 seconds before raising a lock error
        self.cursor = self.conn.cursor()

    def execute_query(self, query, params=(), fetch_all=True):
        self.cursor.execute(query, params)
        self.conn.commit()
        if fetch_all:
            return self.cursor.fetchall()
        return None

    def close(self):
        self.conn.close()


# Initialize a single database manager instance
db_manager = DatabaseManager('EquipmentManager\\EquipmentLogs.db')


# Retrieve all login data
def get_login_data() -> list:
    query = '''
    SELECT Username, Password FROM login_data
    '''
    return db_manager.execute_query(query)


# Retrieve contact data
def get_contact_data() -> list:
    query = '''
    SELECT Fname, Lname, PhoneNumber, Email FROM contact
    '''
    return db_manager.execute_query(query)


# Retrieve equipment data
def get_equipment_data() -> list:
    query = '''
    SELECT contact_id, Ename, DateInstalled, Decomissioned, DecomissionedDate,
           MaintenanceDate, Department
    FROM equipment
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
        db_manager.execute_query(query, data, fetch_all=False)
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
        db_manager.execute_query(query, data, fetch_all=False)
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
    data = contact_id, ename, date_installed, decomissioned, decomissioned_date, maintenance_date, department

    if validate_database_entry('equipment', data):
        return 'This data is already in the database.'
    else:
        db_manager.execute_query(query, data, fetch_all=False)
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
    result = db_manager.execute_query(query, (fname, lname))
    if not result:
        return f"No contact found with first name '{fname}' and last name '{lname}'"
    return result[0][0]  # Return the ID


# Validate if data already exists in the database
def validate_database_entry(table_name: str, data: list) -> bool:
    if table_name == 'login_data':
        query = '''
        SELECT Fname, Lname, Username, Password FROM login_data 
        WHERE Fname = ? AND Lname = ? AND Username = ? AND Password = ?
        '''
    elif table_name == 'contact':
        query = '''
        SELECT Fname, Lname, PhoneNumber, Email FROM contact 
        WHERE Fname = ? AND Lname = ? AND PhoneNumber = ? AND Email = ?
        '''
    elif table_name == 'equipment':
        query = '''
        SELECT contact_id, Ename, DateInstalled, Decomissioned, DecomissionedDate, 
               MaintenanceDate, Department 
        FROM equipment 
        WHERE contact_id = ? AND Ename = ? AND DateInstalled = ? 
              AND Decomissioned = ? AND DecomissionedDate = ? 
              AND MaintenanceDate = ? AND Department = ?
        '''
    else:
        return False

    result = db_manager.execute_query(query, data)
    return bool(result)


# Retrieve combined data for menu
def get_all_data_for_menu() -> list:
    query = '''
    SELECT
        contact.Fname,
        contact.Lname,
        equipment.Ename
    FROM
        contact
    LEFT JOIN
        equipment
    ON
        contact.id = equipment.contact_id
    ORDER BY
        contact.Fname, contact.Lname;
    '''
    results = db_manager.execute_query(query)

    data_list = []
    for row in results:
        data_list.append({
            "Fname": row[0],
            "Lname": row[1],
            "Ename": row[2] if row[2] else "No Equipment",  # Handle NULL values
            "Department": row[3] if row[3] else "N/A",  # Handle NULL values
        })

    return data_list

# Test functionality here
if __name__ == '__main__':

    # print(add_contact('Henry', 'Jones', '601-895-2344', 'hjones@gmail.com'))
    # print(add_equipment('Henry', 'Jones', 'Router', '10/04/2024', 'False', 'N/A', '01/01/2025', 'I.T.'))

    # print(get_login_data())
    # print(get_contact_data())
    # print(get_equipment_data())
    
    # print(get_all_data_for_menu())
    # print(add_login('Kaleb', 'Hall', 'manager4', '12345678'))

    pass