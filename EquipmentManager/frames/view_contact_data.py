import customtkinter as ctk

class ViewContactData(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.container = ctk.CTkFrame(self)
        self.container.pack(expand=True, padx=20, pady=20)

        self.label = ctk.CTkLabel(self.container, text='Contact Details', font=('Arial', 20))
        self.label.pack(padx=20, pady=10)
        
        self.details_label = ctk.CTkLabel(self.container, text='', font=('Arial', 15))
        self.details_label.pack(padx=20, pady=10)

        self.delete_button = ctk.CTkButton(self.container, text='Delete Entry')
        self.delete_button.pack(pady=(10, 5))

        self.back_button = ctk.CTkButton(self.container, text='Back', fg_color='#243573', command=lambda: self.master.show_frame('Database'))
        self.back_button.pack(pady=(5, 10))

    def show_data(self, fname, lname, phone, email):
        details = f'First Name: {fname}\nLast Name: {lname}\nPhone: {phone}\nEmail: {email}'
        self.details_label.configure(text=details)