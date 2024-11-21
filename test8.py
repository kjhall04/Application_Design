import customtkinter as ctk

# Set the appearance of the app
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Set up the main window
        self.title("Multiple Frames Example")
        self.geometry("600x400")

        # Create a parent frame to hold multiple child frames
        self.parent_frame = ctk.CTkFrame(self)
        self.parent_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Add multiple child frames
        self.frame1 = ctk.CTkFrame(self.parent_frame, corner_radius=10, border_width=2, border_color="blue")
        self.frame1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.frame2 = ctk.CTkFrame(self.parent_frame, corner_radius=10, border_width=2, border_color="green")
        self.frame2.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.frame3 = ctk.CTkFrame(self.parent_frame, corner_radius=10, border_width=2, border_color="red")
        self.frame3.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.frame4 = ctk.CTkFrame(self.parent_frame, corner_radius=10, border_width=2, border_color="orange")
        self.frame4.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        # Configure parent frame grid weights
        self.parent_frame.grid_rowconfigure((0, 1), weight=1)
        self.parent_frame.grid_columnconfigure((0, 1), weight=1)

        # Add widgets to child frames
        self.populate_frames()

    def populate_frames(self):
        # Frame 1 content
        label1 = ctk.CTkLabel(self.frame1, text="Frame 1", font=("Arial", 16))
        label1.pack(padx=10, pady=10)

        # Frame 2 content
        label2 = ctk.CTkLabel(self.frame2, text="Frame 2", font=("Arial", 16))
        label2.pack(padx=10, pady=10)

        # Frame 3 content
        label3 = ctk.CTkLabel(self.frame3, text="Frame 3", font=("Arial", 16))
        label3.pack(padx=10, pady=10)

        # Frame 4 content
        label4 = ctk.CTkLabel(self.frame4, text="Frame 4", font=("Arial", 16))
        label4.pack(padx=10, pady=10)


if __name__ == "__main__":
    app = App()
    app.mainloop()
