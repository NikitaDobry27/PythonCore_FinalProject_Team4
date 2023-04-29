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
        self._name = value        


class _Phone(_Field):
    def __init__(self, phone):
        self.phone = phone

    @property
    def phone(self):
        return self._phone
        
    @phone.setter
    def phone(self, value):
        if not self.is_valid(value):
            raise ValueError("Phone number is not valid!")
        self._phone = value

    def is_valid(self, value):
        """
        Examples of acceptable phone number values: +380955555555, 0955555555, 575555555, +44-20-7123-4567
        Examples of unacceptable phone number values: +380955552252525, 093321247124612654, 039245, +3809427
        """
        pattern = re.compile(r'^\+(?:\d[\s-]?){9,14}\d$|\d{9,10}$')
        return bool(pattern.match(value))


class _Email(_Field):
    def __init__(self, email):
        self.email = email

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        if not self.is_valid(value):
            raise ValueError("Provided email is not valid")
        self._email = value

    def is_valid(self, value):
        """
        Pattern will match: 123@test.com, j@n.com, 231@em.co.ua, 231@em.com.ua
        Pattern will not match: 123.com, 123@com, 123@23.com, 1.1.1.1@gnisah.com, ыри@оы,con
        """
        pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        return bool(pattern.match(value))

class _Birthday(_Field):
    def __init__(self, birthday):
        self.birthday = birthday
    
    @property
    def birthday(self):
        return self._birthday
    
    @birthday.setter
    def birthday(self, value):
        if not self.is_valid(value):
            return ValueError("Birthday is not valid. Acceptable format: yyyy-m-d. Don't use dates in future")
        self._birthday = value

    def is_valid(self, value):
        try:
            birthday_date = datetime.strptime(value, "%Y-%m-%d")
            current_date = datetime.now()

            if birthday_date > current_date:
                return False
            
            return True
        except ValueError:
            return False

class _Record(_Field):
    raise NotImplementedError


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
