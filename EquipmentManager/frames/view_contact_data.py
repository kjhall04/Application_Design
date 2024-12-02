import customtkinter as ctk
import DatabaseFunctions

class ViewContactData(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.container = ctk.CTkFrame(self)
        self.container.pack(expand=True, padx=20, pady=20)

        self.label = ctk.CTkLabel(self.container, text='Contact Details', font=('Arial', 20))
        self.label.pack(padx=20, pady=10)

        # Create a frame for the details grid
        self.details_frame = ctk.CTkFrame(self.container)
        self.details_frame.pack(padx=20, pady=10)

        self.delete_button = ctk.CTkButton(self.container, text='Delete Entry', command=lambda: self.delete_entry())
        self.delete_button.pack(pady=(10, 5))

        self.back_button = ctk.CTkButton(self.container, text='Back', fg_color='#243573', command=lambda: self.master.show_frame('Database'))
        self.back_button.pack(pady=(5, 10))

    def show_data(self, fname, lname, phone, email):
        self.fname = fname
        self.lname = lname
        self.phone = phone
        self.email = email

        # Clear the grid to avoid overlapping data
        for widget in self.details_frame.winfo_children():
            widget.destroy()

        # Create a grid layout for details
        data_labels = ['First Name', 'Last Name', 'Phone', 'Email']
        data_values = [fname, lname, phone, email]

        for i, (label, value) in enumerate(zip(data_labels, data_values)):
            label_widget = ctk.CTkLabel(self.details_frame, text=f'{label}:', font=('Arial', 15), anchor='e')
            label_widget.grid(row=i, column=0, sticky='e', padx=10, pady=5)

            value_widget = ctk.CTkLabel(self.details_frame, text=value, font=('Arial', 15), anchor='w')
            value_widget.grid(row=i, column=1, sticky='w', padx=10, pady=5)

    def delete_entry(self):
        if hasattr(self, 'fname') and hasattr(self, 'lname') and hasattr(self, 'phone') and hasattr(self, 'email'):
            DatabaseFunctions.delete_contact_and_equipment(self.fname, self.lname, self.phone, self.email)
            self.master.frames['Database'].refresh_data(fetch_fresh=True)
            self.master.show_frame('Database')