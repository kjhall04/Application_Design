#! python3
# Phonebook - will allow user to add name and number,
#             view all records, and delete info

# imports for custom modules
import Phonebook
import Contact
import Check

# main function
def main():
    # Create phone book object
    phone_book = Phonebook.Phonebook()

    while True:
        # prints out the menu and the options
        print('\nPhone Book Application')
        print('1. Add Contact')
        print('2. View Contacts')
        print('3. Search Contacts')
        print('4. Delete Contacts')
        print('5. Exit')

        #asks for the user input
        choice = input('\nType in the choice you want to use: ')

        # to add, creates a contact object wiht the name and phone number and adds it to the phonebook object
        if choice == '1':
            name = input('\nType in the name: ')
            # function to make sure name is without numbers
            Check.check_name(name)
            phone_number = input('Type in the phone number: ')
            # function to make sure phone number is without letters
            Check.check_phone_number(phone_number)
            contact = Contact.Contact(name, phone_number)
            phone_book.add_contact(contact)

        # calls the view contacts fuction and prints out the list values
        elif choice == '2':
            phone_book.view_contacts()

        # takes the input to search for contacts from the list using th name variable
        elif choice == '3':
            name = input('\nType in name to search: ')
            # function to make sure name is without numbers
            Check.check_name(name)
            phone_book.search_contact(name)

        # same think with search except it removes the name from the list
        elif choice == '4':
            name = input('\nType in name to delete: ')
            # function to make sure name is without numbers
            Check.check_name(name)
            phone_book.delete_contact(name)

        # ends the program
        elif choice == '5':
            print('\nExiting the phone book application')
            break
        
        # value error if the input is not correct
        else:
            raise ValueError('Enter a number between 1 and 5')

            
if __name__ == '__main__':
    # Run main function that creates the interactive menu

    main()