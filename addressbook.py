from collections import UserDict
from abc import ABC


class _Field(ABC):
    def __init__(self):
        raise NotImplementedError


class _Name(_Field):
    def __init__(self):
        super().__init__()
        raise NotImplementedError


class _Phone(_Field):
    def __init__(self):
        super().__init__()
        raise NotImplementedError


class _Email(_Field):
    def __init__(self):
        super().__init__()
        raise NotImplementedError


class _Birthday(_Field):
    def __init__(self):
        super().__init__()
        raise NotImplementedError


class Record(Name, Phone):
    phones = []

    def __init__(self, name, phone):
        self.name = name
        self.phone = []
        if phone:
            self.phones.append(phone)

    def name_name(self):
        self.value = Name

    def phone_phone(self):
        self.value = Phone

    def add_phone(self, phone):
        if not phone in self.phones:
            self.phones.append(phone)

    def chenge_phone(self, phone, ph):
        if phone in self.phones:
            ind = self.phones.index(phone)
            self.phones[ind] = ph

    def remove_phone(self, phone):
        if phone in self.phones:
            self.phones.remove(phone)


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
        return self.data



if __name__ == '__main__':
    ...
