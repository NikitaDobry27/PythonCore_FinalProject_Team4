from command_handlers import function
from addressbook import AddressBook


def command_parser(addressbook: AddressBook, input_string) -> str:
    input_string = input_string.strip().lstrip()
    command = input_string.split()[0].lower()
    arguments = input_string.split()[1:]
    print(f'Command: {command}, Arguments: {arguments}')  # Debug message
    if command in function:
        message = function[command](addressbook, *arguments)
    elif input_string.lower() in ('good bye', 'exit', 'close'):
        message = 'Good bye!'
    else:
        message = f'Command {command} does not exist!'
    return message


def main() -> None:
    print('Type "help" for list of commands.')
#     my_address_book = AddressBook()

    while True:
        input_string = input('Enter Command: ')
        if not len(input_string):
            continue
        message = command_parser(my_address_book, input_string)
        print(message)
        if message == 'Good bye!':
            break


if __name__ == '__main__':
    my_address_book = AddressBook()
    
    my_address_book.add_record("Alexander")                         # Создаем контакт
    my_address_book["Alexander"].add_phone('111111111')             # Добавляем к контакту 1 номер
    my_address_book["Alexander"].add_phone('111111112')             # Добавляем к контакту 2 номер
    my_address_book["Alexander"].add_phone('111111113')             # Добавляем к контакту 3 номер
    my_address_book["Alexander"].set_birthday('30-05-2020')         # Добавляем к контакту день рождения
    my_address_book["Alexander"].set_email('abcdef@gmail.com')      # Добавляем к контакту емеил
    
    my_address_book.add_record("Hiba")                         # Создаем контакт
    my_address_book["Hiba"].add_phone('111111111')             # Добавляем к контакту 1 номер
    my_address_book["Hiba"].add_phone('111111112')             # Добавляем к контакту 2 номер
    my_address_book["Hiba"].add_phone('111111113')             # Добавляем к контакту 3 номер
    my_address_book["Hiba"].set_birthday('29-05-2002')         # Добавляем к контакту день рождения
    my_address_book["Hiba"].set_email('abcdef@gmail.com')      # Добавляем к контакту емеил

    my_address_book.add_record("Abud")                         # Создаем контакт
    my_address_book["Abud"].add_phone('111111111')             # Добавляем к контакту 1 номер
    my_address_book["Abud"].add_phone('111111112')             # Добавляем к контакту 2 номер
    my_address_book["Abud"].add_phone('111111113')             # Добавляем к контакту 3 номер
    my_address_book["Abud"].set_birthday('28-05-1995')         # Добавляем к контакту день рождения
    my_address_book["Abud"].set_email('abcdef@gmail.com')      # Добавляем к контакту емеил

    my_address_book.add_record("Jakub")                         # Создаем контакт
    my_address_book["Jakub"].add_phone('111111111')             # Добавляем к контакту 1 номер
    my_address_book["Jakub"].add_phone('111111112')             # Добавляем к контакту 2 номер
    my_address_book["Jakub"].add_phone('111111113')             # Добавляем к контакту 3 номер
    my_address_book["Jakub"].set_birthday('28-05-1995')         # Добавляем к контакту день рождения
    my_address_book["Jakub"].set_email('abcdef@gmail.com')      # Добавляем к контакту емеил
    
    main()
