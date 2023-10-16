from collections import UserDict
# from input_data import *

class AddressBook(UserDict):
    def add(self, record):
        self.data[record.name] = record



book = AddressBook()

# print(book.add_record)

    # def list_contacts_with_day_of_birthday(self):
    #     pass
    #
    # def find(self, name, number_phone, email, date_birthday):
    #     for key, value in self.data.items():
    #         if key == name:
    #             return value
    #
    # def editing_a_contact(self, parameter):
    #     pass
    #
    # # def delete(self, name):
    # #     if name in self.data:
    # #         self.data.pop(name)
    #
    # def search_by_match(self, match):
    #     list_serched_contact = []
    #     list_str_cont = [str(it) for it in self.data.values()]
    #     for st in list_str_cont:
    #         if st.lower().find(match.lower()) != -1:
    #             list_serched_contact.append(st)
    #     return list_serched_contact
    #
    # def __getstate__(self):
    #     attributes = self.__dict__.copy()
    #     return attributes
    #
    # def __setstate__(self, value):
    #     self.__dict__ = value



