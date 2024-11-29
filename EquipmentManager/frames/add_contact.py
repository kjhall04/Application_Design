import customtkinter as ctk
import ValidateEntry
import DatabaseFunctions

class AddContact(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.container = ctk.CTkFrame(self)
        self.container.pack(expand=True, padx=20, pady=20)

        self.label = ctk.CTkLabel(self.container, text='Add Contact', font=('Arial', 25))
        self.label.pack(padx=40, pady=10)

        self.fname_entry = ctk.CTkEntry(self.container, placeholder_text='First Name')
        self.fname_entry.pack(pady=5)

        self.lname_entry = ctk.CTkEntry(self.container, placeholder_text='Last Name')
        self.lname_entry.pack(pady=5)

        self.phone_number_entry = ctk.CTkEntry(self.container, placeholder_text='Phone Number')
        self.phone_number_entry.pack(pady=5)

        self.email_entry = ctk.CTkEntry(self.container, placeholder_text='Email')
        self.email_entry.pack(pady=5)

        self.add_button = ctk.CTkButton(self.container, text='Add Contact', command=self.validate_info)
        self.add_button.pack(pady=5)

        self.error_label = ctk.CTkLabel(self.container, text='', text_color='red')
        self.error_label.pack(padx=10)

        self.back_button = ctk.CTkButton(self.container, text='Back', fg_color='#243573', command=lambda: (self.master.show_frame('Database'), self.clear_entries()))
        self.back_button.pack(pady=(5, 15))

    def validate_info(self):
        fname = self.fname_entry.get()
        lname = self.lname_entry.get()
        phonenumber = self.phone_number_entry.get()
        email = self.email_entry.get()

        validation_results = [
            ('First name', ValidateEntry.name(fname)),
            ('Last name', ValidateEntry.name(lname)),
            ('Phone Number', ValidateEntry.phone_number(phonenumber)),
            ('Email', ValidateEntry.email(email)),
        ]

        if not fname or not lname or not phonenumber or not email:
            self.error_label.configure(text='Enter info into all the boxes.')
            return

        for field, result in validation_results:
            if result is not True:
                self.error_label.configure(text=f'{field}: {result}')
                return

        self.error_label.configure(text='')  # Clear error label

        action = DatabaseFunctions.add_contact(fname, lname, phonenumber, email)

        if action != True:
            self.error_label.configure(text=action)
        else:
            self.master.show_frame('Database')
            self.clear_entries()
    
    def clear_entries(self):
        self.fname_entry.delete(0, 'end')
        self.lname_entry.delete(0, 'end')
        self.phone_number_entry.delete(0, 'end')
        self.email_entry.delete(0, 'end')