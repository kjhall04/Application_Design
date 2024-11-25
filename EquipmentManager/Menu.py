import customtkinter as ctk
from PIL import Image  # Required for handling images
from frames import *

# Set the default appearance of the GUI to dark mode and the colors to dark-blue
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

class FrameManager(ctk.CTk):
    def __init__(self, debug_mode=False):
        super().__init__()
        
        self.title('Equipment Manager')
        self.geometry('1000x580')

        # Add background image
        self.background_image = ctk.CTkImage(Image.open("EquipmentManager\\background.png"), size=(1000, 580))
        self.background_label = ctk.CTkLabel(self, image=self.background_image, text="")
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.background_label.lower() 

        # Configure layout grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Create a dictionary for frames
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
        # Add frames and set transparency
        frame = page_class(self)
        frame.configure(fg_color="transparent")  # Ensure frames allow background to show
        self.frames[name] = frame
        frame.grid(row=0, column=0, sticky='nsew')

    def show_frame(self, name):
        # Raise the selected frame to the top
        self.frames[name].tkraise()

    def login_succesful(self):
        self.show_frame('Loading')
        self.frames['Loading'].animate_loading()

if __name__ == '__main__':
    app = FrameManager(debug_mode=True)
    app.mainloop()
