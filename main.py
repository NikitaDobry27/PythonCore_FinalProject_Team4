from command_handlers import function
from addressbook import AddressBook


def command_parser(addressbook: AddressBook, input_string) -> str:
    input_string = input_string.strip().lstrip()
    command = input_string.split()[0].lower()
    arguments = input_string.split()[1:]
    if command in function:
        message = function[command](addressbook, *arguments)
    elif input_string.lower() in ('good bye', 'exit', 'close', 'bye', '.'):
        message = '\nGood bye!\n'
    else:
        message = f'\nCommand {command} does not exist!\n'
    return message


def main() -> None:
    print('\nType "help" for list of commands.\n')
    my_address_book = AddressBook()
    my_address_book.read_records_from_file('storage1.dat')

    while True:
        input_string = input('Enter Command: ')

        if not len(input_string):
            continue
        message = command_parser(my_address_book, input_string)
        print(message)
        if message == '\nGood bye!\n':
            break


if __name__ == '__main__':
    main()
