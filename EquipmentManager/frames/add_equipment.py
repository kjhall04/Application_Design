import customtkinter as ctk
import ValidateEntry
import DatabaseFunctions

class AddEquipment(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.container = ctk.CTkFrame(self)
        self.container.pack(expand=True, padx=20, pady=20)

        self.label = ctk.CTkLabel(self.container, text='Add Equipment', font=('Arial', 25))
        self.label.pack(padx=40, pady=10)

        self.fname_entry = ctk.CTkEntry(self.container, placeholder_text='Contact First Name')
        self.fname_entry.pack(pady=5)

        self.lname_entry = ctk.CTkEntry(self.container, placeholder_text='Contact Last Name')
        self.lname_entry.pack(pady=5)

        self.ename_entry = ctk.CTkEntry(self.container, placeholder_text='Equipment Name')
        self.ename_entry.pack(pady=(15, 5))

        self.date_installed_entry = ctk.CTkEntry(self.container, placeholder_text='Date Installed')
        self.date_installed_entry.pack(pady=5)

        self.decomissioned_entry = ctk.CTkEntry(self.container, placeholder_text='Decomissioned')
        self.decomissioned_entry.pack(pady=5)

        self.decomissioned_date_entry = ctk.CTkEntry(self.container, placeholder_text='Decomissioned Date')
        self.decomissioned_date_entry.pack(pady=5)

        self.maintenance_date_entry = ctk.CTkEntry(self.container, placeholder_text='Maintenance Date')
        self.maintenance_date_entry.pack(pady=5)

        self.department_entry = ctk.CTkEntry(self.container, placeholder_text='Department')
        self.department_entry.pack(pady=5)

        self.add_button = ctk.CTkButton(self.container, text='Add Equipment', command=self.validate_info)
        self.add_button.pack(pady=5)

        self.error_label = ctk.CTkLabel(self.container, text='', text_color='red')
        self.error_label.pack(padx=10)

        self.back_button = ctk.CTkButton(self.container, text='Back', fg_color='#243573', command=lambda: (self.master.show_frame('Database'), self.clear_entries()))
        self.back_button.pack(pady=(5, 15))

    def validate_info(self):
        fname = self.fname_entry.get()
        lname = self.lname_entry.get()
        ename = self.ename_entry.get()
        date_installed = self.date_installed_entry.get()
        decomissioned = self.decomissioned_entry.get()
        decomissioned_date = self.decomissioned_date_entry.get()
        maintenance_date = self.maintenance_date_entry.get()
        department = self.department_entry.get()

        validation_results = [
            ('Equipment Name', ValidateEntry.other_fields(ename)),
            ('Date Installed', ValidateEntry.date(date_installed)),
            ('Decomissioned', ValidateEntry.boolean(decomissioned)),
            ('Decomissioned Date', ValidateEntry.decomissioned_date(decomissioned_date)),
            ('Maintenance Date', ValidateEntry.date(maintenance_date)),
            ('Department', ValidateEntry.other_fields(department))
        ]

        if not fname or not lname or not ename or not date_installed or not decomissioned or not decomissioned_date or not maintenance_date or not department:
            self.error_label.configure(text='Enter info into all the boxes.')
            return

        for field, result in validation_results:
            if result is not True:
                self.error_label.configure(text=f'{field}: {result}')
                return

        self.error_label.configure(text='')  # Clear error label

        action = DatabaseFunctions.add_equipment(fname, lname, ename, date_installed, decomissioned, decomissioned_date, maintenance_date, department)

        if action != True:
            self.error_label.configure(text=action)
        else:
            self.master.show_frame('Database')
            self.clear_entries()
    
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