import re
from abc import ABC, abstractmethod
from datetime import date, datetime
from collections import UserDict
import pickle


class _Field(ABC):
    def __init__(self, value):
        self._value = None
        self.value = value

    @property
    @abstractmethod
    def value(self):
        raise NotImplementedError

    @value.setter
    @abstractmethod
    def value(self, value):
        raise NotImplementedError


class _Name(_Field):
    def __init__(self, value):
        super().__init__(value)

    @property
    def value(self) -> str:
        return self._value

    @value.setter
    def value(self, value) -> None:
        name_value_pattern = r'^[A-Za-zА-Яа-яїЇєЄ]{2,25}$'
        if re.match(name_value_pattern, value):
            self._value = value
        else:
            raise ValueError("Name is not valid. It should contain only letters and be no longer than 25 characters.")


class _Phone(_Field):
    def __init__(self, value):
        super().__init__(value)

    @property
    def value(self) -> str:
        return self._value
        
    @value.setter
    def value(self, value):
        if not re.compile(r'^\+(?:\d[\s-]?){9,14}\d$|\d{9,10}$').match(value):
            raise ValueError("Phone number is not valid!")
        self._value = value

    def __eq__(self, _obj) -> bool:
        return self.value == _obj.value


class _Email(_Field):
    def __init__(self, value):
        super().__init__(value)

    @property
    def value(self) -> str:
        return self._value
    
    @value.setter
    def value(self, value):
        
        if not re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$').match(value):
            raise ValueError("Provided email is not valid")
        self._value = value


class _Birthday(_Field):
    def __init__(self, value):
        super().__init__(value)
    
    @property
    def value(self) -> date:
        return self._value
    
    @value.setter
    def value(self, value) -> None:
        email_value_pattern = r"[-|_|\\|/]"
        day, month, year = map(int, re.split(email_value_pattern, value))
        birthday = date(year, month, day)
        if birthday >= date.today():
            raise ValueError(f'Birthday must be in the past')
        self._value = birthday

    def __str__(self) -> str:
        return self._value.strftime("%d-%m-%Y")


class _Record:
    def __init__(self, name: str):
        self.name = _Name(name)
        self.phones = []
        self.birthday = None
        self.email = None

    def add_phone(self, phone: str):
        phone = _Phone(phone)
        if phone not in self.phones:
            self.phones.append(phone)
        else:
            raise ValueError(f"Phone {phone.value} already exists in {self.name.value} record")

    def del_phone(self, phone: str):
        phone = _Phone(phone)
        if phone in self.phones:
            self.phones.remove(phone)
        else:
            raise KeyError(f"Phone {phone.value} does not exist in {self.name.value} record")

    def set_birthday(self, birthday: str):
        birthday = _Birthday(birthday)
        self.birthday = birthday

    def set_email(self, email: str):
        email = _Email(email)
        self.email = email

    def days_to_birthday(self) -> int | None:
        if not self.birthday:
            return None
        today = date.today()
        try:
            birthday_this_year = self.birthday.value.replace(year=today.year)
        except ValueError:
            birthday_this_year = self.birthday.value.replace(year=today.year, day=today.day - 1)
        if birthday_this_year < today:
            birthday_this_year = self.birthday.value.replace(year=today.year + 1)
        days_to_birthday = (birthday_this_year - today).days
        return days_to_birthday

    def __str__(self):
        str_phones = ' '.join(phone.value for phone in self.phones)
        str_email = self.email.value if self.email else str()
        str_birthday = str(self.birthday) if self.birthday else str()
        return '|'.join((self.name.value, str_email, str_phones, str_birthday))


class AddressBook(UserDict):

    def add_record(self, name: str):
        if name not in self.data:
            self.data[name] = _Record(name)
        else:
            raise KeyError('Record with this name already exists.')

    def change_phone(self, old_phone, new_phone):
        for record in self.data.values():
            if old_phone in record.phones:
                try:
                    record.add_phone(new_phone)
                    record.del_phone(old_phone)
                except ValueError as e:
                    print(str(e))
                break
        else:
            raise KeyError(f'Phone {old_phone} is not found in any record')

    def del_email(self, email: str):
        for record in self.data.values():
            if record.email == email:
                record.email = None
                break
        else:
            raise KeyError(f'Email {email} is not found in any record')

    def del_phone(self, phone: str):
        for record in self.data.values():
            if phone in record.phones:
                record.del_phone(phone)
                break
        else:
            raise KeyError(f'Phone {phone} is not found in any record')

    def del_birthday(self, birthday):
        for record in self.data.values():
            if record.birthday and str(record.birthday) == str(birthday):
                record.birthday = None
                break
        else:
            raise KeyError(f'Birthday {birthday} is not found in any record')

    def show_records(self):
        for i in self.data.values():
            print(str(i))

    def search(self, query):
        results = []
        for record in self.data.values():
            if query.lower() in record.name.lower() or query in record.phone:
                results.append(record)
        return results

    def contacts_with_days_to_bday(self, days):
        result = []
        for record in self.values():
            bd = datetime.strptime(record.bday, "%d %B %Y")
            today = date.today()
            current_year_birthday = date(today.year, bd.month, bd.day)
            if current_year_birthday < today:
                current_year_birthday = date(today.year + 1, bd.month, bd.day)
            delta = current_year_birthday - today
            if delta.days == int(days):
                result.append(f"{record.name}, {record.bday}")
        return "\n".join(result)
    
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
    # Примеры работы с адресной книгой
    addressbook = AddressBook()
    addressbook.add_record("Alexander")                         # Создаем контакт
    addressbook["Alexander"].add_phone('111111111')             # Добавляем к контакту 1 номер
    addressbook["Alexander"].add_phone('111111112')             # Добавляем к контакту 2 номер
    addressbook["Alexander"].add_phone('111111113')             # Добавляем к контакту 3 номер
    addressbook["Alexander"].set_birthday('30-09-2022')         # Добавляем к контакту день рождения
    addressbook["Alexander"].set_email('abcdef@gmail.com')      # Добавляем к контакту емеил
    # удалять день рождения и емеил пока что нельзя, только переназначать
    addressbook["Alexander"].del_phone('111111112')             # Удаляем номер
    # изменение номера телефона делается путем удаления старого номера и добавления нового
    addressbook.show_records()                                  # заглушка, нужно сделать через генератор
    addressbook.del_record("Alexander")                         # Удаляем запись
    addressbook.show_records()
