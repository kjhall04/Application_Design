import sqlite3

def search_record(Fname, Lname):
    # Connect to the SQLite database
    conn = sqlite3.connect('phonebook.db')
    
    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()

    # Define the SQL query to search the records
    search_query = '''
    SELECT FName, LName, Phone FROM person
    WHERE FName = ? AND LName = ?
    '''

    # Execute the query with the provided names
    cursor.execute(search_query, (Fname, Lname))

    # put the matching values into a variable
    matching_rows = cursor.fetchall()

    # if there is a match, print it out or print no match found
    if matching_rows:
        for row in matching_rows:
            Fname, Lname, phone_number = row
        print(f"\nName: {Fname} {Lname}, Phone Number: {phone_number}")
    else:
        print("\nNo match found.")

    # Close the database
    conn.close()