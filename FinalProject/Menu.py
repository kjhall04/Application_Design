import customtkinter
import DatabaseFunctions
import Validation

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('green')

class FrameManager(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title('Equipment Manager')
        self.geometry('600x400')
        self.eval('tk::PlaceWindow . center')

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frames = {}

        self.add_frame(LoginFrame, 'Login')
        self.add_frame(SignUpFrame, 'Sign Up')
        self.add_frame(MenuFrame, 'Menu')

        self.show_frame('Login')

    def add_frame(self, page_class, name):
        frame = page_class(self)
        self.frames[name] = frame
        frame.grid(row=0, column=0, sticky='nsew')

    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()

    def login_succesful(self):
        self.show_frame('Menu')

class LoginFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
 
        self.container = customtkinter.CTkFrame(self)
        self.container.pack(expand=True)

        self.label = customtkinter.CTkLabel(self.container, text='Equipment Logs', font=('Arial', 25))
        self.label.pack(padx=20, pady=10)

        self.username_entry = customtkinter.CTkEntry(self.container, placeholder_text='Username')
        self.username_entry.pack(pady=(10, 5))

        self.password_entry = customtkinter.CTkEntry(self.container, placeholder_text='Password', show='*')
        self.password_entry.pack(pady=5)

        self.login_button = customtkinter.CTkButton(self.container, text='Login', command=self.validate_entry)
        self.login_button.pack(pady=(5, 10))

        self.error_label = customtkinter.CTkLabel(self.container, text="", text_color="red")
        self.error_label.pack(padx=10)

        self.sign_up_button = customtkinter.CTkButton(self.container, text='Sign Up', command=lambda: self.master.show_frame('Sign Up'))
        self.sign_up_button.pack(pady=5)

    def validate_entry(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Retrieve login data from the database
        login_data = DatabaseFunctions.get_login_data()

        # Check if the username and password match any entry in the login data
        for db_username, db_password in login_data:
            if username == db_username and password == db_password:
                self.error_label.configure(text="Login successful!", text_color="green")
                self.master.login_succesful()  # Show the Menu frame
                return

        # If no match is found, display an error message
        self.error_label.configure(text="Invalid username or password", text_color="red")

class SignUpFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.container = customtkinter.CTkFrame(self)
        self.container.pack(expand=True)

        self.label = customtkinter.CTkLabel(self.container, text='Sign Up', font=('Arial', 25))
        self.label.pack(padx=40, pady=10)

        self.fname_entry = customtkinter.CTkEntry(self.container, placeholder_text='Enter your first name')
        self.fname_entry.pack(pady=5)

        self.lname_entry = customtkinter.CTkEntry(self.container, placeholder_text='Enter your last name')
        self.lname_entry.pack(pady=5)

        self.username_entry = customtkinter.CTkEntry(self.container, placeholder_text='Enter a Username')
        self.username_entry.pack(pady=5)

        self.password_entry = customtkinter.CTkEntry(self.container, placeholder_text='Enter a Password')
        self.password_entry.pack(pady=5)

        self.sign_up_button = customtkinter.CTkButton(self.container, text='Sign Up', command=self.validate_info)
        self.sign_up_button.pack(pady=5)

        self.error_label = customtkinter.CTkLabel(self.container, text="", text_color="red")
        self.error_label.pack(padx=10, pady=5)

        self.login_button = customtkinter.CTkButton(self.container, text='Go Back', command=lambda: self.master.show_frame('Login'))
        self.login_button.pack(pady=5)

    def validate_info(self):
        fname = self.fname_entry.get()
        lname = self.lname_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Validate each field and show appropriate error messages
        validation_results = [
            ("First name", Validation.name(fname)),
            ("Last name", Validation.name(lname)),
            ("Username", Validation.other_fields(username)),
            ("Password", Validation.other_fields(password)),
        ]

        if not fname or not lname or not username or not password:
            self.error_label.configure(text='Enter info into all the boxes.')
            return

        # Check for any validation errors
        for field, result in validation_results:
            if result is not True:
                # Display the first encountered error
                self.error_label.configure(text=f"{field}: {result}")
                return

        # If all validations pass, proceed to add data to the database
        self.error_label.configure(text="")  # Clear error label
        DatabaseFunctions.add_login_entry(fname, lname, username, password)

        self.error_label.configure(text="Sign-up successful!", text_color="green")
        self.master.show_frame('Login')

class MenuFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
 
        self.container = customtkinter.CTkFrame(self)
        self.container.pack(expand=True)

        self.label = customtkinter.CTkLabel(self.container, text='Menu', font=('Arial', 25))
        self.label.pack(padx=50, pady=10)

        self.add_record = customtkinter.CTkButton(self.container, text='Add Record')
        self.add_record.pack(pady=5)

        self.add_record = customtkinter.CTkButton(self.container, text='Delete Record')
        self.add_record.pack(pady=5)

        self.add_record = customtkinter.CTkButton(self.container, text='Create Report')
        self.add_record.pack(pady=5)

        self.add_record = customtkinter.CTkButton(self.container, text='Exit Program')
        self.add_record.pack(pady=5)