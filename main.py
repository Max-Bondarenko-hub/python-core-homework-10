from collections import UserDict


class Field:

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    ...


class Phone(Field):

    def __init__(self, value):
        if value.isdigit() and len(value) == 10:
            self.value = value
        else:
            raise ValueError
            

class Record:

    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        try:
            phone = Phone(phone_number)
            self.phones.append(phone)
        except ValueError:
            print(f'{phone_number} is wrong format, nuber must be only digits and 10 numbers length')
    
    def remove_phone(self, removing_phone):
        for ph in self.phones:
            if ph.value == removing_phone:
                self.phones.remove(ph)
                return f'{removing_phone} was removed'
        raise ValueError

    def edit_phone(self, existed_number, new_number):
        new_phone = Phone(new_number)
        for ph in self.phones:
            if ph.value == existed_number:
                self.phones.remove(ph)
                self.phones.append(new_phone)
                return 'Phone number edited'
        raise ValueError

    def find_phone(self, phone_number):
        phone = Phone(phone_number)
        for ph in self.phones:
            if ph.value == phone.value:
                return phone
        return None 
  
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):

    def add_record(self, record: Record):
        self.data[record.name.value] = record
    
    def find(self, name: Name):
        if name in self.data:
            return self.data[name]
        return None 

    def delete(self, name_for_deleting: Name):
        if name_for_deleting in self.data:
            del self.data[name_for_deleting]