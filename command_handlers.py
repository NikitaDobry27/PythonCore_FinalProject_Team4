from addressbook import AddressBook
from notebook import NoteBook
from file_sorter import file_sorter


def input_error(func):
    def execute(*args):
        try:
            return func(*args)
        except IndexError as index_error:
            return index_error
        except ValueError as value_error:
            return value_error
        except KeyError as key_error:
            return key_error
        except AttributeError as attribute_error:
            return attribute_error
    return execute


def welcome_message(*args) -> str:
    message = "Hi! How can i help you?"
    return message


def help_message(*args) -> str:
    message = "help message"
    return message


@input_error
def add_handler(addressbook: AddressBook, *args) -> str:
    if args[0] == 'record':
        addressbook.add_record(' '.join(args[1]))
        message = f'New record with name {args[1]} added to addressbook.'
    elif args[0] == 'phone':
        addressbook[args[1]].add_phone(args[2])
        message = f'Phone {args[2]} added to {args[1]} record.'
    elif args[0] == 'email':
        addressbook[args[1]].set_email(args[2])
        message = f'Email {args[2]} added to {args[1]} record.'
    elif args[0] == 'birthday':
        addressbook[args[1]].set_birthday(args[2])
        message = f'Birthday {args[2]} added to {args[1]} record.'
    else:
        message = f'add does not support {args[0]} command.'
    return message


@input_error
def show_handler(addressbook: AddressBook, *args) -> str:
    addressbook.show_records()


@input_error
def change_handler(addressbook: AddressBook, *args) -> str:
    raise NotImplementedError


@input_error
def del_handler(addressbook: AddressBook, *args) -> str:
    raise NotImplementedError


@input_error
def birthday_handler(addressbook: AddressBook, *args):
    raise NotImplementedError


@input_error
def search_handler(addressbook: AddressBook, *args):
    query = " ".join(args)
    results = addressbook.search(query)

    if not results:
        return "No results found"

    response = ""
    for record in results:
        response += f"{str(record.name).capitalize()}: {record.phone}\n"

    return response

def save_data(addressbook: AddressBook, *args) -> str:
    raise NotImplementedError


def load_data(addressbook: AddressBook, *args) -> str:
    raise NotImplementedError


@input_error
def sort_files(addressbook: AddressBook, *args) -> str:
    message = file_sorter(args[0])


def notes(addressbook: AddressBook, *args):
    raise NotImplementedError


function = {'hello': welcome_message,
            'help': help_message,
            'add': add_handler,
            'show': show_handler,
            'change': change_handler,
            'del': del_handler,
            'birthday': birthday_handler,
            'search': search_handler,
            'save': save_data,
            'load': load_data,
            'sort_files': sort_files}
