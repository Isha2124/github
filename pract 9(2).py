# Book class
class Book:
    def __init__(self, bid, title, author):
        self.bid = bid
        self.title = title
        self.author = author
        self.available = True


# Member class
class Member:
    def __init__(self, mid, name):
        self.mid = mid
        self.name = name


# Library class
class Library:
    def __init__(self):
        self.books = []
        self.members = []

    # Add book
    def add_book(self):
        bid = input("Enter Book ID: ")
        title = input("Enter Title: ")
        author = input("Enter Author: ")
        self.books.append(Book(bid, title, author))
        print("Book added successfully!")

    # Add member
    def add_member(self):
        mid = input("Enter Member ID: ")
        name = input("Enter Name: ")
        self.members.append(Member(mid, name))
        print("Member added!")

    # Display books
    def display_books(self):
        for b in self.books:
            status = "Available" if b.available else "Issued"
            print(b.bid, b.title, b.author, status)

    # Lend book
    def lend_book(self):
        bid = input("Enter Book ID to lend: ")
        for b in self.books:
            if b.bid == bid and b.available:
                b.available = False
                print("Book issued!")
                return
        print("Book not available!")

    # Return book
    def return_book(self):
        bid = input("Enter Book ID to return: ")
        for b in self.books:
            if b.bid == bid:
                b.available = True
                print("Book returned!")
                return
        print("Book not found!")


# Main program (menu)
lib = Library()

while True:
    print("\n1. Add Book")
    print("2. Add Member")
    print("3. Display Books")
    print("4. Lend Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        lib.add_book()
    elif choice == '2':
        lib.add_member()
    elif choice == '3':
        lib.display_books()
    elif choice == '4':
        lib.lend_book()
    elif choice == '5':
        lib.return_book()
    elif choice == '6':
        break
    else:
        print("Invalid choice!")