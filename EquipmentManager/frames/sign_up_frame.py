import customtkinter as ctk
import DatabaseFunctions
import ValidateEntry

# Class for the sign up frame
class SignUpFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Place the frame in the middle and let it expand to fit the widgets if needed
        self.container = ctk.CTkFrame(self)
        self.container.pack(expand=True)

        # Create the text at the top
        self.label = ctk.CTkLabel(self.container, text='Sign Up', font=('Arial', 25))
        self.label.pack(padx=40, pady=10)

        # Entry for the first name
        self.fname_entry = ctk.CTkEntry(self.container, placeholder_text='First Name')
        self.fname_entry.pack(pady=5)

        # Entry for the last name
        self.lname_entry = ctk.CTkEntry(self.container, placeholder_text='Last Name')
        self.lname_entry.pack(pady=5)

        # Entry for the Username
        self.username_entry = ctk.CTkEntry(self.container, placeholder_text='Username')
        self.username_entry.pack(pady=5)

        # Entry for the Password
        self.password_entry = ctk.CTkEntry(self.container, placeholder_text='Password')
        self.password_entry.pack(pady=5)

        # Sign up button to add login info to the database
        # Run the validate info command
        self.sign_up_button = ctk.CTkButton(self.container, text='Sign Up', command=self.validate_info)
        self.sign_up_button.pack(pady=5)

        # Error label for showing entry errors
        self.error_label = ctk.CTkLabel(self.container, text='', text_color='red')
        self.error_label.pack(padx=10)

        # Button to go back to the login page
        # Run the show frame command for the login page
        self.back_button = ctk.CTkButton(self.container, text='Back', fg_color='#243573', command=lambda: (self.master.show_frame('Login'), self.clear_entries()))
        self.back_button.pack(pady=(5, 15))

    # Function to validate the info
    def validate_info(self):
        # Store all the entries to seperate variables
        fname = self.fname_entry.get()
        lname = self.lname_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Run through the validation functions for the entries and store results in a list
        validation_results = [
            ('First name', ValidateEntry.name(fname)),
            ('Last name', ValidateEntry.name(lname)),
            ('Username', ValidateEntry.other_fields(username)),
            ('Password', ValidateEntry.password(password)),
        ]

        # If any entry is empty then display the appropriate error
        if not fname or not lname or not username or not password:
            self.error_label.configure(text='Enter info into all the boxes.')
            return

        # If any validation returns false then show the appropriate error label
        for field, result in validation_results:
            if result is not True:
                # Display the first encountered error
                self.error_label.configure(text=f'{field}: {result}')
                return

        # If all validations pass, proceed to add data to the database
        self.error_label.configure(text='')  # Clear error label

        action = DatabaseFunctions.add_login(fname, lname, username, password)

        if action != True:
            self.error_label.configure(text=action)
        else:
            self.master.show_frame('Login')
            self.clear_entries()
    
    def clear_entries(self):
        self.fname_entry.delete(0, 'end')
        self.lname_entry.delete(0, 'end')
        self.username_entry.delete(0, 'end')
        self.password_entry.delete(0, 'end')
