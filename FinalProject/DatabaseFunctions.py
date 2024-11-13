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
        username, password = row
        data.append(row)

    conn.close()
    return data

if __name__ == '__main__':
    get_login_data()