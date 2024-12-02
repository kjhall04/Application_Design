import customtkinter as ctk
import DatabaseFunctions
import ValidateEntry

class EditEquipmentData(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.container = ctk.CTkFrame(self)
        self.container.pack(expand=True, padx=20, pady=20)

        self.label = ctk.CTkLabel(self.container, text='Edit Equipment Data', font=('Arial', 20))
        self.label.pack(padx=20, pady=10)

        self.input_frame = ctk.CTkFrame(self.container)
        self.input_frame.pack(padx=20, pady=10)

        self.save_button = ctk.CTkButton(self.container, text='Update', command= self.save_changes)
        self.save_button.pack(pady=(10, 5))

        self.error_label = ctk.CTkLabel(self.container, text='', text_color='red')
        self.error_label.pack(padx=10)

        self.back_button = ctk.CTkButton(self.container, text='Back', fg_color='#243573', command=lambda: (self.master.show_frame('EData'), 
                                                                                                           self.error_label.configure(text='')))
        self.back_button.pack(pady=(5, 10))

    def show_data(self, label, value, contact_id, ename, date_installed, decomissioned, decomissioned_date,
                  maintenance_date, department):
        self.label_text = label
        self.old_value = value

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

    def save_changes(self):
        new_value = self.entry.get()
        column_mapping = {
            'Equipment': 'Ename',
            'Date Installed': 'DateInstalled',
            'Decomissioned': 'Decomissioned',
            'Decomissioned Date': 'DecomissionedDate',
            'Maintenance Date': 'MaintenanceDate',
            'Department': 'Department'
        }
        if self.label_text in column_mapping:
            column = column_mapping[self.label_text]
            
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

            if validation_result is not True:
                self.error_label.configure(text=f'{self.label_text}: {validation_result}')
                return

            success = DatabaseFunctions.update_single_data('equipment', column, new_value, self.conditions)
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