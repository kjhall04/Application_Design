import customtkinter as ctk
import DatabaseFunctions
import ValidateEntry

# Class for edit contact data frame
class EditContactData(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Create the frame to put widgets in
        self.container = ctk.CTkFrame(self)
        self.container.pack(expand=True, padx=20, pady=20)

        # Title label
        self.label = ctk.CTkLabel(self.container, text='Edit Contact Data', font=('Arial', 20))
        self.label.pack(padx=20, pady=10)

        # Frame where the entry for editing is placed
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
                                         command=lambda: (self.master.show_frame('CData'), self.error_label.configure(text='')))
        self.back_button.pack(pady=(5, 10))

    # Shows the data that was clicked
    def show_data(self, label, value, fname, lname, phone, email):
        # Label and value to use later
        self.label_text = label
        self.old_value = value

        # Store conditions for updating the specific row
        self.conditions = {
            'Fname': fname,
            'Lname': lname,
            'PhoneNumber': phone,
            'Email': email,
        }

        # Create the input field for editing
        self.entry = ctk.CTkEntry(self.input_frame, placeholder_text=value, font=('Arial', 15))
        self.entry.grid(row=0, column=0, padx=10, pady=10)

    # Function to update database with single value
    def save_changes(self):
        # New value is what is input and make a dict of the databse columns
        new_value = self.entry.get() 
        column_mapping = {
            'First Name': 'Fname',
            'Last Name': 'Lname',
            'Phone': 'PhoneNumber',
            'Email': 'Email'
        }

        # If the label name is one of the columns then set it to a variable to be editted
        if self.label_text in column_mapping:
            column = column_mapping[self.label_text]
            # If one of the columns then validate the new value
            if column in ['Fname', 'Lname']:
                validation_result = ValidateEntry.name(new_value)
            elif column == 'PhoneNumber':
                validation_result = ValidateEntry.phone_number(new_value)
            elif column == 'Email':
                validation_result = ValidateEntry.email(new_value)
            else:
                validation_result = True

            # Show error if not correct
            if validation_result is not True:
                self.error_label.configure(text=f'{self.label_text}: {validation_result}')
                return

            # Add the new data to the database
            success = DatabaseFunctions.update_single_data('contact', column, new_value, self.conditions)
            # Clear the error and go back to the previous page showing the new data
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