import customtkinter as ctk
import DatabaseFunctions
import ValidateEntry

# Set the default appearnace of the GUI to dark mode and the colors to green
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

# Class for managing all the frames
class FrameManager(ctk.CTk):
    def __init__(self, debug_mode=False):
        super().__init__()
        self.title('Equipment Manager')
        self.geometry('1000x580')

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Create a list of the frames and their names
        self.frames = {}

        # Add all the frames
        self.add_frame(LoginFrame, 'Login')
        self.add_frame(SignUpFrame, 'Sign Up')
        self.add_frame(LoadingFrame, 'Loading')
        self.add_frame(DatabaseFrame, 'Database')
        self.add_frame(ViewContactData, 'CData')
        self.add_frame(ViewEquipmentData, 'EData')
        self.add_frame(AddContact, 'AddC')
        self.add_frame(AddEquipment, 'AddE')

        # Debug mode
        self.debug_mode = debug_mode
        if self.debug_mode:
            self.frame_selector = ctk.CTkOptionMenu(
                self,
                values=list(self.frames.keys()),
                command=self.show_frame,
            )
            self.frame_selector.grid(row=0, column=1, padx=10, pady=10, sticky='e')

        # Show the first frame
        self.show_frame('Login')

    def add_frame(self, page_class, name):
        self.frames[name] = page_class(self)
        self.frames[name].grid(row=0, column=0, sticky='nsew')

    def show_frame(self, name):
        self.frames[name].tkraise()

    def login_succesful(self):
        self.show_frame('Loading')
        self.frames['Loading'].animate_loading()

# Class for  the login Frame
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
        self.login_button = ctk.CTkButton(self.container, text='Login', command=self.validate_entry)
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
        self.fname_entry = ctk.CTkEntry(self.container, placeholder_text='Enter your first name')
        self.fname_entry.pack(pady=5)

        # Entry for the last name
        self.lname_entry = ctk.CTkEntry(self.container, placeholder_text='Enter your last name')
        self.lname_entry.pack(pady=5)

        # Entry for the Username
        self.username_entry = ctk.CTkEntry(self.container, placeholder_text='Enter a Username')
        self.username_entry.pack(pady=5)

        # Entry for the Password
        self.password_entry = ctk.CTkEntry(self.container, placeholder_text='Enter a Password')
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
        self.back_button = ctk.CTkButton(self.container, text='Back', fg_color='#243573', command=lambda: self.master.show_frame('Login'))
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
            # Show the login frame
            self.master.show_frame('Login')
        

# Frame for the loading animation
class LoadingFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.container = ctk.CTkFrame(self)
        self.container.pack(expand=True)

        self.loading_label = ctk.CTkLabel(self.container, text='Loading Database...', font=('Arial', 15))
        self.loading_label.pack(padx=40, pady=10)

        self.progress = ctk.CTkProgressBar(self.container, orientation='horizontal', width=200)
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
            self.master.show_frame('Database')
            pass

class DatabaseFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.container = ctk.CTkFrame(self)
        self.container.pack(expand=True, padx=20, pady=20)

        self.container.grid_rowconfigure((0, 1), weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.label = ctk.CTkLabel(self.container, text='Database', font=('Arial', 25))
        self.label.grid(row=0, columnspan=2, padx=10, pady=(20, 10), sticky='n')

        self.database = ctk.CTkScrollableFrame(self.container, width=260)
        self.database.grid(row=1, columnspan=2, padx=20, pady=(0, 20), sticky='nsew')

        self.database.grid_columnconfigure(0, weight=1)

        self.add_contact_button = ctk.CTkButton(self.container, text='Add Contact')
        self.add_contact_button.grid(row=2, column=0, padx=(15, 5), pady=5)

        self.add_equipment_button = ctk.CTkButton(self.container, text='Add Equipment')
        self.add_equipment_button.grid(row=2, column=1, padx=(0, 15), pady=5)

        self.create_report_button = ctk.CTkButton(self.container, text='Create Report')
        self.create_report_button.grid(row=3, columnspan=2, padx=15, pady=5)

        self.exit_button = ctk.CTkButton(self.container, text='Exit Program', fg_color='#243573', command=self.master.quit)
        self.exit_button.grid(row=4, columnspan=2, padx=15, pady=(5, 10))

        self.row_counter = 0

        data_list = DatabaseFunctions.get_all_data_for_menu()

        grouped_data = {}
        for entry in data_list:
            full_name = f"{entry['Fname']} {entry['Lname']}"
            if full_name not in grouped_data:
                grouped_data[full_name] = []
            grouped_data[full_name].append({'Ename': entry['Ename'], 'Department': entry['Department']})

        for name, equipment_list in grouped_data.items():
            name_label = ctk.CTkLabel(
                self.database, 
                text=name, 
                font=('Arial', 15), 
                anchor='center'
            )
            name_label.grid(row=self.row_counter, column=0, padx=10, pady=5, sticky= 'w')
            self.row_counter += 1

            name_label._label.configure(cursor='hand2')

            name_label.bind('<Enter>', lambda e, label=name_label: self.on_hover(e, label))
            name_label.bind('<Leave>', lambda e, label=name_label: self.on_leave(e, label))  # When cursor leaves
            name_label.bind('<Button-1>', lambda e, name=name: self.on_name_click(e, name))

            for equipment in equipment_list:
                equipment_label = ctk.CTkLabel(
                    self.database,
                    text=f"{equipment['Ename']} ({equipment['Department']})",
                    font=('Arial', 14),
                    anchor='w'
                )
                equipment_label.grid(row=self.row_counter-1, column=1, padx=10, pady=5, sticky= 'w')
                self.row_counter += 1

                equipment_label._label.configure(cursor='hand2')

                equipment_label.bind('<Enter>', lambda e, label=equipment_label: self.on_hover(e, label))
                equipment_label.bind('<Leave>', lambda e, label=equipment_label: self.on_leave(e, label))  # When cursor leaves
                equipment_label.bind('<Button-1>', lambda e, eq=equipment: self.on_eq_click(e, eq))

    def on_hover(self, event, label):
        label.configure(text_color='gray')

    def on_leave(self, event, label):
        label.configure(text_color='white')

    def on_name_click(self, event, name):
        contact_data = DatabaseFunctions.get_contact_data()
        for fname, lname, phone, email in contact_data:
            full_name = f"{fname} {lname}"
            if full_name == name:
                # Display contact details
                self.master.frames['CData'].show_data(fname, lname, phone, email)
                self.master.show_frame('CData')
                break

    def on_eq_click(self, event, equipment):
        equipment_data = DatabaseFunctions.get_equipment_data()
        for contact_id, ename, date_installed, decomissioned, decomissioned_date, equipment_age, maintenance_date, department in equipment_data:
            e_data = {'Ename': ename, 'Department': department}
            if e_data == equipment:
                self.master.frames['EData'].show_data(contact_id, ename, date_installed, decomissioned, decomissioned_date,
                                                      equipment_age, maintenance_date, department)
                self.master.show_frame('EData')
                break

class ViewContactData(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.container = ctk.CTkFrame(self)
        self.container.pack(expand=True, padx=20, pady=20)

        self.label = ctk.CTkLabel(self.container, text='Contact Details', font=('Arial', 20))
        self.label.pack(padx=20, pady=10)

        self.details_label = ctk.CTkLabel(self.container, text='', font=('Arial', 15))
        self.details_label.pack(padx=20, pady=10)

        self.delete_button = ctk.CTkButton(self.container, text='Delete Entry')
        self.delete_button.pack(pady=(10, 5))

        self.back_button = ctk.CTkButton(self.container, text='Back', fg_color='#243573', command=lambda: self.master.show_frame('Database'))
        self.back_button.pack(pady=(5, 10))

    def show_data(self, fname, lname, phone, email):
        details = f'First Name: {fname}\nLast Name: {lname}\nPhone: {phone}\nEmail: {email}'
        self.details_label.configure(text=details)

class ViewEquipmentData(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.container = ctk.CTkFrame(self)
        self.container.pack(expand=True, padx=20, pady=20)

        self.label = ctk.CTkLabel(self.container, text='Equipment Details', font=('Arial', 20))
        self.label.pack(padx=20, pady=10)

        self.details_label = ctk.CTkLabel(self.container, text='', font=('Arial', 15))
        self.details_label.pack(padx=20, pady=10)

        self.delete_button = ctk.CTkButton(self.container, text='Delete Entry')
        self.delete_button.pack(pady=(10, 5))

        self.back_button = ctk.CTkButton(self.container, text='Back', fg_color='#243573', command=lambda: self.master.show_frame('Database'))
        self.back_button.pack(pady=(5, 10))

    def show_data(self, contact_id, ename, date_installed, decomissioned, decomissioned_date, equipment_age, maintenance_date, department):
        details = f'Equipment: {ename}\nDepartment: {department}\nDate Installed: {date_installed}\nEquipment Age: {equipment_age}\nMaintenance Date: {maintenance_date}\nDecomissioned: {decomissioned}\nDecomissioned Date: {decomissioned_date}'
        self.details_label.configure(text=details)

class AddContact(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.container = ctk.CTkFrame(self)
        self.container.pack(expand=True, padx=20, pady=20)

class AddEquipment(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.container = ctk.CTkFrame(self)
        self.container.pack(expand=True, padx=20, pady=20)

if __name__ == '__main__':
    # Run the program in the debug mode
    app = FrameManager(debug_mode=True)
    app.mainloop()