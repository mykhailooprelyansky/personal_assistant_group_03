from datetime import date, datetime
import re
from addres_book import *

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
    def __init__(self, value):
        self.value = value

    def __getitem__(self):
        return self.value


class Birthday:
    def __init__(self, value=''):
        while True:
            if value:
                self.value = value
            else:
                self.value = input("Birthday date in format: day/month/year: ")
            try:
                if re.match('^\d{2}/\d{2}/\d{2}$', self.value):
                    self.value = datetime.strptime(self.value, "%d/%m/%y")
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
                f"email: {self.email},\nbirthday: {self.birthday}")


book = AddressBook()

def test():
    name = Name(input("Name: ")).value
    phones = Phone().value
    address = Address(input("Enter address: ")).value
    birth = Birthday().value
    email = Email().value
    record = Record(name, phones, address, birth, email)
    return book.add(record)

if __name__ == '__main__':
    test()