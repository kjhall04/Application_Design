class Contact:
    # Initializer and instance attributes name and phone_number
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
    
    # returns the info about the contact (name and phone number)
    def __str__(self):
        return 'Name: ' + self.name + ', Phone Number: ' + self.phone_number

if __name__ == '__main__':
    pass