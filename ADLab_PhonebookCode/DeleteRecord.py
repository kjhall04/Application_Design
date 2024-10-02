import sqlite3

def delete_record(first_name, last_name):
    # Connect to the SQLite database
    conn = sqlite3.connect('phonebook.db')
    
    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()
    
    # Define the SQL query to delete a record
    delete_query = '''
    DELETE FROM person
    WHERE FName = ? AND LName = ?;
    '''
    
    # Execute the query with the provided values
    cursor.execute(delete_query, (first_name, last_name))
    
    # Commit the changes to the database
    conn.commit()
    
    # Close the connection
    conn.close()
    
    print(f"\nRecord deleted: {first_name} {last_name}")