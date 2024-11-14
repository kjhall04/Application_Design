import re

# All functions return True if valid or an error message about the wrong input.

def date(entry: str):
    # Validates a date in MM/DD/YYYY format.
    if re.match(r'^(0[1-9]|1[0-2])/(0[1-9]|[1-2][0-9]|3[0-1])/([0-9]{4})$', entry):
        return True
    else:
        return f"'{entry}' is an invalid date format. Expected MM/DD/YYYY."

def phone_number(entry: str):
    # Validates a phone number in XXX-XXX-XXXX format.
    if re.match(r'^\d{3}-\d{3}-\d{4}$', entry):
        return True
    else:
        return f"'{entry}' is an invalid phone number format. Expected XXX-XXX-XXXX."

def age(entry: str):
    # Validates age by ensuring the entry is a positive integer.
    if entry.isdigit():
        return True
    else:
        return f"'{entry}' is an invalid age. Expected a positive integer."

def name(entry:str):
    # Validates names by ensuring their are only letters and spaces
    for char in entry:
        if not char.isalpha() and not char.isspace():
            return f"'{entry}' is invalid. Only letters and spaces are allowed."
    return True

def email(entry: str):
    # Validates an email address pattern.
    if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', entry):
        return True
    else:
        return f"'{entry}' is an invalid email format."

def boolean(entry: str):
    # Validates a string representation of a boolean, accepting 'true' or 'false'.
    if entry.lower() == 'true':
        return True
    elif entry.lower() == 'false':
        return True
    else:
        return f"'{entry}' is invalid. Expected 'True' or 'False'."
    
def other_fields(entry: str):
    # Validates all other fields, allowing alphabetic characters, spaces, and digits.
    for char in entry:
        if not char.isalpha() and not char.isspace() and not char.isdigit():
            return f"'{entry}' is invalid. Only letters, spaces, and numbers are allowed."
    return True

    
# Main is to make sure the functions above work properly
if __name__ == '__main__':
    # Uncomment and change the function values to test different funcitons

    # print(date('09/64/2024'))
    # print(phonenumber('601-888-8888'))
    # print(age('78'))
    # print(name('el capitan4565'))
    # print(boolean('sdfas'))
    # print(email('kalebhall678678'))
    # print(other_fields('el capitan4565'))
    pass