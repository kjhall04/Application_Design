import customtkinter as ctk
import ValidateEntry
import DatabaseFunctions

# Class for the add equipment frame
class AddEquipment(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Create the frame for everything to go in
        self.container = ctk.CTkFrame(self)
        self.container.pack(expand=True, padx=20, pady=20)

        # Title label
        self.label = ctk.CTkLabel(self.container, text='Add Equipment', font=('Arial', 25))
        self.label.pack(padx=40, pady=10)

        # Entry box
        self.fname_entry = ctk.CTkEntry(self.container, placeholder_text='Contact First Name')
        self.fname_entry.pack(pady=5)

        # Entry box
        self.lname_entry = ctk.CTkEntry(self.container, placeholder_text='Contact Last Name')
        self.lname_entry.pack(pady=5)

        # Entry box
        self.ename_entry = ctk.CTkEntry(self.container, placeholder_text='Equipment Name')
        self.ename_entry.pack(pady=(15, 5))

        # Entry box
        self.date_installed_entry = ctk.CTkEntry(self.container, placeholder_text='Date Installed')
        self.date_installed_entry.pack(pady=5)

        # Entry box
        self.decomissioned_entry = ctk.CTkEntry(self.container, placeholder_text='Decomissioned')
        self.decomissioned_entry.pack(pady=5)

        # Entry box
        self.decomissioned_date_entry = ctk.CTkEntry(self.container, placeholder_text='Decomissioned Date')
        self.decomissioned_date_entry.pack(pady=5)

        # Entry box
        self.maintenance_date_entry = ctk.CTkEntry(self.container, placeholder_text='Maintenance Date')
        self.maintenance_date_entry.pack(pady=5)

        # Entry box
        self.department_entry = ctk.CTkEntry(self.container, placeholder_text='Department')
        self.department_entry.pack(pady=5)

        # Add data and run the validate function
        self.add_button = ctk.CTkButton(self.container, text='Add Equipment', command=self.validate_info)
        self.add_button.pack(pady=5)
        
        # Error label
        self.error_label = ctk.CTkLabel(self.container, text='', text_color='red')
        self.error_label.pack(padx=10)

        # Back button and clear entries on this page
        self.back_button = ctk.CTkButton(self.container, text='Back', fg_color='#243573', 
                                         command=lambda: (self.master.show_frame('Database'), self.clear_entries()))
        self.back_button.pack(pady=(5, 15))

    # Validate and add data
    def validate_info(self):
        # Assign all entry data to variables
        fname = self.fname_entry.get()
        lname = self.lname_entry.get()
        ename = self.ename_entry.get()
        date_installed = self.date_installed_entry.get()
        decomissioned = self.decomissioned_entry.get()
        decomissioned_date = self.decomissioned_date_entry.get()
        maintenance_date = self.maintenance_date_entry.get()
        department = self.department_entry.get()

        # Run validation on all info and store all results
        validation_results = [
            ('Equipment Name', ValidateEntry.other_fields(ename)),
            ('Date Installed', ValidateEntry.date(date_installed)),
            ('Decomissioned', ValidateEntry.boolean(decomissioned)),
            ('Decomissioned Date', ValidateEntry.date_or_NA(decomissioned_date)),
            ('Maintenance Date', ValidateEntry.date_or_NA(maintenance_date)),
            ('Department', ValidateEntry.other_fields(department))
        ]

        # If any return none then show error to fill in all data
        if not fname or not lname or not ename or not date_installed or not decomissioned or not decomissioned_date or not maintenance_date or not department:
            self.error_label.configure(text='Enter info into all the boxes.')
            return

        # IF any errors then show the error
        for field, result in validation_results:
            if result is not True:
                self.error_label.configure(text=f'{field}: {result}')
                return

        # Clear the error label
        self.error_label.configure(text='')

        # Run the add function and store the result
        action = DatabaseFunctions.add_equipment(fname, lname, ename, date_installed, decomissioned, decomissioned_date, maintenance_date, department)

        # If not sucessful then show error
        if action != True:
            self.error_label.configure(text=action)
        else:
            # Go back to the database and refresh data and clear entries on this page
            self.master.frames['Database'].refresh_data()
            self.master.show_frame('Database')
            self.clear_entries()
    
    # Clear entries, reset labels, and clear errors
    def clear_entries(self):
        self.fname_entry.delete(0, 'end')
        self.lname_entry.delete(0, 'end')
        self.ename_entry.delete(0, 'end')
        self.date_installed_entry.delete(0, 'end')
        self.decomissioned_entry.delete(0, 'end')
        self.decomissioned_date_entry.delete(0, 'end')
        self.maintenance_date_entry.delete(0, 'end')
        self.department_entry.delete(0, 'end')

        self.fname_entry.configure(placeholder_text='Contact First Name')
        self.lname_entry.configure(placeholder_text='Contact Last Name')
        self.ename_entry.configure(placeholder_text='Equipment Name')
        self.date_installed_entry.configure(placeholder_text='Date Installed')
        self.decomissioned_entry.configure(placeholder_text='Decomissioned')
        self.decomissioned_date_entry.configure(placeholder_text='Decomissioned Date')
        self.maintenance_date_entry.configure(placeholder_text='Maintenance Date')
        self.department_entry.configure(placeholder_text='Department')

        self.error_label.configure(text='')