import pickle
from random import randint as rai
import time

phone_book = [
              {"name": "Petr", "surname": "Petrov", "age": 50, "phone_number":"+380501234567","skype": "222"},
              {"name": "Ivan", "surname": "Ivanov", "age": 15, "phone_number":"+380507654321","skype": "111"},
             ]

def print_entry(number, entry):
    print ("--[ %s ]--------------------------" % number)
    print ("| Surname:       %20s |" % entry["surname"])
    print ("| Name:          %20s |" % entry["name"])
    print ("| Age:           %20s |" % entry["age"])
    print ("| Phone number:  %20s |" % entry["phone_number"])
    print ("| skype:         %20s |" % entry["skype"])
    print ()


def add_skype(name):
    found = False
    for keys in phone_book:
        if keys["name"] == name:
            print("Entry found!")
            skype = str(input("    Enter skype name: "))
            time.sleep(0.5)
            print("Processing...")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(3)
            print("Connecting to Skype service...")
            s=rai(0,1)
            if s==1:
                time.sleep(5)
                print(".")
                time.sleep(0.5)
                print(".")
                time.sleep(0.5)
                print(".")
                time.sleep(1)
                print("No connection to skype service!")
                time.sleep(1)
                found = True
                break
            else:
                time.sleep(3)
                print(".")
                time.sleep(0.5)
                print(".")
                time.sleep(0.5)
                print(".")
                time.sleep(2)
                print("Add success")
                time.sleep(1)
                keys["skype"] = skype
                found = True
    if not found:
        printInfo("Name not found!")


def find_skype_name_phonebook(skype):
    idx = 1
    found = False
    for entry in phone_book:
        if entry["skype"] == skype:
            print_entry(idx, entry)
            idx += 1
            found = True
    if not found:
        printError("Not found!!")

def print_phonebook():
    print ()
    print ()
    print ("#########  Phone book  ##########")
    print ()

    number = 1
    for entry in phone_book:
        print_entry(number, entry)
        number += 1

def print_phonebook_by_age():
    for entry in sorted(phone_book, key=lambda entry: entry['age']):
        print(entry)



def add_entry_phonebook(surname, name, age):
    entry = {}
    entry["surname"] = surname
    entry["name"] = name
    entry["age"] = age
    phone_book.append(entry)

def printError(message):
    print ("ERROR: %s" % message)

def printInfo(message):
    print ("INFO: %s" % message)

def find_entry_name_phonebook(name):
    idx = 1
    found = False
    for entry in phone_book:
        if entry["name"] == name:
            print_entry(idx, entry)
            idx += 1
            found = True
    if not found:
        printError("Not found!!")


def find_entry_phone_phonebook(phone_number):
    idx = 1
    found = False
    for entry in phone_book:
        if entry["phone_number"] == phone_number:
            print_entry(idx, entry)
            idx += 1
            found = True
    if not found:
        printError("Not found!!")

def find_entry_age_phonebook(age):
    idx = 1
    found = False
    for entry in phone_book:
        if entry["age"] == age:
            print_entry(idx, entry)
            idx += 1
            found = True
    if not found:
        printError("Not found!!")

def delete_entry_name_phonebook(name):
    found = False
    for entry in phone_book:
        if entry["name"] == name:
            print("Starting annihilation of %s" %[entry["name"]])
            time.sleep(3)
            print("Refreshing...")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            phone_book.remove(entry)
            print("Done!")
            found = True
    if not found:
        printError("Not found!!")

def count_all_entries_in_phonebook():
    print ("Total number of entries: ", len(phone_book))

def print_avr_age():
    sum = 0
    for entry in phone_book:
        year = entry["age"]
        sum += year
    avg_age = sum // len(phone_book)
    print('Average age is :', (avg_age))

def increase_age(number_of_years):
    for entry in phone_book:
        entry["age"]+=number_of_years

def save_to_file():
    pickle.dump(phone_book, open("phone_book.save", "wb"))
    printInfo("Phonebook is saved into 'phone_book.save'")


def load_from_file():
    global phone_book
    phone_book = pickle.load(open("phone_book.save", "rb"))
    printInfo("Phonebook is loaded from 'phone_book.save'")


def main():
    while True:
        user_input = ""
        try:
            print ()
            print ()
            print ()
            print ("~ Welcome to phonebook ~")
            print ("Select one of actions below:")
            print ("     1 - Print phonebook entries")
            print ("     2 - Print phonebook entries (by age)")
            print ("     3 - Add new entry")
            print ("     4 - Find entry by name")
            print ("     5 - Find entry by age")
            print ("     6 - Delete entry by name")
            print ("     7 - The number of entries in the phonebook")
            print ("     8 - Avr. age of all persons")
            print ("     9 - Increase age by num. of years")
            print ("    10 - find phone number")
            print ("    11 - Add skype")
            print ("    12 - Find entry by skype")
            print ("-----------------------------")
            print ("     s - Save to file")
            print ("     l - Load from file")
            print ("     0 - Exit")

            user_input = input("Enter you choice: ")
            choice = int(user_input)

            if choice == 1:
                print_phonebook()
            elif choice == 2:
                print_phonebook_by_age()
            elif choice == 3:
                surname = str(input("    Enter surname: "))
                name = str(input("    Enter name: "))
                age = int(input("    Enter age: "))
                add_entry_phonebook(surname, name, age)
            elif choice == 4:
                name = str(input("    Enter name: "))
                find_entry_name_phonebook(name)
            elif choice == 5:
                age = int(input("    Enter age: "))
                find_entry_age_phonebook(age)
            elif choice == 6:
                name = str(input("    Enter name: "))
                delete_entry_name_phonebook(name)
            elif choice == 7:
                count_all_entries_in_phonebook()
            elif choice == 8:
                print_avr_age()
            elif choice == 9:
                nmbrs_of_years = int(input("    Enter number of years to add to current ages: "))
                increase_age(nmbrs_of_years)
            elif choice == 10:
                phone_number = input("    Enter phone number in full format(Ex. +380671234567): ")
                find_entry_phone_phonebook(phone_number)
            elif choice == 11:
                name = str(input("    Enter name: "))
                add_skype(name)
            elif choice == 12:
                name = str(input("    Enter Skype name: "))
                find_skype_name_phonebook(name)
            elif choice == 0:
                print ("Bye!")
                break
            else:
                print ("Enter action within range [0..9]")

        except ValueError:
            if str(user_input) == 's':
                save_to_file()
            elif str(user_input) == 'l':
                load_from_file()
            else:
                printError("Something went wrong. Try again...")


if __name__ == '__main__':
    main()