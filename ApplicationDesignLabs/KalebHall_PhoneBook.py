#! python3
# Phonebook - will allow user to add name and number,
#             view all records, and delete info
        
# Class for contacts
class Contact:
    # Initializer and instance attributes name and phone_number
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
    
    # returns the info about the contact (name and phone number)
    def __str__(self):
        return 'Name: ' + self.name + ', Phone Number:' + self.phone_number

# Class for the phone book
class PhoneBook:
    # creates an empty list to store contacts
    def __init__(self):
        self.contacts = []
    
    # function for adding contact info to the phone book
    def add_contact(self, contact):
        self.contacts.append(contact)
        print('\nContact ' + contact.name + ' added sucessfully.')

    # function to view contacts
    def view_contacts(self):
        if self.contacts == []:
            print('\nNo contacts avialable.')
            return
        for contact in self.contacts:
            print(contact)

    # function for searching for contacts
    def search_contact(self, name):
        for contact in self.contacts: 
            if contact.name.lower() == name.lower():
                print(contact)
                return
        print('\nContact with name ' + name + ' not found.')

    # funtion for deleting contacts
    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print('\nContact ' + name + ' deleted sucessfully.')
                return
        print('\nContact with name ' + name + ' not found.')

# main function
def main():
    # Create phone book object
    phone_book = PhoneBook()

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
            phone_number = input('Type in the phone number: ')
            contact = Contact(name, phone_number)
            phone_book.add_contact(contact)

        # calls the view contacts fuction and prints out the list values
        elif choice == '2':
            phone_book.view_contacts()

        # takes the input to search for contacts from the list using th name variable
        elif choice == '3':
            name = input('\nType in name to search: ')
            phone_book.search_contact(name)

        # same think with search except it removes the name from the list
        elif choice == '4':
            name = input('\nType in name to delete: ')
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