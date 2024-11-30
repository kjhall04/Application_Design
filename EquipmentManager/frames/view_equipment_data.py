import customtkinter as ctk
import DatabaseFunctions

class ViewEquipmentData(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.container = ctk.CTkFrame(self)
        self.container.pack(expand=True, padx=20, pady=20)

        self.label = ctk.CTkLabel(self.container, text='Equipment Details', font=('Arial', 20))
        self.label.pack(padx=20, pady=10)

        self.details_label = ctk.CTkLabel(self.container, text='', font=('Arial', 15))
        self.details_label.pack(padx=20, pady=10)

        self.delete_button = ctk.CTkButton(self.container, text='Delete Entry', command=lambda: self.delete_entry())
        self.delete_button.pack(pady=(10, 5))

        self.back_button = ctk.CTkButton(self.container, text='Back', fg_color='#243573', command=lambda: self.master.show_frame('Database'))
        self.back_button.pack(pady=(5, 10))

    def show_data(self, contact_id, ename, date_installed, decomissioned, decomissioned_date, maintenance_date, department):
        self.ename = ename
        self.date_installed = date_installed
        self.decomissioned = decomissioned
        self.decomissioned_date = decomissioned_date
        self.maintenance_date = maintenance_date
        self.department = department

        details = f'Equipment: {ename}\nDepartment: {department}\nDate Installed: {date_installed}\nMaintenance Date: {maintenance_date}\nDecomissioned: {decomissioned}\nDecomissioned Date: {decomissioned_date}'
        self.details_label.configure(text=details)
        return

    def delete_entry(self):
        if hasattr(self, 'ename') and hasattr(self, 'date_installed') and hasattr(self, 'decomissioned') and hasattr(self, 'decomissioned_date') and hasattr(self, 'maintenance_date') and hasattr(self, 'department'):
            DatabaseFunctions.delete_equipment(self.ename, self.date_installed, self.decomissioned, self.decomissioned_date, self.maintenance_date, self.department)
            self.master.show_frame('Database')
        return