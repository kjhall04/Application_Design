# Phonebook module
class Phonebook:
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

if __name__ == '__main__':
    pass