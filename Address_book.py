from collections import UserDict
from datetime import date, datetime
import pickle
import os
from main import *


class AddressBook(UserDict):
    def add(self, record):
        self.data[record.name] = record

    def list_contacts_with_day_of_birthday(self, days):
        list_contacts = []
        for value in self.data.values():
            if value.birthday:
                if self.days_to_birthday(value.birthday) == days:
                    list_contacts.append(value)
        return list_contacts

    def days_to_birthday(self, bday):
            current_day = date.today()
            if bday.month < current_day.month:
                year_of_future_birthday = current_day.year + 1
            else:
                year_of_future_birthday = current_day.year
            date_of_future_birthday = date(year=year_of_future_birthday, month=bday.month,
                                           day=bday.day)
            days_count = date_of_future_birthday - current_day
            return days_count.days

    def find(self, name, number_phone, email, date_birthday):
        for key, value in self.data.items():
            if key == name:
                return value
            if value.phones == number_phone:
                return value
            if value.email == email:
                return value
            if value.birthday == date_birthday:
                return value

    def editing_contact(self, name, parameter):
        try:
            if name not in self.data.keys():
                raise NameError
            for account, value in self.data.items():
                if account == name:
                    if parameter == 'name':
                        value.name = Name(input("Name: ")).value.strip()
                        #account = value.name
                    elif parameter == 'birthday':
                        value.birthday = Birthday().value
                    elif parameter == 'email':
                        value.email = Email().value
                    elif parameter == 'address':
                        value.address = Address(input("New address: ")).value.strip()
                    elif parameter == 'phones':
                        value.phones = Phone().value
                    else:
                        raise ValueError

        except ValueError:
            print('Incorrect parameter! Please provide correct parameter')
        except NameError:
            print('There is no such contact in address book!')
        else:
            return True
        return False

    def delete(self, name):
        if name in self.data:
            self.data.pop(name)

    def search_by_match(self, match):
        list_serched_contact = []
        list_str_cont = [str(it) for it in self.data.values()]
        for st in list_str_cont:
            if st.lower().find(match.lower()) != -1:
                list_serched_contact.append(st)
        return list_serched_contact

    def __getstate__(self):
        attributes = self.__dict__.copy()
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value

    def __str__(self):
        result = []
        for account, value in self.data.items():
            #print(value)
            result.append(
                "_" * 30 + "\n" + f"Name: {value.name} \nPhones: {value.phones} \nBirthday: {value.birthday.strftime('%d/%m/%Y')} \nEmail: {value.email}\nAddress: {value.address}\n")
        return '\n'.join(result)

    def save(self, file_name):
        with open(file_name + '.bin', 'wb') as file:
            pickle.dump(self.data, file)

    def load(self, file_name):
        emptyness = os.stat(file_name + '.bin')
        if emptyness.st_size != 0:
            with open(file_name + '.bin', 'rb') as file:
                self.data = pickle.load(file)
        else:
            pass
        return self.data



