import customtkinter as ctk

# Initialize CustomTkinter and set appearance
ctk.set_appearance_mode("dark")  # Options: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("green")

class FrameManager(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Set window title and size
        self.title("Dynamic Multi-Page GUI")
        self.geometry("600x400")

        # Centering window on screen
        self.eval('tk::PlaceWindow . center')

        # Configure row and column for centering frames in the main window
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Dictionary to hold page frames
        self.frames = {}

        # Create different pages and add them to frames
        self.add_page(LoginPage, "Login")
        self.add_page(MenuPage, "Menu")
        self.add_page(Page1, "Page1")
        self.add_page(Page2, "Page2")

        # Display the initial page (Login)
        self.show_frame("Login")

    def add_page(self, page_class, name):
        """Add a page to the frame manager."""
        frame = page_class(self)
        self.frames[name] = frame
        frame.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, name):
        """Show a specific page frame."""
        frame = self.frames[name]
        frame.tkraise()

    def login_successful(self):
        """Handle login success by showing the menu page."""
        self.show_frame("Menu")

class LoginPage(ctk.CTkFrame):
    """Login page frame."""
    def __init__(self, parent):
        super().__init__(parent)

        # Placeholder login credentials
        self.username = "user"
        self.password = "pass"

        # Container frame to center widgets
        self.container = ctk.CTkFrame(self)
        self.container.pack(expand=True)  # Expand and center vertically and horizontally

        self.label = ctk.CTkLabel(self.container, text="Login Page", font=("Arial", 20))
        self.label.pack(pady=10)

        self.user_entry = ctk.CTkEntry(self.container, placeholder_text="Username")
        self.user_entry.pack(pady=5)

        self.pass_entry = ctk.CTkEntry(self.container, placeholder_text="Password", show="*")
        self.pass_entry.pack(pady=5)

        self.login_button = ctk.CTkButton(self.container, text="Login", command=self.check_login)
        self.login_button.pack(pady=10)

        self.error_label = ctk.CTkLabel(self.container, text="", text_color="red")
        self.error_label.pack(pady=5)

    def check_login(self):
        """Check login credentials."""
        username = self.user_entry.get()
        password = self.pass_entry.get()
        if username == self.username and password == self.password:
            self.error_label.configure(text="")
            self.master.login_successful()
        else:
            self.error_label.configure(text="Invalid username or password")

class MenuPage(ctk.CTkFrame):
    """Menu page frame shown after login."""
    def __init__(self, parent):
        super().__init__(parent)

        # Container frame to center widgets
        self.container = ctk.CTkFrame(self)
        self.container.pack(expand=True)

        self.label = ctk.CTkLabel(self.container, text="Menu Page", font=("Arial", 20))
        self.label.pack(pady=10)

        # Navigation buttons to other pages
        self.page1_button = ctk.CTkButton(self.container, text="Go to Page 1", command=lambda: parent.show_frame("Page1"))
        self.page1_button.pack(pady=5)

        self.page2_button = ctk.CTkButton(self.container, text="Go to Page 2", command=lambda: parent.show_frame("Page2"))
        self.page2_button.pack(pady=5)

        # Logout button to exit the program
        self.logout_button = ctk.CTkButton(self.container, text="Logout", command=self.quit)
        self.logout_button.pack(pady=10)

class Page1(ctk.CTkFrame):
    """Example page 1 frame."""
    def __init__(self, parent):
        super().__init__(parent)

        # Container frame to center widgets
        self.container = ctk.CTkFrame(self)
        self.container.pack(expand=True)

        self.label = ctk.CTkLabel(self.container, text="Page 1", font=("Arial", 20))
        self.label.pack(pady=10)

        # Back button to return to menu
        self.back_button = ctk.CTkButton(self.container, text="Back to Menu", command=lambda: parent.show_frame("Menu"))
        self.back_button.pack(pady=10)

class Page2(ctk.CTkFrame):
    """Example page 2 frame."""
    def __init__(self, parent):
        super().__init__(parent)

        # Container frame to center widgets
        self.container = ctk.CTkFrame(self)
        self.container.pack(expand=True)

        self.label = ctk.CTkLabel(self.container, text="Page 2", font=("Arial", 20))
        self.label.pack(pady=10)

        # Back button to return to menu
        self.back_button = ctk.CTkButton(self.container, text="Back to Menu", command=lambda: parent.show_frame("Menu"))
        self.back_button.pack(pady=10)

# Run the application
if __name__ == "__main__":
    app = FrameManager()
    app.mainloop()

