import customtkinter as ctk
import DatabaseFunctions
import CreateReport

class DatabaseFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Create the frame to put the widgets
        self.container = ctk.CTkFrame(self)
        self.container.pack(expand=True, padx=20, pady=20)

        # Configure the frame to place widgets properly
        self.container.grid_rowconfigure((0, 1), weight=1)
        self.container.grid_columnconfigure((0, 1), weight=1)

        # Title label
        self.label = ctk.CTkLabel(self.container, text='Database', font=('Arial', 25))
        self.label.grid(row=0, columnspan=2, padx=10, pady=(20, 10), sticky='n')

        # Search bar and command to dynamically show data when typed
        self.search_var = ctk.StringVar()
        self.search_bar = ctk.CTkEntry(self.container, textvariable=self.search_var,)
        self.search_bar.grid(row=1, columnspan=2, padx=20, pady=(0, 10), sticky='ew')
        self.search_bar.bind('<KeyRelease>', self.filter_data)

        # Create the frame to display all the contact and equipment data
        self.database = ctk.CTkScrollableFrame(self.container, width=350)
        self.database.grid(row=2, columnspan=2, padx=20, pady=(0, 20), sticky='nsew')

        # Congifure the database to show data properly
        self.database.grid_columnconfigure((0, 1), weight=1)

        # Button to go to the add contact page
        self.add_contact_button = ctk.CTkButton(self.container, text='Add Contact', command=lambda: self.master.show_frame('AddC'))
        self.add_contact_button.grid(row=3, column=0, padx=(15, 5), pady=5, sticky='ew')

        # Button to go to the add equipment page
        self.add_equipment_button = ctk.CTkButton(self.container, text='Add Equipment', command=lambda: self.master.show_frame('AddE'))
        self.add_equipment_button.grid(row=3, column=1, padx=(5, 15), pady=5, sticky='ew')

        # Button to run the create report function and go to it
        self.create_report_button = ctk.CTkButton(self.container, text='Create Report', command=self.create_report)
        self.create_report_button.grid(row=4, columnspan=2, padx=15, pady=(5, 0))

        # Error label
        self.error_label = ctk.CTkLabel(self.container, text='', text_color='red')
        self.error_label.grid(row=5, columnspan=2, padx=15, pady=2)

        # Button to exit and end the program
        self.exit_button = ctk.CTkButton(self.container, text='Exit Program', fg_color='#243573', command=self.master.quit)
        self.exit_button.grid(row=6, columnspan=2, padx=15, pady=(0, 10))

        # Set the row counter for later
        self.row_counter = 0

        # Refresh the data/display the data from 
        self.refresh_data()

    # Change the label color when hovered over
    def on_hover(self, event, label):
        label.configure(text_color='gray')

    # Default label color
    def on_leave(self, event, label):
        label.configure(text_color='white')

    # When name is clicked then go and display all associated data
    def on_name_click(self, event, name):
        contact_data = DatabaseFunctions.get_contact_data()
        for fname, lname, phone, email in contact_data:
            full_name = f"{fname} {lname}"
            if full_name == name:
                # Display contact details
                self.master.frames['CData'].show_data(fname, lname, phone, email)
                self.master.show_frame('CData')
                break
    
    # When equipment is clicked then go and display all associated data
    def on_eq_click(self, event, equipment):
        equipment_data = DatabaseFunctions.get_equipment_data()
        for contact_id, ename, department, date_installed, maintenance_date, decomissioned, decomissioned_date in equipment_data:
            if ename == equipment['Ename']:
                # Display equipment details
                self.master.frames['EData'].show_data(
                    contact_id, ename, department, date_installed, maintenance_date, decomissioned, decomissioned_date
                )
                self.master.show_frame('EData')
                break
    
    # Function to run the create report module
    def create_report(self):
        action = CreateReport.generate_pdf()
        # If it cant work then display the returned error
        if action != None:
            self.error_label.configure(text=action)

    # Function for displaying data as it is typed in the search bar
    def filter_data(self, event=None):
        # Get what is typed and assign it to a variable
        search_term = self.search_var.get().lower()
        # Put the data in a list
        filtered_data = [
            entry for entry in self.all_data
            if search_term in f"{entry['Fname']} {entry['Lname']}".lower() 
        ]
        # Refresh page with the new data
        self.refresh_data(filtered_data)

    # Refresh all the database date
    def refresh_data(self, data_list=None, fetch_fresh=False):
        # Retrieve new data
        if fetch_fresh or data_list is None:
            self.all_data = DatabaseFunctions.get_all_data_for_menu()
            data_list = self.all_data

        # Clear existing UI components in the scrollable frame
        for widget in self.database.winfo_children():
            widget.destroy()

        # Set the row counter and an empty dict for data
        self.row_counter = 0
        grouped_data = {}

        # Add the contact names to the dict to be displayed
        for entry in data_list:
            full_name = f"{entry['Fname']} {entry['Lname']}"
            if full_name not in grouped_data:
                grouped_data[full_name] = []
            grouped_data[full_name].append({'Ename': entry['Ename']})

        # Iterate through grouped data to display it
        for name, equipment_list in grouped_data.items():
            # Name label
            name_label = ctk.CTkLabel(
                self.database, 
                text=name, 
                font=('Arial', 15), 
                anchor='center'
            )
            name_label.grid(row=self.row_counter, column=0, padx=10, pady=5, sticky='e')
            
            # add to the row counter for the next row
            self.row_counter += 1

            # Assign label to interact with cursor
            name_label._label.configure(cursor='hand2')

            # Label commands for interaction
            name_label.bind('<Enter>', lambda e, label=name_label: self.on_hover(e, label))
            name_label.bind('<Leave>', lambda e, label=name_label: self.on_leave(e, label))
            name_label.bind('<Button-1>', lambda e, name=name: self.on_name_click(e, name))

            # For all assosicated equipment
            for equipment in equipment_list:
                # Equipment label
                equipment_label = ctk.CTkLabel(
                    self.database,
                    text=f"{equipment['Ename']}",
                    font=('Arial', 14),
                    anchor='w'
                )
                equipment_label.grid(row=self.row_counter - 1, column=1, padx=10, pady=5, sticky='w')

                # Iterate to the next row
                self.row_counter += 1

                # Assign cursor to the label for interaction
                equipment_label._label.configure(cursor='hand2')

                # Commands for interaction
                equipment_label.bind('<Enter>', lambda e, label=equipment_label: self.on_hover(e, label))
                equipment_label.bind('<Leave>', lambda e, label=equipment_label: self.on_leave(e, label))
                equipment_label.bind('<Button-1>', lambda e, eq=equipment: self.on_eq_click(e, eq))