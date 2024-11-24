import customtkinter as ctk

# Initialize the application
app = ctk.CTk()

# Set the window size and title
app.geometry("400x200")
app.title("Interactive Label Example")

# Define functions for hover effects
def on_hover(event):
    clickable_label.configure(text_color="gray")  # Change color to gray on hover

def on_leave(event):
    clickable_label.configure(text_color="blue")  # Reset color when the cursor leaves

def on_label_click(event):
    print("Label clicked!")

# Create a clickable label
clickable_label = ctk.CTkLabel(app, text="Click me!", text_color="blue", cursor="hand2")
clickable_label.pack(pady=20)

# Bind hover and click events
clickable_label.bind("<Enter>", on_hover)  # When cursor enters
clickable_label.bind("<Leave>", on_leave)  # When cursor leaves
clickable_label.bind("<Button-1>", on_label_click)  # When clicked

# Run the application
app.mainloop()
