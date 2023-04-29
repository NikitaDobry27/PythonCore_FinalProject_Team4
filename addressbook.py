from collections import UserDict
from abc import ABC
from datetime import datetime
import re


class _Field(ABC):
    def __init__(self):
        raise NotImplementedError


class _Name(_Field):
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name can not be empty!")
        
        if not re.compile(r'^[a-zA-Zа-щА-ЩЬьЮюЯяЇїІіЄєҐґ]{2,25}$').match(value):
            raise ValueError("Name is not valid. It should contain only letters (Latin or Ukrainian) and be no longer than 25 characters.")
        self._name = value        


class _Phone(_Field):
    def __init__(self, phone):
        self.phone = phone

    @property
    def phone(self):
        return self._phone
        
    @phone.setter
    def phone(self, value):
        if not re.compile(r'^\+(?:\d[\s-]?){9,14}\d$|\d{9,10}$').match(value):
            raise ValueError("Phone number is not valid!")
        self._phone = value


class _Email(_Field):
    def __init__(self, email):
        self.email = email

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        
        if not re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$').match(value):
            raise ValueError("Provided email is not valid")
        self._email = value

class _Birthday(_Field):
    def __init__(self, birthday):
        self.birthday = birthday
    
    @property
    def birthday(self):
        return self._birthday
    
    @birthday.setter
    def birthday(self, value):
        try:
            birthday_date = datetime.strptime(value, "%Y-%m-%d")
            current_date = datetime.now()

            if birthday_date > current_date:
                raise ValueError("Birthday is not valid. Don't use dates in the future")
            
            self._birthday = value
        except ValueError:
            raise ValueError("Birthday is not valid. Acceptable format: yyyy-m-d")

class _Record(_Field):
    pass

class AddressBook(UserDict):
    ...

    def search(self, query):
        results = []
        for record in self.data.values():
            if query.lower() in record.name.lower() or query in record.phone:
                results.append(record)
        return results

    ...

if __name__ == '__main__':
    ...