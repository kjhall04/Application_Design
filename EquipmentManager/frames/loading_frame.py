import customtkinter as ctk

# Frame for the loading animation
class LoadingFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Place the frame in the middle and let it expand to fit the widgets if needed
        self.container = ctk.CTkFrame(self)
        self.container.pack(expand=True)

        # Create title label
        self.loading_label = ctk.CTkLabel(self.container, text='Loading Database...', font=('Arial', 15))
        self.loading_label.pack(padx=40, pady=10)

        # Create the progress bar
        self.progress = ctk.CTkProgressBar(self.container, orientation='horizontal', width=200)
        self.progress.pack(padx=10, pady=10)

    # Initiate animating the loading
    def animate_loading(self):
        self.progress.set(0)
        self.update_progress(0)

    # Fill in the loading bar and show the database frame when completed
    def update_progress(self, progress):
        if progress < 1.0:
            progress += 0.04
            self.progress.set(progress)
            self.after(50, lambda:self.update_progress(progress))
        else:
            self.master.show_frame('Database')