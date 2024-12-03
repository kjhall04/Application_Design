import customtkinter as ctk
import ValidateEntry
import DatabaseFunctions

# Class for the add contact frame
class AddContact(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        # Create frame container
        self.container = ctk.CTkFrame(self)
        self.container.pack(expand=True, padx=20, pady=20)

        # Title labe
        self.label = ctk.CTkLabel(self.container, text='Add Contact', font=('Arial', 25))
        self.label.pack(padx=40, pady=10)

        # Entry box
        self.fname_entry = ctk.CTkEntry(self.container, placeholder_text='First Name')
        self.fname_entry.pack(pady=5)

        # Entry box
        self.lname_entry = ctk.CTkEntry(self.container, placeholder_text='Last Name')
        self.lname_entry.pack(pady=5)

        # Entry box
        self.phone_number_entry = ctk.CTkEntry(self.container, placeholder_text='Phone Number')
        self.phone_number_entry.pack(pady=5)

        # Entry box
        self.email_entry = ctk.CTkEntry(self.container, placeholder_text='Email')
        self.email_entry.pack(pady=5)

        # Button for adding that runs the validate function
        self.add_button = ctk.CTkButton(self.container, text='Add Contact', command=self.validate_info)
        self.add_button.pack(pady=5)

        # Label for error messages
        self.error_label = ctk.CTkLabel(self.container, text='', text_color='red')
        self.error_label.pack(padx=10)

        # Button to go back to the database screen and clear entries from this screen
        self.back_button = ctk.CTkButton(self.container, text='Back', fg_color='#243573', 
                                         command=lambda: (self.master.show_frame('Database'), self.clear_entries()))
        self.back_button.pack(pady=(5, 15))

    # Validate and add the data
    def validate_info(self):
        # Put all entries into seperate variables
        fname = self.fname_entry.get()
        lname = self.lname_entry.get()
        phonenumber = self.phone_number_entry.get()
        email = self.email_entry.get()

        # Run through all the validation and store the results
        validation_results = [
            ('First name', ValidateEntry.name(fname)),
            ('Last name', ValidateEntry.name(lname)),
            ('Phone Number', ValidateEntry.phone_number(phonenumber)),
            ('Email', ValidateEntry.email(email)),
        ]

        # If any return as none then there are empty boxes
        if not fname or not lname or not phonenumber or not email:
            self.error_label.configure(text='Enter info into all the boxes.')
            return

        # If there are any errors then show the error message
        for field, result in validation_results:
            if result is not True:
                self.error_label.configure(text=f'{field}: {result}')
                return

        # Clear error message
        self.error_label.configure(text='')

        # Add data to the database and assign the result to a variable
        action = DatabaseFunctions.add_contact(fname, lname, phonenumber, email)

        # If not True then there was an error and display it
        if action != True:
            self.error_label.configure(text=action)
        else:
            # Data was stored correctly so show database with the data refreshed
            # Clear entries of this page
            self.master.frames['Database'].refresh_data()
            self.master.show_frame('Database')
            self.clear_entries()
    
    def clear_entries(self):
        # Clear the entries and errors, and reset labels
        self.fname_entry.delete(0, 'end')
        self.lname_entry.delete(0, 'end')
        self.phone_number_entry.delete(0, 'end')
        self.email_entry.delete(0, 'end')

        self.fname_entry.configure(placeholder_text='First Name')
        self.lname_entry.configure(placeholder_text='Last Name')
        self.phone_number_entry.configure(placeholder_text='Phone Number')
        self.email_entry.configure(placeholder_text='Email')

        self.error_label.configure(text='')