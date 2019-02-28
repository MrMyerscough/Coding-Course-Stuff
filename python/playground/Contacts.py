class Contacts():
    first_name = None
    last_name = None
    address = None
    phone_number = None
    email = None
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone_number = phone_number
        self.email = email

    full_name = first_name + last_name

    contacts_list = []

    def get_phone_number(self, full_name):
        