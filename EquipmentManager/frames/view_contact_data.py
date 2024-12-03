import customtkinter as ctk
import DatabaseFunctions

# Class for the contact data frame
class ViewContactData(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Frame to put the widgets in
        self.container = ctk.CTkFrame(self)
        self.container.pack(expand=True, padx=20, pady=20)

        # Title label
        self.label = ctk.CTkLabel(self.container, text='Contact Details', font=('Arial', 20))
        self.label.pack(padx=20, pady=10)

        # Create a frame for the details grid
        self.details_frame = ctk.CTkFrame(self.container)
        self.details_frame.pack(padx=20, pady=10)

        # Button to delete the shown entry
        self.delete_button = ctk.CTkButton(self.container, text='Delete Entry', command=lambda: self.delete_entry())
        self.delete_button.pack(pady=(10, 5))

        # Button to go back to the previous page
        self.back_button = ctk.CTkButton(self.container, text='Back', fg_color='#243573', 
                                         command=lambda: (self.master.show_frame('Database'), self.master.frames['Database'].refresh_data(fetch_fresh=True)))
        self.back_button.pack(pady=(5, 10))

    # Function to show the data
    def show_data(self, fname, lname, phone, email):
        # Assign the data to variables
        self.fname = fname
        self.lname = lname
        self.phone = phone
        self.email = email

        # Clear the grid to avoid overlapping data
        for widget in self.details_frame.winfo_children():
            widget.destroy()

        # Assign the data to lists to iterate over
        data_labels = ['First Name', 'Last Name', 'Phone', 'Email']
        data_values = [fname, lname, phone, email]

        # Creates a tuple to iterate over
        for i, (label, value) in enumerate(zip(data_labels, data_values)):
            # Data type is shown
            label_widget = ctk.CTkLabel(self.details_frame, text=f'{label}:', font=('Arial', 15), anchor='e')
            label_widget.grid(row=i, column=0, sticky='e', padx=10, pady=5)

            # Value is shown
            value_widget = ctk.CTkLabel(self.details_frame, text=value, font=('Arial', 15), anchor='w')
            value_widget.grid(row=i, column=1, sticky='w', padx=10, pady=5)

            # Assigned to react to the cursor
            value_widget._label.configure(cursor='hand2')

            # Given the commands when it is hovered over and clicked
            value_widget.bind('<Enter>', lambda e, label=value_widget: self.on_hover(e, label))
            value_widget.bind('<Leave>', lambda e, label=value_widget: self.on_leave(e, label))
            value_widget.bind('<Button-1>', lambda e, label_text=label, value=value: self.on_value_click(e, label_text, value))

    # Delete the entry
    def delete_entry(self):
        # If all attributes are there then delete entry and go back to the database
        if hasattr(self, 'fname') and hasattr(self, 'lname') and hasattr(self, 'phone') and hasattr(self, 'email'):
            DatabaseFunctions.delete_contact_and_equipment(self.fname, self.lname, self.phone, self.email)
            self.master.frames['Database'].refresh_data(fetch_fresh=True)
            self.master.show_frame('Database')

    # Funciton to change color of label when hovered over
    def on_hover(self, event, label):
        label.configure(text_color='gray')

    # Default label color
    def on_leave(self, event, label):
        label.configure(text_color='white')

    # When a value is clicked go to the editing frame
    def on_value_click(self, event, label_text, value):
        # Show a new frame for editing the value
        self.master.frames['EditC'].show_data(label_text, value, self.fname, self.lname, self.phone, self.email)
        self.master.show_frame('EditC')