import customtkinter as ctk
from PIL import Image
import os

# Test minimal setup
app = ctk.CTk()

current_path = os.path.dirname(os.path.realpath(__file__))
image_path = os.path.join(current_path, "Wallpaper.jpg")
bg_image = ctk.CTkImage(Image.open(image_path), size=(1000, 580))

bg_image_label = ctk.CTkLabel(app, image=bg_image)
bg_image_label.grid(row=0, column=0, sticky='nsew')
bg_image_label.lower()

app.geometry('1000x580')
app.mainloop()
