# global variables for checking name and number validation
CHECK_NAME = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
CHECK_NUMBER = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'
                'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v'
                'w', 'x', 'y', 'z']

# function to check for numbers where they shouldn't be
def check_name(name):
    # making sure numbers arent put in for a name
    for i in name:
        if i in CHECK_NAME:
            raise ValueError('No numbers should be typed in the name.')
    
# fucntion to check for letters where they shouldn't be
def check_phone_number(phone_number):
    # make sure letters are not in the phone number
    for i in phone_number.lower():
        if i in CHECK_NUMBER:
            raise ValueError('No letters should be in the phone number.')

if __name__ == '__main__':
    pass