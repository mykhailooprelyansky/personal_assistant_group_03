from collections import UserDict
from datetime import date, datetime
# from input_data import *

class AddressBook(UserDict):
    def add(self, record):
        self.data[record.name] = record
        for value in self.data.values():
            print(type(value))

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

    def editing_contact(self, name, parameter, new_value):
        pass

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



