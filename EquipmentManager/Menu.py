import customtkinter as ctk
from Frames import *

# Set the default appearance of the GUI to dark mode and the colors to dark-blue
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

# Class to run all frames through
class FrameManager(ctk.CTk):
    def __init__(self, debug_mode=False):
        super().__init__()
        
        # Program title and screen size
        self.title('Equipment Manager')
        self.geometry('1000x580')

        # Configure layout grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Create a dictionary for frames
        self.frames = {}

        # Add all the frames by class and name for reference
        self.add_frame(LoginFrame, 'Login')
        self.add_frame(SignUpFrame, 'Sign Up')
        self.add_frame(LoadingFrame, 'Loading')
        self.add_frame(DatabaseFrame, 'Database')
        self.add_frame(ViewContactData, 'CData')
        self.add_frame(ViewEquipmentData, 'EData')
        self.add_frame(AddContact, 'AddC')
        self.add_frame(AddEquipment, 'AddE')
        self.add_frame(EditContactData, 'EditC')
        self.add_frame(EditEquipmentData, 'EditE')

        # Debug mode that creates a dropdown to the side of all the different
        # frames to iterate through without running the program properly
        self.debug_mode = debug_mode
        if self.debug_mode:
            self.frame_selector = ctk.CTkOptionMenu(
                self,
                values=list(self.frames.keys()),
                command=self.show_frame,
            )
            self.frame_selector.grid(row=0, column=1, padx=10, pady=10, sticky='e')

        # Show the first frame 'Login'
        self.show_frame('Login')

    def add_frame(self, page_class, name):
        # Add frames to dictionary and pass class and name and position when displayed
        frame = page_class(self)
        self.frames[name] = frame
        frame.grid(row=0, column=0, sticky='nsew')

    def show_frame(self, name):
        # Show the frame listed
        frame = self.frames[name]
        frame.tkraise()

    def login_succesful(self):
        # When login is sucessful pull up the loading screen and animate it
        self.show_frame('Loading')
        self.frames['Loading'].animate_loading()

# If main then run with debugger
if __name__ == '__main__':
    app = FrameManager(debug_mode=True)
    app.mainloop()