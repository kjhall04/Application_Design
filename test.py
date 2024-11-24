from tkinter import Tk, Label
from PIL import Image, ImageTk

class TestApp(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x580")
        self.title("Image Test")

        image_path = "EquipmentManager\\background.jpg"
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)

        label = Label(self, image=photo)
        label.image = photo  # Prevent garbage collection
        label.pack(fill="both", expand=True)

app = TestApp()
app.mainloop()
