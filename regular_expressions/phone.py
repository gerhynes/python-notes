import re

def extract_phone(input):
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    match = phone_regex.search(input) 
    if match:
        return match.group()
    return None

def extract_all_phones(input):
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    return phone_regex.findall(input) 
    
def is_valid_phone(input):
    phone_regex = re.compile(r'^\d{3} \d{3}-\d{4}$')
    match = phone_regex.search(input) 
    if match:
        return True
    return False

def is_valid_phone_alt(input):
    phone_regex = re.compile(r'\d{3} \d{3}-\d{4}')
    match = phone_regex.fullmatch(input) 
    if match:
        return True
    return False

extract_phone("my number is 432 567-8976")
is_valid_phone("my number is 432 567-8976")
