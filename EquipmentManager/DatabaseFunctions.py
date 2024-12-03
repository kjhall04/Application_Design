import sqlite3
import os

# Class to manage database functions
class DatabaseManager:
    def __init__(self, db_path):
        # When init connect ot database and trun on keys and timeout in case too many actions occur
        self.conn = sqlite3.connect(db_path)
        self.conn.execute('PRAGMA foreign_keys = ON;')
        self.conn.execute('PRAGMA busy_timeout = 5000;')  # Wait 5 seconds before raising a lock error
        self.cursor = self.conn.cursor()

    def execute_query(self, query, params=(), fetch_all=True):
        # For any action pass execute with query with any data parameters and fetch_all data if needed
        self.cursor.execute(query, params)
        self.conn.commit()
        if fetch_all:
            return self.cursor.fetchall()
        return None

    def close(self):
        # Close database
        self.conn.close()


# Initialize a single database instance
db_path = os.path.join('EquipmentManager', 'EquipmentLogs.db')
db_manager = DatabaseManager(db_path)

# Retrieve all login data
def get_login_data() -> list:
    # Get login data and return retrieved data
    query = '''
    SELECT Username, Password FROM login_data
    '''
    return db_manager.execute_query(query)


# Retrieve contact data
def get_contact_data() -> list:
    # Get contact data and return retrieved data
    query = '''
    SELECT Fname, Lname, PhoneNumber, Email FROM contact
    '''
    return db_manager.execute_query(query)


# Retrieve equipment data
def get_equipment_data() -> list:
    # Get equipment data and return retrieved data
    query = '''
    SELECT contact_id, Ename, Department, DateInstalled, MaintenanceDate, 
           Decomissioned, DecomissionedDate
    FROM equipment
    '''
    return db_manager.execute_query(query)


# Add login data to the database
def add_login(fname: str, lname: str, username: str, password: str) -> str | bool:
    # Insert Query and data to insert
    query = '''
    INSERT INTO login_data (Fname, Lname, Username, Password)
    VALUES (?, ?, ?, ?);
    '''
    data = fname, lname, username, password

    # Check to see if data is already in the databse
    if validate_database_entry('login_data', data):
        return 'This user data is already in use.'
    else:
        # Execute the query and add the data only
        db_manager.execute_query(query, data, fetch_all=False)
        return True


# Add contact data to the database
def add_contact(fname: str, lname: str, phone_number: str, email: str) -> str | bool:
    # Insert Query and data to insert
    query = '''
    INSERT INTO contact (Fname, Lname, PhoneNumber, Email)
    VALUES (?, ?, ?, ?);
    '''
    data = fname, lname, phone_number, email

    # Check to see if data is already in the database
    if validate_database_entry('contact', data):
        return 'This data is already in the database.'
    else:
        # Execute the query and add the data only
        db_manager.execute_query(query, data, fetch_all=False)
        return True


# Add equipment data to the database
def add_equipment(fname: str, lname: str, ename: str, department: str, date_installed: str, 
                   maintenance_date: str, decomissioned: str, decomissioned_date: str) -> str | bool:
    # Get the contact_id of the associated contact
    contact_id = get_contact_id(fname, lname)
    if isinstance(contact_id, str):
        return contact_id  # Return error message if no contact is found

    # Insert query and data
    query = '''
    INSERT INTO equipment (contact_id, Ename, Department, DateInstalled, MaintenanceDate, 
                           Decomissioned, DecomissionedDate)
    VALUES (?, ?, ?, ?, ?, ?, ?);
    '''
    data = contact_id, ename, department, date_installed, maintenance_date, decomissioned, decomissioned_date

    # Check if data is already in the database
    if validate_database_entry('equipment', data):
        return 'This data is already in the database.'
    else:
        # Execute the query and add the data only
        db_manager.execute_query(query, data, fetch_all=False)
        return True


# Retrieve the contact id for the equipment table
def get_contact_id(fname: str, lname: str) -> str | int:
    # Select query
    query = '''
    SELECT id FROM contact WHERE Fname = ? AND Lname = ?
    '''
    # See if a result is found with the given name data
    result = db_manager.execute_query(query, (fname, lname))
    if not result:
        # If not succesful then error
        return f"No contact found with first name '{fname}' and last name '{lname}'"
    # Return the id result
    return result[0][0]  # Return the ID


# Validate if data already exists in the database
def validate_database_entry(table_name: str, data: list) -> bool:
    # Login data query
    if table_name == 'login_data':
        query = '''
        SELECT Fname, Lname, Username, Password FROM login_data 
        WHERE Fname = ? AND Lname = ? AND Username = ? AND Password = ?
        '''
    # Contact data query
    elif table_name == 'contact':
        query = '''
        SELECT Fname, Lname, PhoneNumber, Email FROM contact 
        WHERE Fname = ? AND Lname = ? AND PhoneNumber = ? AND Email = ?
        '''
    # Equipment data query
    elif table_name == 'equipment':
        query = '''
        SELECT contact_id, Ename, Department, MaintenanceDate, DateInstalled,
               Decomissioned, DecomissionedDate
        FROM equipment 
        WHERE contact_id = ? AND Ename = ? AND Department = ? 
              AND DateInstalled = ? AND MaintenanceDate = ?
              AND Decomissioned = ? AND DecomissionedDate = ? 
        '''
    else:
        return False

    # Execute query and return bool of result
    result = db_manager.execute_query(query, data)
    return bool(result)


# Retrieve combined data for menu
def get_all_data_for_menu() -> list:
    # Data query to search and join data and return data to display
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

    # List of data to return
    data_list = []
    # Arrange data for the menu and return the list
    for row in results:
        data_list.append({
            'Fname': row[0],
            'Lname': row[1],
            # If now value for equipment name then assign N/A
            'Ename': row[2] if row[2] else 'N/A'
        })
    return data_list

# Delete contact and connected quipment
def delete_contact_and_equipment(fname: str, lname: str, phone_number: str, email: str) -> bool:
    # Delete query and data
    delete_query = '''
    DELETE FROM contact WHERE Fname = ? AND Lname = ? AND PhoneNumber = ? AND Email = ?;
    '''
    data = fname, lname, phone_number, email

    # Execute query and delete data only
    db_manager.execute_query(delete_query, data, fetch_all=False)
    return True

# Delete equipment
def delete_equipment(ename: str, date_installed: str, decomissioned: str, 
                     decomissioned_date: str, maintenance_date: str, department: str) -> bool:
    # Delete query and data
    delete_query = '''
    DELETE FROM equipment WHERE Ename = ? AND Department = ? AND DateInstalled = ? AND MaintenanceDate = ? AND Decomissioned = ? AND DecomissionedDate = ?;
    '''
    data = ename, date_installed, decomissioned, decomissioned_date, maintenance_date, department

    # Execute query nd delete data only
    db_manager.execute_query(delete_query, data, fetch_all=False)
    return True

# Updates single data values in contact or equipment entries
def update_single_data(table_name: str, column_to_update: str, new_value: str, conditions: dict) -> bool:
    # table_name is where value is located
    # column_to_update is which value type to update
    # new_value is the new value
    # conditions is the other values with the data to help find which row to update
    
    # If any is false or none then stop
    if not table_name or not column_to_update or not conditions:
        return False
    
    # If no condiions and make sure conditions is a dict
    if not isinstance(conditions, dict) or len(conditions) == 0:
        return False

    # Build the WHERE clause dynamically from conditions
    where_clause = " AND ".join([f"{col} = ?" for col in conditions.keys()])
    where_values = list(conditions.values())

    # Build the SQL query
    query = f"UPDATE {table_name} SET {column_to_update} = ? WHERE {where_clause};"
    params = [new_value] + where_values

    # Execute the query and update the data only
    result = db_manager.execute_query(query, params, fetch_all=False)
    # To make sure the database actually updates
    if result is None:
        return True
    else:
        return False

# Close the database connection when done
def close_database() -> None:
    db_manager.close()


# Test functionality here
if __name__ == '__main__':

    # print(add_contact('John', 'Estes', '678-822-4111', 'jestes@gmail.com'))
    # print(add_equipment('John', 'Estes', 'Laptop', '10/04/2024', 'False', 'N/A', '01/01/2025', 'IT'))

    # print(get_login_data())
    # print(get_contact_data())
    # print(get_equipment_data())
    
    # print(get_all_data_for_menu())
    # print(add_login('Kaleb', 'Hall', 'manager4', '12345678'))

    pass