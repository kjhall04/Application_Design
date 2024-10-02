import sqlite3

def add_record(first_name, last_name, phone_number):
    # Connect to the SQLite database
    conn = sqlite3.connect('phonebook.db')
    
    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()
    
    # Define the SQL query to insert a record
    insert_query = '''
    INSERT INTO person (FName, LName, Phone)
    VALUES (?, ?, ?);
    '''
    
    # Execute the query with the provided values
    cursor.execute(insert_query, (first_name, last_name, phone_number))
    
    # Commit the changes to the database
    conn.commit()
    
    # Close the connection
    conn.close()
    
    print(f"\nRecord added: {first_name} {last_name}, {phone_number}")