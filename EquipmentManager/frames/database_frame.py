import customtkinter as ctk
import DatabaseFunctions
import CreateReport

class DatabaseFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.data_cache = {}
        self.all_data = DatabaseFunctions.get_all_data_for_menu()

        self.container = ctk.CTkFrame(self)
        self.container.pack(expand=True, padx=20, pady=20)

        self.container.grid_rowconfigure((0, 1), weight=1)
        self.container.grid_columnconfigure((0, 1), weight=1)

        self.label = ctk.CTkLabel(self.container, text='Database', font=('Arial', 25))
        self.label.grid(row=0, columnspan=2, padx=10, pady=(20, 10), sticky='n')

        self.search_var = ctk.StringVar()
        self.search_bar = ctk.CTkEntry(self.container, textvariable=self.search_var,)
        self.search_bar.grid(row=1, columnspan=2, padx=20, pady=(0, 10), sticky='ew')
        self.search_bar.bind('<KeyRelease>', self.filter_data)

        self.database = ctk.CTkScrollableFrame(self.container, width=350)
        self.database.grid(row=2, columnspan=2, padx=20, pady=(0, 20), sticky='nsew')

        self.database.grid_columnconfigure((0, 1), weight=1)

        self.add_contact_button = ctk.CTkButton(self.container, text='Add Contact', command=lambda: self.master.show_frame('AddC'))
        self.add_contact_button.grid(row=3, column=0, padx=(15, 5), pady=5, sticky='ew')

        self.add_equipment_button = ctk.CTkButton(self.container, text='Add Equipment', command=lambda: self.master.show_frame('AddE'))
        self.add_equipment_button.grid(row=3, column=1, padx=(5, 15), pady=5, sticky='ew')

        self.create_report_button = ctk.CTkButton(self.container, text='Create Report', command=self.create_report)
        self.create_report_button.grid(row=4, columnspan=2, padx=15, pady=(5, 0))

        self.error_label = ctk.CTkLabel(self.container, text='', text_color='red')
        self.error_label.grid(row=5, columnspan=2, padx=15, pady=2)

        self.exit_button = ctk.CTkButton(self.container, text='Exit Program', fg_color='#243573', command=self.master.quit)
        self.exit_button.grid(row=6, columnspan=2, padx=15, pady=(0, 10))

        self.row_counter = 0

        self.refresh_data()

    def on_hover(self, event, label):
        label.configure(text_color='gray')

    def on_leave(self, event, label):
        label.configure(text_color='white')

    def on_name_click(self, event, name):
        contact_data = DatabaseFunctions.get_contact_data()
        for fname, lname, phone, email in contact_data:
            full_name = f"{fname} {lname}"
            if full_name == name:
                # Display contact details
                self.master.frames['CData'].show_data(fname, lname, phone, email)
                self.master.show_frame('CData')
                break

    def on_eq_click(self, event, equipment):
        equipment_data = DatabaseFunctions.get_equipment_data()
        for contact_id, ename, date_installed, decomissioned, decomissioned_date, maintenance_date, department in equipment_data:
            if ename == equipment['Ename']:  # Compare the equipment name directly
                self.master.frames['EData'].show_data(
                    contact_id, ename, date_installed, decomissioned, decomissioned_date, maintenance_date, department
                )
                self.master.show_frame('EData')
                break

    def create_report(self):
        action = CreateReport.generate_pdf()
        if action != None:
            self.error_label.configure(text=action)

    def filter_data(self, event=None):
        search_term = self.search_var.get().lower()
        filtered_data = [
            entry for entry in self.all_data
            if search_term in f"{entry['Fname']} {entry['Lname']}".lower() 
        ]
        self.refresh_data(filtered_data)

    def refresh_data(self, data_list=None, fetch_fresh=False):
        if fetch_fresh or data_list is None:
            self.all_data = DatabaseFunctions.get_all_data_for_menu()
            data_list = self.all_data

        # Clear existing UI components in the scrollable frame
        for widget in self.database.winfo_children():
            widget.destroy()

        self.row_counter = 0
        grouped_data = {}

        for entry in data_list:
            full_name = f"{entry['Fname']} {entry['Lname']}"
            if full_name not in grouped_data:
                grouped_data[full_name] = []
            grouped_data[full_name].append({'Ename': entry['Ename']})

        for name, equipment_list in grouped_data.items():
            name_label = ctk.CTkLabel(
                self.database, 
                text=name, 
                font=('Arial', 15), 
                anchor='center'
            )
            name_label.grid(row=self.row_counter, column=0, padx=10, pady=5, sticky='e')
            self.row_counter += 1

            name_label._label.configure(cursor='hand2')

            name_label.bind('<Enter>', lambda e, label=name_label: self.on_hover(e, label))
            name_label.bind('<Leave>', lambda e, label=name_label: self.on_leave(e, label))
            name_label.bind('<Button-1>', lambda e, name=name: self.on_name_click(e, name))

            for equipment in equipment_list:
                equipment_label = ctk.CTkLabel(
                    self.database,
                    text=f"{equipment['Ename']}",
                    font=('Arial', 14),
                    anchor='w'
                )
                equipment_label.grid(row=self.row_counter - 1, column=1, padx=10, pady=5, sticky='w')
                self.row_counter += 1

                equipment_label._label.configure(cursor='hand2')

                equipment_label.bind('<Enter>', lambda e, label=equipment_label: self.on_hover(e, label))
                equipment_label.bind('<Leave>', lambda e, label=equipment_label: self.on_leave(e, label))
                equipment_label.bind('<Button-1>', lambda e, eq=equipment: self.on_eq_click(e, eq))