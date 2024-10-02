import re

# function to check for invalid characters in names
def check_name(name):
    # ensuring no digits in the name
    if re.match('^[a-zA-z]*$', name):
        return True
    else:
        raise ValueError(f"Invalid name '{name}'. Names can only contain letters.")

# function to check for invalid characters in phone numbers
def check_phone_number(phone_number):
    # ensuring date is typed correctly
    if re.match(r'^\d{3}-\d{3}-\d{4}$', phone_number):
        return True
    else:
        raise ValueError(f"Invalid phone number '{phone_number}'. Phone numbers can only contain numbers and dashes.")