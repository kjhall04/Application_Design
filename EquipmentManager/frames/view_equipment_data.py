import customtkinter as ctk
import DatabaseFunctions

# Class for the equipment data frame
class ViewEquipmentData(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Frame to put the widgets in
        self.container = ctk.CTkFrame(self)
        self.container.pack(expand=True, padx=20, pady=20)

        # Title label
        self.label = ctk.CTkLabel(self.container, text='Equipment Details', font=('Arial', 20))
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
    def show_data(self, contact_id, ename, department, date_installed, maintenance_date, decomissioned, decomissioned_date):
        # Assign the data to variables
        self.contact_id = contact_id
        self.ename = ename
        self.department = department
        self.date_installed = date_installed
        self.maintenance_date = maintenance_date
        self.decomissioned = decomissioned
        self.decomissioned_date = decomissioned_date
        
        # Clear the grid to avoid overlapping data
        for widget in self.details_frame.winfo_children():
            widget.destroy()

        # Assign the data to lists to iterate over
        data_labels = [
            "Equipment", "Department", "Date Installed", 
            "Maintenance Date", "Decomissioned", "Decomissioned Date"
        ]
        data_values = [
            ename, department, date_installed, 
            maintenance_date, decomissioned, decomissioned_date
        ]

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
        # If all the attributes are there then delete entry and go back to the database frame
        if all(
            hasattr(self, attr) for attr in 
            ['ename', 'date_installed', 'decomissioned', 'decomissioned_date', 'maintenance_date', 'department']
        ):
            DatabaseFunctions.delete_equipment(
                self.ename, self.date_installed, self.decomissioned,
                self.decomissioned_date, self.maintenance_date, self.department
            )
            self.master.frames['Database'].refresh_data(fetch_fresh=True)
            self.master.show_frame('Database')

    # Funciton to change color of label when hovered over
    def on_hover(self, event, label):
        label.configure(text_color='gray')

    # Default label color
    def on_leave(self, event, label):
        label.configure(text_color='white')

    # When a value is clicked go to the editing frmae
    def on_value_click(self, event, label_text, value):
        # Show a new frame for editing the value
        self.master.frames['EditE'].show_data(label_text, value, self.contact_id, self.ename, self.date_installed, self.decomissioned,
                                              self.decomissioned_date, self.maintenance_date, self.department)
        self.master.show_frame('EditE')