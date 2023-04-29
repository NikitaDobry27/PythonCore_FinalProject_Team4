from addressbook import AddressBook
from notebook import NoteBook


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
    raise NotImplementedError


@input_error
def add_handler(addressbook: AddressBook, *args) -> str:
    raise NotImplementedError


@input_error
def show_handler(addressbook: AddressBook, *args) -> str:
    raise NotImplementedError


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


def sort_files(addressbook: AddressBook, *args):
    raise NotImplementedError


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
