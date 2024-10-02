#! python3
# Phonebook - Lets the user alter a pre-existing phonebook database
#             with adding, deleting, searching, and viewing all

# imports for custom modules
import AddRecord
import DeleteRecord
import ViewAllRecords
import SearchRecord
import CheckInput
import CreateReport

# function for all name input
def input_name(prompt):
    while True:
        try:
            name = input(prompt)
            CheckInput.check_name(name)
            return name
        except ValueError as e:
            print(f"\nError: {e}")
            print("Please provide a valid name.")

# function for all number inputs with error handling
def input_phone_number(prompt):
    while True:
        try:
            phone_number = input(prompt)
            CheckInput.check_phone_number(phone_number)
            return phone_number
        except ValueError as e:
            print(f"\nError: {e}")
            print("Please provide a valid phone number.")

# function for add record
def add_record():
    Fname = input_name('\nType in the first name: ')
    Lname = input_name('\nType in the last name: ')
    phone_number = input_phone_number('\nType in the phone number in the format XXX-XXX-XXXX: ')
    AddRecord.add_record(Fname, Lname, phone_number)

# function for view all records
def view_records():
    ViewAllRecords.view_records()

# fucntion to search the records and print if found
def search_record():
    Fname = input_name('\nType in the first name of the person to search: ')
    Lname = input_name('\nType in the last name of the person to search: ')
    SearchRecord.search_record(Fname, Lname)

# function to delete info from the database
def delete_record():
    Fname = input_name('\nType in the first name of the person to delete: ')
    Lname = input_name('\nType in the last name of the person to delete: ')
    DeleteRecord.delete_record(Fname, Lname)

# fucntion to create report
def create_report():
    CreateReport.write_html()
    CreateReport.printreport()

# main function
def main():
    while True:
        # prints out the menu and the options
        print('\nPhone Book Application')
        print('1. Add Contact')
        print('2. View All Contacts')
        print('3. Search Contacts')
        print('4. Delete Contacts')
        print('5. Create Report')
        print('6. Exit')

        # asks for the user input
        choice = input('\nType in the choice you want to use: ')

        # adds contact info to the database
        if choice == '1':
            add_record()

        # calls the view records function and prints out the list of values
        elif choice == '2':
            view_records()

        # searches the database and prints out the inputted info if found
        elif choice == '3':
            search_record()

        # deletes info from the database
        elif choice == '4':
            delete_record()

        # creates report from the database
        elif choice == '5':
            create_report()

        # ends the program
        elif choice == '6':
            print('\nExiting the phone book application.')
            break

        # handle invalid choices
        else:
            print("\nInvalid choice. Please enter a number between 1 and 6.")

if __name__ == '__main__':
    # Run main function that creates the interactive menu

    main()