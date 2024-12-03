# Creates the pdf report of all the equipment data
import sqlite3
from fpdf import FPDF, XPos, YPos
import os
import platform

# Initialize PDF
class PDF(FPDF):
    def __init__(self):
        super().__init__()
        # Set page margins and bottom page margin
        self.set_margins(10, 10, 10)
        self.set_auto_page_break(auto=True, margin=15)

    def header(self):
        # Set parameters for the header of the pdf
        self.set_font('Helvetica', 'B', 12)
        self.cell(0, 10, 'Database Report: Contacts and Equipment', 0, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')

    def chapter_title(self, title):
        # Set parameters for any titles
        self.set_font('Helvetica', 'B', 10)
        self.cell(0, 10, title, 0, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='L')
        self.ln(2)

    def chapter_body(self, body):
        # Set parameters for any other text
        self.set_font('Helvetica', '', 10)
        self.multi_cell(0, 5, body)  # Use smaller line spacing for dense content
        self.ln()

    def check_space(self, content_height):
        # Check the space left to see if should go to the next page
        if self.get_y() + content_height > self.h - 15:  # 15 for bottom margin
            self.add_page()

# Function to open the PDF with the users system
def open_pdf(file_path):
    system = platform.system()
    if system == 'Windows':
        os.startfile(file_path)
    elif system == 'Darwin':  # macOS
        os.system(f'open {file_path}')
    elif system == 'Linux':
        os.system(f'xdg-open {file_path}')
    else:
        return f'Unsupported OS: {system}. Please open the file manually.'

# Function to generate PDF
def generate_pdf():
    pdf = PDF()
    pdf.add_page()

    # Connect to SQLite database
    conn = sqlite3.connect('EquipmentManager\\EquipmentLogs.db')
    cursor = conn.cursor()

    # Fetch contacts and their associated equipment and retrieve all data
    cursor.execute('''
        SELECT 
            c.id, c.Fname, c.Lname, c.PhoneNumber, c.Email, 
            e.Ename, e.DateInstalled, e.Decomissioned, e.DecomissionedDate, 
            e.MaintenanceDate, e.Department
        FROM contact c
        LEFT JOIN equipment e ON c.id = e.contact_id
        ORDER BY c.id
    ''')
    data = cursor.fetchall()

    # Process the results
    current_contact_id = None
    for row in data:
        contact_id = row[0]
        if contact_id != current_contact_id:
            # New contact: Add their details
            pdf.check_space(15)  # Reserve space for contact details
            pdf.chapter_title(f'Name: {row[1]} {row[2]}')
            pdf.chapter_body(f'Phone: {row[3]}\nEmail: {row[4]}')
            current_contact_id = contact_id

        # Add equipment details if available
        if row[5]:  # Check if equipment exists
            equipment_details = (f'  Equipment: {row[5]}\n    Date Installed: {row[6]}\n    '
                                 f'Decomissioned: {row[7]}\n    Decomissioned Date: {row[8]}\n    '
                                 f'Maintenance Date: {row[9]}\n    Department: {row[10]}')
            # Reserve space for equipment details (estimate multi-line content height)
            pdf.check_space(len(equipment_details.split('\n')) * 5)
            pdf.chapter_body(equipment_details)

    # Close database
    conn.close()

    # Output PDF
    output_file = 'EquipmentManager\\Contact_Equipment_Report.pdf'
    pdf.output(output_file)

    # Open the PDF
    return open_pdf(output_file)

# Test if needed
if __name__ == "__main__":
    print(generate_pdf())