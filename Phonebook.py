# Creating a phonebook using a dictionary
phonebook = {
    "Alice": "123-4567",
    "Bob": "987-6543",
    "Charlie": "555-1122",
     "Bob": "999-8888"
}

# Looking up a number
print("Alice's number:", phonebook["Alice"])

# Adding a new entry
phonebook["David"] = "333-4444"


# Printing the updated phonebook
print("\nUpdated Phonebook:")
for name, number in phonebook.items():
    print(name, ":", number)
