from datetime import date, datetime
import re
from Address_book import *
#from sorting import *


class Name:
    def __init__(self, value):
        self.value = value

    def __getitem__(self):
        return self.value


class Phone:
    def __init__(self):
        while True:
            self.values = []
            self.value = input("Enter phones with code: +38 plus 10 numbers after:")
            try:
                for number in self.value.split(' '):
                    if re.match('^\\+38\d{10}$', number):
                        self.values.append(number)
                    else:
                        raise ValueError
            except ValueError:
                print('Incorrect phone number!')
            else:
                break

    def __getitem__(self):
        return self.values


class Address:
    def __init__(self, value=""):
        self.value = value

    def __getitem__(self):
        return self.value


class Birthday:
    def __init__(self, value=''):
        while True:
            if value:
                self.value = value
            else:
                self.value = input("Birthday date in format (dd/mm/yyyy) : ")
            try:
                if re.match('^\d{2}/\d{2}/\d{4}$', self.value):
                    self.value = datetime.strptime(self.value, "%d/%m/%Y")
                    break
                elif self.value == '':
                    break
                else:
                    raise ValueError
            except ValueError:
                print('Incorrect date! Please provide correct date format.')

    def __getitem__(self):
        return self.value


class Email:
    def __init__(self, value=''):
        while True:
            if value:
                self.value = value
            else:
                self.value = input("Email: ")
            try:
                if re.match('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', self.value):
                    break
                else:
                    raise ValueError
            except ValueError:
                print('Incorrect email! Please enter right email.')

    def __getitem__(self):
        return self.value


class Record:
    def __init__(self, name="", phones='', address='', birthday='', email=''):
        self.name = name
        self.phones = phones
        self.address = address
        self.birthday = birthday
        self.email = email

    def __str__(self):
        return (f"Contact name: {self.name},\nphones: {self.phones},\n"
                f"email: {self.email},\nbirthday: {self.birthday},\naddress: {self.address}")


class Bot:
    def __init__(self):
        self.book = AddressBook()

    def handle(self, action):
        if action == 'add':
            name = Name(input("Name: ")).value.strip()
            phones = Phone().value
            birthday = Birthday().value
            email = Email().value.strip()
            address = Address(input("Address: ")).value.strip()
            record = Record(name, phones, address, birthday, email)
            print(record)
            return self.book.add(record)
        elif action == 'search':
            pattern = input('Enter Search pattern: ')
            result = self.book.search_by_match(pattern)
            if result:
                for item in result:
                    print(item)
            else:
                print("There is no such Contact name!")
        elif action == 'edit':
            contact_name = input('Contact name: ')
            parameter = input('Which parameter to edit(name, phones, birthday, address, email): ').strip()
            return self.book.editing_contact(contact_name, parameter)
        elif action == 'remove':
            contact_name = input('Contact name: ')
            return self.book.delete(contact_name)
        elif action == 'save':
            file_name = input("File name: ")
            return self.book.save(file_name)
        elif action == 'load':
            file_name = input("File name: ")
            return self.book.load(file_name)
        elif action == 'birthdays':
            days = input("Enter the number of days until Birthday: ")
            print(self.book.list_contacts_with_day_of_birthday(days))
        elif action == 'view':
            print(self.book)
        elif action == 'sort':
            sorting = FileSorter()
        elif action == 'exit':
            pass
        else:
            print("There is no such command!")


def main():
    command = ""
    bot = Bot()
    bot.book.load("auto_save")
    commands_help = ['Add', 'Search', 'Edit', 'Load', 'Remove', 'Save', 'Birthdays', 'View', 'Notes', 'Sort', 'Exit']
    while True:
        command = input("Enter your command or the command Help to see a list of commands: ").lower()
        if command == 'help':
            format_str = str('{:%s%d}' % ('^', 20))
            for command in commands_help:
                print(format_str.format(command))
            command = input().strip().lower()
            bot.handle(command)
            if command in ['add', 'remove', 'edit']:
                bot.book.save("auto_save")
        else:
            bot.handle(command)
            if command in ['add', 'remove', 'edit']:
                bot.book.save("auto_save")
        if command == 'exit':
            print("Good bay")
            break


if __name__ == '__main__':
    main()

