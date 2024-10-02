import sqlite3

def view_records():
    # Connect to the SQLite database
    conn = sqlite3.connect('phonebook.db')
    
    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()

    # Create query to find all values
    search_query = '''
    SELECT * FROM person
    '''
    
    # execute the query command
    cursor.execute(search_query)

    # put the data found into a variable
    rows = cursor.fetchall()

    # prints all the data from the tuples in an orderly fashion
    print()
    for row in rows:
        id, Fname, Lname, phone_number = row
        print(f"Name: {Fname} {Lname}, Phone Number: {phone_number}")

    # Close database
    conn.close()