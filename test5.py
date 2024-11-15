import customtkinter as ctk
import time

# Initialize customtkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Define the main application
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Set up window
        self.title("GUI with Loading Screen")
        self.geometry("400x300")
        
        # Frames for Main Screens and Loading Screen
        self.main_frame1 = ctk.CTkFrame(self)
        self.main_frame2 = ctk.CTkFrame(self)
        self.loading_screen = ctk.CTkFrame(self)
        
        # MainFrame1 - first usable GUI part
        self.main_frame1.pack(fill="both", expand=True)
        self.label1 = ctk.CTkLabel(self.main_frame1, text="Main Screen 1")
        self.label1.pack(pady=20)
        self.start_button = ctk.CTkButton(self.main_frame1, text="Start", command=self.show_loading_screen)
        self.start_button.pack(pady=10)
        
        # MainFrame2 - second usable GUI part
        self.label2 = ctk.CTkLabel(self.main_frame2, text="Main Screen 2")
        self.label2.pack(pady=20)
        self.back_button = ctk.CTkButton(self.main_frame2, text="Go Back", command=self.show_main_frame1)
        self.back_button.pack(pady=10)
        
        # Loading Screen with fake animation
        self.loading_label = ctk.CTkLabel(self.loading_screen, text="Loading...")
        self.loading_label.pack(pady=20)
        self.progress = ctk.CTkProgressBar(self.loading_screen, orientation="horizontal", width=200)
        self.progress.pack(pady=10)
        self.progress.set(0)
        
    def show_main_frame1(self):
        # Switch to Main Frame 1
        self.main_frame2.pack_forget()
        self.main_frame1.pack(fill="both", expand=True)
        
    def show_main_frame2(self):
        # Switch to Main Frame 2
        self.loading_screen.pack_forget()
        self.main_frame2.pack(fill="both", expand=True)
        
    def show_loading_screen(self):
        # Display Loading Screen and animate progress
        self.main_frame1.pack_forget()
        self.loading_screen.pack(fill="both", expand=True)
        
        # Animate loading bar
        self.animate_loading()
        
    def animate_loading(self):
        progress = 0
        for _ in range(20):  # Update progress bar 20 times
            progress += 0.05
            self.progress.set(progress)
            self.update_idletasks()
            time.sleep(0.05)  # Adjust speed as needed
        self.after(500, self.show_main_frame2)  # Transition to MainFrame2 after a short delay


if __name__ == "__main__":
    app = App()
    app.mainloop()
