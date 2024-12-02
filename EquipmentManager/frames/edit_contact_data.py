import customtkinter as ctk
import DatabaseFunctions
import ValidateEntry

class EditContactData(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.container = ctk.CTkFrame(self)
        self.container.pack(expand=True, padx=20, pady=20)

        self.label = ctk.CTkLabel(self.container, text='Edit Contact Data', font=('Arial', 20))
        self.label.pack(padx=20, pady=10)

        self.input_frame = ctk.CTkFrame(self.container)
        self.input_frame.pack(padx=20, pady=10)

        self.save_button = ctk.CTkButton(self.container, text='Update', command= self.save_changes)
        self.save_button.pack(pady=(10, 5))

        self.error_label = ctk.CTkLabel(self.container, text='', text_color='red')
        self.error_label.pack(padx=10)

        self.back_button = ctk.CTkButton(self.container, text='Back', fg_color='#243573', command=lambda: (self.master.show_frame('CData'), 
                                                                                                           self.error_label.configure(text='')))
        self.back_button.pack(pady=(5, 10))

    def show_data(self, label, value, fname, lname, phone, email):
        self.label_text = label
        self.old_value = value

        # Store conditions for updating the specific row
        self.conditions = {
            'Fname': fname,
            'Lname': lname,
            'PhoneNumber': phone,
            'Email': email,
        }

        # Clear the input frame and recreate the input field
        for widget in self.input_frame.winfo_children():
            widget.destroy()

        # Create the input field for editing
        self.entry = ctk.CTkEntry(self.input_frame, placeholder_text=value, font=('Arial', 15))
        self.entry.grid(row=0, column=0, padx=10, pady=10)

    def save_changes(self):
        new_value = self.entry.get()
        column_mapping = {
            'First Name': 'Fname',
            'Last Name': 'Lname',
            'Phone': 'PhoneNumber',
            'Email': 'Email'
        }
        if self.label_text in column_mapping:
            column = column_mapping[self.label_text]

            if column in ['Fname', 'Lname']:
                validation_result = ValidateEntry.name(new_value)
            elif column == 'PhoneNumber':
                validation_result = ValidateEntry.phone_number(new_value)
            elif column == 'Email':
                validation_result = ValidateEntry.email(new_value)
            else:
                validation_result = True

            if validation_result is not True:
                self.error_label.configure(text=f'{self.label_text}: {validation_result}')
                return

            success = DatabaseFunctions.update_single_data('contact', column, new_value, self.conditions)
            if success:
                self.error_label.configure(text='')
                self.conditions[column] = new_value
                self.master.frames['CData'].show_data(
                    self.conditions['Fname'],
                    self.conditions['Lname'],
                    self.conditions['PhoneNumber'],
                    self.conditions['Email']
                )
                self.master.show_frame('CData')