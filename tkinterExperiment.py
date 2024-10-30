import customtkinter as ctk

ctk.set_appearance_mode('Dark')
ctk.set_default_color_theme('green')

app = ctk.CTk()
app.geometry('400x240')

def button_function():
    print('button pressed')

button = ctk.CTkButton(master=app, text='Press', text_color='black', command=button_function)
button.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

app.mainloop()