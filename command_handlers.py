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
        except NotImplementedError:
            return 'This feature is not implemented'
    return execute


def welcome_message(*args) -> str:
    message = "Hi! How can i help you?"
    return message


def help_message(*args) -> str:
    message = """
Commands and their usage:
add: 
    record 'name'                        : adds a new record with specified name.
    phone 'name' 'phone'                 : add new phone to record.
    email 'name' 'email'                 : add email to record. Can be only one.
    birthday 'name' 'birthday'           : add birthday to record. Can be only one. Birthday format dd-mm-yyyy.
change: 
    phone 'name' 'old phone' 'new phone' : change old phone with new one.
    email 'name' 'email'                 : change email in record. 
    birthday 'name' 'birthday'           : change birthday in record. Birthday format dd-mm-yyyy.
del: 
    record 'name'                        : delete record with specified name.
    phone 'name' 'phone'                 : delete phone from record.
    email 'name' 'email'                 : NOT IMPLEMENTED
    birthday 'name' 'birthday'           : NOT IMPLEMENTED
    """
    return message


@input_error
def add_handler(addressbook: AddressBook, *args) -> str:
    if args[0] == 'record':
        addressbook.add_record(args[1])
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
def change_handler(addressbook: AddressBook, *args) -> str:
    if args[0] == 'phone':
        addressbook[args[1]].del_phone(args[2])
        addressbook[args[1]].add_phone(args[3])
        message = f'Phone in record {args[1]} was changed from {args[2]} to {args[3]} record.'
    elif args[0] == 'email':
        addressbook[args[1]].set_email(args[2])
        message = f'Email in record {args[1]} was changed'
    elif args[0] == 'birthday':
        addressbook[args[1]].set_birthday(args[2])
        message = f'Email in record {args[1]} was changed'
    else:
        message = f'change does not support {args[0]} command.'
    return message


@input_error
def del_handler(addressbook: AddressBook, *args) -> str:
    if args[0] == 'record':
        addressbook.del_record(args[1])
        message = f'Record with name {args[1]} was deleted from addressbook.'
    elif args[0] == 'phone':
        addressbook[args[1]].del_phone(args[2])
        message = f'Phone {args[2]} was deleted from {args[1]} record.'
    elif args[0] == 'email':
        raise NotImplementedError
    elif args[0] == 'birthday':
        raise NotImplementedError
    else:
        message = f'del does not support {args[0]} command.'
    return message


@input_error
def show_handler(addressbook: AddressBook, *args) -> str:
    addressbook.show_records()
    return 'All records are shown'


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
            'change': change_handler,
            'del': del_handler,
            'show': show_handler,
            'search': search_handler,
            'save': save_data,
            'load': load_data,
            'sort_files': sort_files}
