import customtkinter as ctk
import DatabaseFunctions

# Class for the login Frame
class LoginFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Place the frame in the middle and let it expand to fit the widgets if needed
        self.container = ctk.CTkFrame(self)
        self.container.pack(expand=True)

        # Create the text at the top
        self.label = ctk.CTkLabel(self.container, text='Equipment Manager', font=('Arial', 25))
        self.label.pack(padx=20, pady=10)

        # Entry for the Username
        self.username_entry = ctk.CTkEntry(self.container, placeholder_text='Username')
        self.username_entry.pack(pady=5)

        # Entry for the password showing '*' in place of the entry
        self.password_entry = ctk.CTkEntry(self.container, placeholder_text='Password', show='*')
        self.password_entry.pack(pady=5)

        # Button for logging in
        self.login_button = ctk.CTkButton(self.container, text='Login', fg_color='#243573', command=self.validate_entry)
        self.login_button.pack(pady=5)

        # Error label to show errors
        self.error_label = ctk.CTkLabel(self.container, text='', text_color='red')
        self.error_label.pack(padx=10)

        # Button for going to the sign up page
        # Run the show frame command to switch to sign up
        self.sign_up_button = ctk.CTkButton(self.container, text='Sign Up', command=lambda: self.master.show_frame('Sign Up'))
        self.sign_up_button.pack(pady=(5, 15))

    # function for validating user entries to login
    def validate_entry(self):
        # Store entries in seperate variables
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Retrieve login data from the database
        login_data = DatabaseFunctions.get_login_data()

        # Check if the username and password match any entry in the login data
        for db_username, db_password in login_data:
            if username == db_username and password == db_password:
                # If succesful run the login succesful function from the master class
                self.master.login_succesful()

        # If no match is found, display an error message
        self.error_label.configure(text='Invalid username or password', text_color='red')

    # Clear all the entries and errors when return to the page
    def clear_entries(self):
        self.username_entry.delete(0, 'end')
        self.password_entry.delete(0, 'end')

        self.username_entry.configure(placeholder_text='Username')
        self.password_entry.configure(placeholder_text='Password', show='*')

        self.error_label.configure(text='')