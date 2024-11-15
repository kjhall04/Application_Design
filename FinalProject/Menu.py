import customtkinter
import DatabaseFunctions
import Validation

# Set the default appearnace of the GUI to dark mode and the colors to green
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('green')

# Class for managing all the frames
class FrameManager(customtkinter.CTk):
    def __init__(self, debug_mode=False):
        super().__init__()

        # Create widow and place it in the center (or close to) of the user screen
        self.title('Equipment Manager')
        self.geometry('600x400')
        self.eval('tk::PlaceWindow . center')

        # Configuration to center the frames inside of the window space
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Create a list of the frames and their names
        self.frames = {}

        # Adds all the frames 
        self.add_frame(LoginFrame, 'Login')
        self.add_frame(SignUpFrame, 'Sign Up')
        self.add_frame(MenuFrame, 'Menu')
        self.add_frame(LoadingFrame, 'Loading')

        # Function for knowing the boolean value to enter the debug mode or not
        # Debug menu is only accessable from running the menu module outside of the main module
        self.debug_mode = debug_mode

        # If debug_mode is True then create a drop down menu to pick from the different frames
        if self.debug_mode:
            self.frame_selector = customtkinter.CTkOptionMenu(
                self, 
                values=list(self.frames.keys()), 
                command=self.show_frame
            )
            # Place the selector to the side outside of the frames
            self.frame_selector.grid(row=0, column=1, padx=10, pady=10)

        # Show the first Login Frame
        self.show_frame('Login')

    # Add frames to the dictionary to call later
    def add_frame(self, page_class, name):
        frame = page_class(self)
        self.frames[name] = frame
        frame.grid(row=0, column=0, sticky='nsew')

    # Showing a frame from the dictionary
    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()

    # If process is succesful then show the loading frame
    def login_succesful(self):
        self.show_frame('Loading')
        self.frames['Loading'].animate_loading()

# Class for  the login Frame
class LoginFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Place the frame in the middle and let it expand to fit the widgets if needed
        self.container = customtkinter.CTkFrame(self)
        self.container.pack(expand=True)

        # Create the text at the top
        self.label = customtkinter.CTkLabel(self.container, text='Equipment Manager', font=('Arial', 25))
        self.label.pack(padx=20, pady=10)

        # Entry for the Username
        self.username_entry = customtkinter.CTkEntry(self.container, placeholder_text='Username')
        self.username_entry.pack(pady=5)

        # Entry for the password showing '*' in place of the entry
        self.password_entry = customtkinter.CTkEntry(self.container, placeholder_text='Password', show='*')
        self.password_entry.pack(pady=5)

        # Button for logging in
        self.login_button = customtkinter.CTkButton(self.container, text='Login', command=self.validate_entry)
        self.login_button.pack(pady=5)

        # Error label to show errors
        self.error_label = customtkinter.CTkLabel(self.container, text='', text_color='red')
        self.error_label.pack(padx=10)

        # Button for going to the sign up page
        # Run the show frame command to switch to sign up
        self.sign_up_button = customtkinter.CTkButton(self.container, text='Sign Up', command=lambda: self.master.show_frame('Sign Up'))
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
                return

        # If no match is found, display an error message
        self.error_label.configure(text='Invalid username or password', text_color='red')

# Class for the sign up frame
class SignUpFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Place the frame in the middle and let it expand to fit the widgets if needed
        self.container = customtkinter.CTkFrame(self)
        self.container.pack(expand=True)

        # Create the text at the top
        self.label = customtkinter.CTkLabel(self.container, text='Sign Up', font=('Arial', 25))
        self.label.pack(padx=40, pady=10)

        # Entry for the first name
        self.fname_entry = customtkinter.CTkEntry(self.container, placeholder_text='Enter your first name')
        self.fname_entry.pack(pady=5)

        # Entry for the last name
        self.lname_entry = customtkinter.CTkEntry(self.container, placeholder_text='Enter your last name')
        self.lname_entry.pack(pady=5)

        # Entry for the Username
        self.username_entry = customtkinter.CTkEntry(self.container, placeholder_text='Enter a Username')
        self.username_entry.pack(pady=5)

        # Entry for the Password
        self.password_entry = customtkinter.CTkEntry(self.container, placeholder_text='Enter a Password')
        self.password_entry.pack(pady=5)

        # Sign up button to add login info to the database
        # Run the validate info command
        self.sign_up_button = customtkinter.CTkButton(self.container, text='Sign Up', command=self.validate_info)
        self.sign_up_button.pack(pady=5)

        # Error label for showing entry errors
        self.error_label = customtkinter.CTkLabel(self.container, text='', text_color='red')
        self.error_label.pack(padx=10)

        # Button to go back to the login page
        # Run the show frame command for the login page
        self.go_back_button = customtkinter.CTkButton(self.container, text='Go Back', command=lambda: self.master.show_frame('Login'))
        self.go_back_button.pack(pady=(5, 15))

    # Function to validate the info
    def validate_info(self):
        # Store all the entries to seperate variables
        fname = self.fname_entry.get()
        lname = self.lname_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Run through the validation functions for the entries and store results in a list
        validation_results = [
            ('First name', Validation.name(fname)),
            ('Last name', Validation.name(lname)),
            ('Username', Validation.other_fields(username)),
            ('Password', Validation.other_fields(password)),
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
        DatabaseFunctions.add_login_entry(fname, lname, username, password)

        # Show the login frame
        self.master.show_frame('Login')

# Frame for the loading animation
class LoadingFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.container = customtkinter.CTkFrame(self)
        self.container.pack(expand=True)

        self.loading_label = customtkinter.CTkLabel(self.container, text='Loading Database...', font=('Arial', 15))
        self.loading_label.pack(padx=40, pady=10)

        self.progress = customtkinter.CTkProgressBar(self.container, orientation='horizontal', width=200)
        self.progress.pack(padx=10, pady=10)

    def animate_loading(self):
        self.progress.set(0)
        self.update_progress(0)

    def update_progress(self, progress):
        if progress < 1.0:
            progress += 0.04
            self.progress.set(progress)
            self.after(50, lambda:self.update_progress(progress))
        else:
            self.master.show_frame('Menu')

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

        self.add_record = customtkinter.CTkButton(self.container, text='Exit Program', command=self.quit)
        self.add_record.pack(pady=5)

if __name__ == '__main__':
    # Run the program in the debug mode
    app = FrameManager(debug_mode=True)    
    app.mainloop()