from collections import UserDict


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record


class Record:
    def __init__(self, new_name) -> None:
        self.name = Name(new_name)
        self.phones = []

    def add_phone(self, new_phone):
        self.phones.append(Phone(new_phone))

    def change_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                self.phones.append(Phone(new_phone))
                self.phones.remove(phone)
            else:
                print("Phone number does't exist")

    def remove_phone(self, old_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                self.phones.remove(phone)
            else:
                print("Phone number does't exist")

class Field:
    pass


class Name(Field):
    def __init__(self, name) -> None:
        self.value = name


class Phone(Field):
    def __init__(self, phone) -> None:
        self.value = phone

# DEFAULT_DICT = {}
addressbook = AddressBook()


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError as error:
            print(f'Unknown command "{error.args[0]}". Try again..')
        except TypeError:
            print(f'WrongD input. Try again..')
        except IndexError:
            print(f'invalid command syntax. Try again..')
        except ValueError as error:
            print(f'Error,{error.args[0]}. Try again...')
    return wrapper


def hello_func(user_input):
    print('How can I help you?')


def show_all_func(user_input):
    print(addressbook.data)


@input_error
def get_user_input():
    user_input = input('Enter command: ').lower().split(' ')
    return user_input


@input_error
def get_handler(actions):
    return OPERATIONS[actions]


@input_error
def add_func(user_input):
    addressbook.data[user_input[1]] = int(user_input[2])
    print(f'New contact added')


@input_error
def change_func(user_input):
    addressbook.data[user_input[1]] = int(user_input[2])
    print(f'Phone number has been changed')


@input_error
def phone_func(user_input):
    print(addressbook.data[user_input[1]])


def break_func(user_input):
    result = 'stop loop'
    print('Good bye!')
    return result


OPERATIONS = {
    'hello': hello_func,
    'add': add_func,
    'change': change_func,
    'phone': phone_func,
    'show all': show_all_func,
    'good bye': break_func,
    'close': break_func,
    'exit': break_func
}

# @input_error


def main():

    while True:
        user_input = get_user_input()

        if user_input == ['']:
            continue
        elif user_input[0] in 'show':
            actions = 'show all'
        else:
            actions = user_input[0]

        handler = get_handler(actions)
        if handler is None:
            continue

        result = handler(user_input)
        if result == 'stop loop':
            break


if __name__ == '__main__':
    main()
