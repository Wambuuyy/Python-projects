#!/usr/bin/env python3
import json

def add_person():
    name = input("Name: ")
    age = input("Age: ")
    email = input("Email: ")

    person = {"name": name, "age": age, "email": email}
    return person

def display_people(people):
    for i, person in enumerate(people):
        print(i + 1, "-", person["name"], "|", person["age"], "|", person["email"])

def delete_contact(people):
    display_people(people)
    while True:
        number = input("Enter a number to delete: ")
        try:
            number = int(number)
            if number <= 0 or number > len(people):
                print("Invalid number, out of range.")
            else:
                break
        except:
            print("invalid number")
    people.pop(number - 1)
    print()

def search(people):
    search_name = input("serch for a name; ").lower()
    results = []

    for person in people:
        name = person["name"]
        if search_name in name.lower():
            results.append(person)
        display_people(results)


print("Hi, welcome to the contact Management System.")
print()

with open("contacts.json", "r") as f:
    people = json.load(f)["contacts"]

while True:
    print("Contact list size:", len(people))
    command = input("You can 'Add', 'Delete' or 'Search' or 'q' to quit: ").lower()

    
    if command == "add":
        person = add_person()
        people.append(person)
    elif command == "delete":
        delete_contact(people)
    elif command == "search":
        search(people)
    elif command == "q":
        break
    else:
        print("Invalid input")

with open("contacts.json", "w") as f:
    people = json.dump({"contacts": people}, f)