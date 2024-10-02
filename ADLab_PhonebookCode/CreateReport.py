import webbrowser
import sqlite3

def write_html():
    # connect to database
    conn = sqlite3.connect('phonebook.db')
    cursor = conn.cursor()

    # query to get all the info from database
    search_query = '''
        SELECT * FROM person
        '''
        
    # execute the query command
    cursor.execute(search_query)

    # put the data found into a variable
    rows = cursor.fetchall()

    # Create an HTML structure
    html_content = '''
    <html>
    <head>
        <title>Phonebook Report</title>
        <style>
            table {
                width: 100%;
                border-collapse: collapse;
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <h1>Phonebook Report</h1>
        <table>
            <tr>
                <th>ID</th>
                <th>First Name</th>
                <th>Last Name</th>
                <th>Phone</th>
            </tr>
    '''

    # Add data rows to the HTML
    for row in rows:
        html_content += f'''
            <tr>
                <td>{row[0]}</td>
                <td>{row[1]}</td>
                <td>{row[2]}</td>
                <td>{row[3]}</td>
            </tr>
        '''

    # Closing HTML tags
    html_content += '''
        </table>
    </body>
    </html>
    '''

    output_file = 'phonebook_report.html'

    # Write the HTML content to a file
    with open(output_file, 'w') as file:
        file.write(html_content)

    # Close the database connection
    conn.close()

    print(f"\nHTML report generated: {output_file}")

def printreport():
    # Specify the path to your HTML file
    html_file = 'phonebook_report.html'
    
    # Open the HTML file in the default web browser
    webbrowser.open(html_file)