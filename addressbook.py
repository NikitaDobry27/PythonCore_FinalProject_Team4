import re
import pickle
from datetime import date
from collections import UserDict


class Name:
    def __init__(self, name: str):
        self._name = None
        self.name = name

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        name_pattern = r'^[A-Za-zА-Яа-я їЇєЄ]{2,25}$'  # TODO check pattern
        if re.match(name_pattern, value):
            self._name = value
        else:
            raise ValueError('Name must contain only letters and be between 2 and 25 characters long')

    def change(self, value: str):
        self.name = value

    def __str__(self):
        return self._name


class Phone:
    def __init__(self, number: str):
        self._number = None
        self.number = number

    @property
    def number(self) -> str:
        return self._number

    @number.setter
    def number(self, value: str):
        digits = ''.join(re.findall(r'\d', value))
        if len(digits) >= 9:
            self._number = '+380' + digits[-9:]  # TODO verify or remake phone check
        else:
            raise ValueError('Phone number must have at least 9 digits')

    def change(self, value: str):
        self.number = value

    def __eq__(self, other) -> bool:
        return self.number == other.number

    def __str__(self):
        return self._number


class Birthday:
    def __init__(self, date: str):
        self._date = None
        self.date = date

    @property
    def date(self) -> date:
        return self._date

    @date.setter
    def date(self, value: str):
        day, month, year = map(int, re.split(r"[-|_|\\|/]", value))
        birthday = date(year, month, day)
        if birthday >= date.today():
            raise ValueError(f'Birthday must be in the past')
        self._date = birthday

    def change(self, value: str):
        self.date = value

    def __str__(self) -> str:
        return self._date.strftime("%d-%m-%Y")


class Email:  # TODO implement Email class
    def __init__(self):
        raise NotImplementedError


class Record:
    def __init__(self, name: Name,
                 phone: Phone = None,
                 birthday: Birthday = '',
                 email: Email = None):
        self.name = name
        self.phones = []
        self.birthday = birthday
        self.email = email
        if phone:
            self.add_phone(phone)

    def add_phone(self, phone: Phone):
        if phone not in self.phones:
            self.phones.append(phone)
        else:
            raise ValueError(f"Phone {phone} already exists in {self.name} record")

    def del_phone(self, phone: Phone):
        if phone in self.phones:
            self.phones.remove(phone)
        else:
            raise KeyError(f"Phone {phone} does not exist in {self.name} record")

    def set_birthday(self, birthday: Birthday):
        self.birthday = birthday

    def days_to_birthday(self):
        if not self.birthday:
            return None
        today = date.today()
        try:
            bday_this_year = self.birthday.date.replace(year=today.year)
        except ValueError:
            bday_this_year = self.birthday.date.replace(year=today.year, day=today.day - 1)
        if bday_this_year < today:
            bday_this_year = self.birthday.date.replace(year=today.year + 1)

        days_to_birthday = (bday_this_year - today).days
        return days_to_birthday

    def set_email(self, value):
        raise NotImplementedError  # TODO implement email set

    def __str__(self):
        return str(self.name) + ' ' + ' '.join(str(phone) for phone in self.phones) + ' ' + str(self.birthday)


class AddressBook(UserDict):

    def add_record(self, record: Record):
        self.data[record.name.name] = record

    def del_record(self, name):
        if name in self.data:
            self.data.pop(name)
        else:
            raise KeyError(f'Record with name {name} does not exist')

    # TODO beautiful record output (probably with colours)
    def show_records(self, records_per_page: int = 1, search_pattern: str = '') -> str:
        output = []
        record_count = 0
        record: Record
        for record in self.data.values():
            search_string = str(record) + " " + str(record.days_to_birthday()) + '\n'
            if search_pattern != '':
                if re.search(search_pattern, search_string, flags=re.IGNORECASE):
                    output.append(search_string)
                    record_count += 1
            else:
                output.append(search_string)
                record_count += 1
            if record_count % records_per_page == 0:
                yield '\n'.join(output)
                output = []
        if output:
            yield ''.join(output)

    def save_records_to_file(self, filename):
        with open(filename, "wb") as fw:
            pickle.dump(self.data, fw)

    def read_records_from_file(self, filename):
        try:
            with open(filename, "rb") as fr:
                content = pickle.load(fr)
                self.data.update(content)
        except FileNotFoundError:
            pass


if __name__ == '__main__':
    # TODO asserts for all classes of AddressBook
    ...
