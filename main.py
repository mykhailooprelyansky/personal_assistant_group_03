
from collections import UserDict
from datetime import date, datetime
import pickle


class Field:
    def __init__(self, value):
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    def __str__(self):
        return str(self.value)

    @value.setter
    def value(self, value):
        self.__value = value


class Name(Field):
    def __init__(self, name):
        super().__init__(name)


class Phone(Field):
    def __init__(self, value):
        if len(value) == 10 and value.isdigit():
            super().__init__(value)
        else:
            raise ValueError("Uncorrect number")


class Birthday(Field):
    def __init__(self, value):
        self.__value = value
        if value is not None:
            if self.validate():
                super().__init__(value)
            else:
                raise ValueError("Uncorrect date, must will be enter date in format: day/month/year")
        else:
            super().__init__(None)

    def validate(self):
        try:
            datetime.strptime(self.__value, '%d/%m/%y')
        except ValueError:
            return False
        else:
            return True


class Record:
    def __init__(self, name, dates=None):
        self.name = Name(name)
        self.date_of_birthday = Birthday(dates).value
        self.phones = []

    def add_phone(self, number):
        self.phones.append(Phone(number))

    def remove_phone(self, number):
        for phone in self.phones:
            if phone.value == number:
                self.phones.remove(phone)
        else:
            return None

    def edit_phone(self, old_number, new_number):
        for phone in self.phones:
            if phone.value == old_number:
                self.phones.remove(phone)
                self.phones.append(Phone(new_number))
                self.phones.reverse()
                break
        else:
            raise ValueError

    def find_phone(self, number):
        for phone in self.phones:
            if phone.value == number:
                return phone
        else:
            return None

    def days_to_birthday(self):
        if self.date_of_birthday is not None:
            birthday = datetime.strptime(self.date_of_birthday, '%d/%m/%y')
            current_day = date.today()
            if birthday.month < current_day.month:
                year_of_future_birthday = current_day.year + 1
            else:
                year_of_future_birthday = current_day.year
            date_of_future_birthday = date(year=year_of_future_birthday, month=birthday.month, day=birthday.day)
            days_count = date_of_future_birthday - current_day
            return days_count.days
        else:
            return None

    def __str__(self):
        return (f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, "
                f"days to birthday: {self.days_to_birthday()}")


class AddressBook(UserDict):

    # def add_record(self, records):
    #     self.data[records.name.value] = records

    def add_record(self, book_record):
        phone_list = self.data.get(book_record.name.value, [])
        for phone in book_record.phones:
            phone_list.append(phone)
        self.data[book_record.name.value] = phone_list

    # def find(self, name):
    #     for key, value in self.data.items():
    #         if key == name:
    #             return value

    def find(self, find_name):
        phones = self.data.get(find_name, None)
        if phones:
            f_record = Record(find_name)
            f_record.name.value = find_name
            f_record.phones = phones
            return f_record
        return None

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

    def iterator(self):

        return Iterator(list(self.data.values()))


class Iterator:
    def __init__(self, address_book):
        self.address_book = address_book

    def __iter__(self):
        self.N = 2
        self.current_count_N = 0
        self.idx = 0
        return self

    def __next__(self):
        if self.current_count_N >= self.N:
            raise StopIteration
        else:
            value = self.address_book[self.idx]
            self.idx += 1
            self.current_count_N += 1
            return value


def create_book():
    book = AddressBook()


def rec_add_phone(args):
    record = Record(args[1])
    record.add_phone(args[2])
    book.add_record(record)


def rec_remove_phone(args):
    record = Record(args[1])
    record.remove_phone(args[2])


OPERATIONS = {
        'add_phone': rec_add_phone,
        'rem_phone': rec_remove_phone,
        # 'show': show_all_func,
    }


def get_handler(args):
    return OPERATIONS[args[0]]


def main():
    cmd_exit = ["good bye", "close", "exit"]
    command = ""

    while True:
        command = input("Enter command: ")
        if command in cmd_exit:
            break
        args = command.split()
        get_handler(args)(args)
        print(book.find(args[1]).__str__())

    print("Good bay")


if __name__ == '__main__':
    book = AddressBook()
    main()

# book = AddressBook()
#
# john_record = Record("John", "21/11/95")
# john_record.add_phone("1234567890")
# john_record.add_phone("5555555555")
# book.add_record(john_record)
#
# jane_record = Record("Jane", "11/3/96")
# jane_record.add_phone("9876543210")
# book.add_record(jane_record)
#
# misha_record = Record("Misha", "24/8/94")
# misha_record.add_phone("9876543210")
# book.add_record(misha_record)
#
# for i in book.iterator():
#     print(i)
#
# john = book.find("John")
# john.edit_phone("1234567890", "1112223333")
#
# print(john)
#
# found_phone = john.find_phone("5555555555")
# print(f"{john.name.value}: {found_phone.value}")
#
# book.delete("Jane")
#
# for i in book.iterator():
#     print(i)
#
# searching = book.search_by_match("765")
# print(searching)
#
# with open("address_book.bin", "wb") as file:
#     pickle.dump(book, file)
#
# with open("address_book.bin", "rb") as file:
#     content = pickle.load(file)
#     print(f"loading_address_book:{content}")