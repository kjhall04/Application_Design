import customtkinter as ctk

# Set the appearance of the app
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Set up the main window
        self.title("Custom Frame Colors and Sizes")
        self.geometry("600x400")

        # Create a parent frame
        self.parent_frame = ctk.CTkFrame(self)
        self.parent_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Add nested frames with customized colors and sizes
        self.frame1 = ctk.CTkFrame(self.parent_frame, 
                                   fg_color="lightblue", 
                                   border_width=2, 
                                   border_color="blue", 
                                   width=200, 
                                   height=150, 
                                   corner_radius=10)
        self.frame1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.frame2 = ctk.CTkFrame(self.parent_frame, 
                                   fg_color="lightgreen", 
                                   border_width=2, 
                                   border_color="green", 
                                   width=200, 
                                   height=150, 
                                   corner_radius=10)
        self.frame2.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.frame3 = ctk.CTkFrame(self.parent_frame, 
                                   fg_color="pink", 
                                   border_width=2, 
                                   border_color="red", 
                                   width=200, 
                                   height=150, 
                                   corner_radius=10)
        self.frame3.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.frame4 = ctk.CTkFrame(self.parent_frame, 
                                   fg_color="lightyellow", 
                                   border_width=2, 
                                   border_color="orange", 
                                   width=200, 
                                   height=150, 
                                   corner_radius=10)
        self.frame4.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        # Configure grid weights to allow resizing
        self.parent_frame.grid_rowconfigure((0, 1), weight=1)
        self.parent_frame.grid_columnconfigure((0, 1), weight=1)

        # Add content to the frames
        self.populate_frames()

    def populate_frames(self):
        # Add labels to each frame
        label1 = ctk.CTkLabel(self.frame1, text="Frame 1", font=("Arial", 14))
        label1.pack(pady=20)

        label2 = ctk.CTkLabel(self.frame2, text="Frame 2", font=("Arial", 14))
        label2.pack(pady=20)

        label3 = ctk.CTkLabel(self.frame3, text="Frame 3", font=("Arial", 14))
        label3.pack(pady=20)

        label4 = ctk.CTkLabel(self.frame4, text="Frame 4", font=("Arial", 14))
        label4.pack(pady=20)


if __name__ == "__main__":
    app = App()
    app.mainloop()
