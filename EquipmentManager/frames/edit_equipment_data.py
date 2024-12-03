import customtkinter as ctk
import DatabaseFunctions
import ValidateEntry

# Class for edit equipment data frame
class EditEquipmentData(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Create frame to put the widgets in
        self.container = ctk.CTkFrame(self)
        self.container.pack(expand=True, padx=20, pady=20)

        # Title label
        self.label = ctk.CTkLabel(self.container, text='Edit Equipment Data', font=('Arial', 20))
        self.label.pack(padx=20, pady=10)

        # Frame where the entry to edit is placed
        self.input_frame = ctk.CTkFrame(self.container)
        self.input_frame.pack(padx=20, pady=10)

        # Button to save and update database
        self.save_button = ctk.CTkButton(self.container, text='Update', command= self.save_changes)
        self.save_button.pack(pady=(10, 5))

        # Error label
        self.error_label = ctk.CTkLabel(self.container, text='', text_color='red')
        self.error_label.pack(padx=10)

        # Button to go back to the previous page
        self.back_button = ctk.CTkButton(self.container, text='Back', fg_color='#243573', 
                                         command=lambda: (self.master.show_frame('EData'), self.error_label.configure(text='')))
        self.back_button.pack(pady=(5, 10))
    
    # Show the data that was clicked
    def show_data(self, label, value, contact_id, ename, date_installed, decomissioned, decomissioned_date,
                  maintenance_date, department):
        # Label and value to use later
        self.label_text = label
        self.old_value = value

        # Store conditions for updating the specific row
        self.conditions = {
            'contact_id': contact_id,
            'Ename': ename,
            'DateInstalled': date_installed,
            'Decomissioned': decomissioned,
            'DecomissionedDate': decomissioned_date,
            'MaintenanceDate': maintenance_date,
            'Department': department
        }

        # Create the input field for editing
        self.entry = ctk.CTkEntry(self.input_frame, placeholder_text=value, font=('Arial', 15))
        self.entry.grid(row=0, column=0, padx=10, pady=10)

    # Funciton to update database with a single value
    def save_changes(self):
        # New value is what is input and make a dict of the database columns
        new_value = self.entry.get()
        column_mapping = {
            'Equipment': 'Ename',
            'Date Installed': 'DateInstalled',
            'Decomissioned': 'Decomissioned',
            'Decomissioned Date': 'DecomissionedDate',
            'Maintenance Date': 'MaintenanceDate',
            'Department': 'Department'
        }

        # If the lavel name is one of the coulms then set it to a variable
        if self.label_text in column_mapping:
            column = column_mapping[self.label_text]
            # If one of the columns then validate the new value
            if column in ['Ename', 'Department']:
                validation_result = ValidateEntry.other_fields(new_value)
            elif column == 'DateInstalled':
                validation_result = ValidateEntry.date(new_value)
            elif column == 'Decomissioned':
                validation_result = ValidateEntry.boolean(new_value)
            elif column in ['DecomissionedDate', 'MaintenanceDate']:
                validation_result = ValidateEntry.date_or_NA(new_value)
            else:
                validation_result = True

            # Show error if not correct
            if validation_result is not True:
                self.error_label.configure(text=f'{self.label_text}: {validation_result}')
                return

            # Add the new data to the database
            success = DatabaseFunctions.update_single_data('equipment', column, new_value, self.conditions)
            # Clear the error and go backt to the previous page showing the new data
            if success:
                self.error_label.configure(text='')
                self.conditions[column] = new_value
                self.master.frames['EData'].show_data(
                    self.conditions['contact_id'],
                    self.conditions['Ename'], 
                    self.conditions['Department'], 
                    self.conditions['DateInstalled'], 
                    self.conditions['MaintenanceDate'],
                    self.conditions['Decomissioned'],
                    self.conditions['DecomissionedDate']
                )
                self.master.show_frame('EData')