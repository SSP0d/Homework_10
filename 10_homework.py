from collections import UserDict


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record


class Record:
    def __init__(self, new_name):
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
                print("Phone number doesn't exist")  

    def remove_phone(self, old_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                self.phones.remove(phone)
            else:
                print("Phone number does't exist")

    def __repr__(self) -> str:
        return f'{self.phones}'

class Field:
    pass


class Name(Field):
    def __init__(self, name) -> None:
        self.value = name


class Phone(Field):
    def __init__(self, phone) -> None:
        self.value = phone

    def __repr__(self) -> str:
        return self.value

addressbook = AddressBook()


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError as error:
            print(f'Unknown command "{error.args[0]}". Try again..')
        except TypeError:
            print(f'Wrong input. Try again..')
        except IndexError:
            print(f'invalid command syntax. Try again..')
        except ValueError as error:
            print(f'Error,{error.args[0]}. Try again...')
    return wrapper


@input_error
def get_user_input():
    user_input = input('Enter command: ').lower().split(' ')
    return user_input


@input_error
def get_handler(actions):
    return OPERATIONS[actions]


@input_error
def add_func(user_input):
    if user_input[1] not in addressbook.data:
        add_record = Record(user_input[1])
        add_record.add_phone(user_input[2])
        addressbook.add_record(add_record)
        print(f'New contact added')
    else:
        add_phone = addressbook.data[1]
        add_phone.add_phone(user_input[2])
        print(f'New phone number to {user_input[1]} has been added')


@input_error
def change_func(user_input):
    if user_input[1] in addressbook.data:
        old_phone = input('Enter phone number to change: ')
        renew_phone = addressbook.data[user_input[1]]
        renew_phone.change_phone(old_phone, user_input[2])
        print(f'Phone number has been changed')
    else:
        print(f"Phone number {user_input[2]} doesn't exist")


@input_error
def delete_func(user_input):
    if user_input[1] in addressbook.data:
        addressbook.data.pop(user_input[1])
        print(f'Contact "{user_input[1]}" has been deleted')


@input_error
def remove_phone_func(user_input):
    if user_input[1] in addressbook.data:
        removing = addressbook.data[user_input[1]]
        removing.remove_phone(user_input[2])
        print(f'Phone number "{user_input[2]}" has been removed')


@input_error
def phone_func(user_input):
    if user_input[1] in addressbook.data:
        print(f'{user_input[1]} has {addressbook.data[user_input[2]]} phone number')
    else:
        print(f"Contact '{user_input[1]}' doesn't exist")


def hello_func(*args):
    print('How can I help you?')


def show_all_func(*args):
    print(addressbook.data)


def break_func(*a):
    result = 'stop loop'
    print('Good bye!')
    return result


OPERATIONS = {
    'hello': hello_func,
    'add': add_func,
    'change': change_func,
    'phone': phone_func,
    'delete': delete_func,
    'remove': remove_phone_func,
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
        elif user_input[0] == 'show':
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
