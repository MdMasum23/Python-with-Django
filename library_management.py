# Library Management System

# Starting book collection
books = ["1984", "Python Basics", "Harry Potter", "Rich Dad Poor Dad"]

# List to track borrowed books
borrowed = []

# Show all books
def show_books():
    print("\n📚 Available Books:")
    for book in books:
        print(f"- {book}")
    print()

# Borrow a book
def borrow_book():
    name = input("Enter the name of the book you want to borrow: ")
    if name in books:
        books.remove(name)
        borrowed.append(name)
        print(f"✅ You have borrowed '{name}'.\n")
    else:
        print("❌ Sorry, that book is not available or already borrowed.\n")

# Return a book
def return_book():
    name = input("Enter the name of the book you want to return: ")
    if name in borrowed:
        borrowed.remove(name)
        books.append(name)
        print(f"✅ You have returned '{name}'.\n")
    else:
        print("❌ This book was not borrowed from us.\n")

# Add a book
def add_book():
    name = input("Enter the name of the new book: ")
    books.append(name)
    print(f"✅ '{name}' has been added to the library.\n")

# Main menu
def menu():
    while True:
        print("====== LIBRARY MENU ======")
        print("1. Show Available Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Add Book")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            show_books()
        elif choice == "2":
            borrow_book()
        elif choice == "3":
            return_book()
        elif choice == "4":
            add_book()
        elif choice == "5":
            print("👋 Thank you for using the library!")
            break
        else:
            print("⚠️ Invalid choice. Please choose between 1-5.\n")

# Start the system
menu()
