import customtkinter

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('green')

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

class LoginFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
 
        self.container = customtkinter.CTkFrame(self)
        self.container.pack(expand=True)

        self.label = customtkinter.CTkLabel(self.container, text='Login Page', font=('Arial', 25))
        self.label.pack(padx=20, pady=10)

        self.username_entry = customtkinter.CTkEntry(self.container, placeholder_text='Username')
        self.username_entry.pack(pady=(10, 5))

        self.password_entry = customtkinter.CTkEntry(self.container, placeholder_text='Password', show='*')
        self.password_entry.pack(pady=(5, 10))

        self.login_button = customtkinter.CTkButton(self.container, text='Login', command=self.validate_entry())
        self.login_button.pack(pady=10)

        self.sign_up_button = customtkinter.CTkButton(self.container, text='Sign Up', command=self.sign_up())
    
    def validate_entry():
        pass

    def sign_up():
        pass

class SignUpFrame(customtkinter.CTkFrame):
    def __init__(self,master):
        super().__init__(master)

        self.container = customtkinter.CTkFrame(self)
        self.container.pack(expand=True)

        self.label = customtkinter.CTkLabel(self.container, text='Sign Up', font=('Arial', 25))
        self.label.pack(padx=40, pady=10)

        self.username_entry = customtkinter.CTkEntry(self.container, placeholder_text='Username')
        self.username_entry.pack(pady=(10, 5))

        self.password_entry = customtkinter.CTkEntry(self.container, placeholder_text='Password')
        self.password_entry.pack(pady=5)

        self.login_button = customtkinter.CTkButton(self.container, text='Sign Up')
        self.login_button.pack(pady=(5, 10))

        self.login_button = customtkinter.CTkButton(self.container, text='Go Back')
        self.login_button.pack(pady=10)
        
class Login(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title('Equipment Manager')
        self.geometry('600x400')
        self.eval('tk::PlaceWindow . center')

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.login_frame = SignUpFrame(self)
        self.login_frame.grid(row=0, column=0, padx=10, pady=10)

app = Login()
app.mainloop()