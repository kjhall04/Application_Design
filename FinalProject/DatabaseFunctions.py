import sqlite3

def add_login_entry(fname, lname, username, password):
    conn = sqlite3.connect('EquipmentLogs.db')
    cursor = conn.cursor()

    insert_query = '''
    INSERT INTO login_data (Fname, Lname, Username, Password)
    VALUES (?, ?, ?, ?);
    '''

    cursor.execute(insert_query, (fname, lname, username, password))
    conn.commit()
    conn.close()

def get_login_data():
    conn = sqlite3.connect('EquipmentLogs.db')
    cursor = conn.cursor()

    search_query = '''
    SELECT Username, Password FROM login_data
    '''

    cursor.execute(search_query)
    rows = cursor.fetchall()
    data = []

    for row in rows:
        data.append(row)

    conn.close()
    return data

def add_user(fname, lname, phone_number, email):
    conn = sqlite3.connect('EquipmentLogs.db')
    cursor = conn.cursor()

    insert_query = '''
    INSERT INTO contact (Fname, Lname, PhoneNumber, Email)
    VALUES (?, ?, ?, ?);
    '''

    cursor.execute(insert_query, (fname, lname, phone_number, email))
    conn.commit()
    conn.close()

def add_equipment(ename, date_installed, decommissioned, decommisioned_date, equipment_age, maintenance_date, department):
    conn = sqlite3.connect('EquipmentLogs.db')
    cursor = conn.cursor()

    insert_query = '''
    INSERT INTO contact (Ename, DateInstalled, Decomissioned, DecomissionedDate, 
    EquipmentAge, MaintenanceDate, Department)
    VALUES (?, ?, ?, ?, ?, ?, ?);
    '''

    cursor.execute(insert_query, (ename, date_installed, decommissioned, decommisioned_date, equipment_age, maintenance_date, department))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    print(get_login_data())