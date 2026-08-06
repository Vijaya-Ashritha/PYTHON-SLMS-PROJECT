#------------------------------------------- SMART LIBRARY MANAGMENT SYSTEM ----------------------------------------------------

from datetime import datetime

#------------------------ LOGIN -----------------------------
username = "admin"
password = "1234"

books = []
issued_books = []

def login():
    print("\n------SMART LIBRARY MANAGEMENT SYSTEM------")

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username == username and password == password:
        print("\nLogin Successful!\n")
        return True
    else:
        print("\nInvalid Username and Password")
        return False

#------------------------ADD BOOK------------------------------
def add_book():
    book_id = input("Book ID: ")
    title = input("Book Title: ")
    author = input("Author: ")
    books.append({
        "id": book_id,
        "title": title,
        "author": author,
        "available": True
    })
    print("Book Added Successfully!")

#------------------------ VIEW BOOKS -------------------------------
def view_book():

    if len(books) == 0:
        print("No Books Available.")
        return
    print("\nBOOK LIST")

    for book in books:
        status = "Available" if book["available"] else "Issued"

        print(f"Book ID : {book['id']}")
        print(f"Title : {book['title']}")
        print(f"Author : {book['author']}")
        print(f"status : {status}")

#--------------------------- SEARCH BOOK ---------------------------------
def search_book():
    title = input("Enter Book Title: ")

    found = False

    for book in books:
        if book["title"].lower() == title.lower():
            print("\nBook Found")
            print(book)
            found = True

    if not found:
        print("Book Not Found!")

#--------------------------- ISSUED BOOK ---------------------------
def issue_book():
    book_id = input("Enter Book ID: ")

    for book in books:

        if book["id"] == book_id and book["available"]:
            student = input("Student Name: ")
            issue_date = input("Issue Date (YYYY-MM-DD): ")

            issued_books.append({
                "book_id": book_id,
                "student":student,
                "issue_date": issue_date
            })
            book["available"] = False
            print("Book Issued Successfully.")
            return

    print("Book Not Available.")

#-------------------------- RETURN BOOK ----------------------------------
def return_book():
    book_id = input("Enter Book ID: ")

    for issue in issued_books:
        if issue["book_id"] == book_id:

            return_date = input("Return Date (YYYY-MM-DD): ")
            issued_date = datetime.strptime(issue["issue_date"],"%Y-%m-%d")
            return_date = datetime.strptime(return_date,"%Y-%m-%d")

            days = (return_date - issued_date).days

            fine = 0

            if days > 7:
                fine = (days - 7)*5
            print("Total Days: ", days)
            print("Fine: ", fine)

            issued_books.remove(issue)

            for book in books:
                if book["id"] == book_id:
                    book["available"] = True

            print("Book Returned Successfully!")
            return
        print("Book Record Not Found.")

#---------------------------- DELETE BOOK --------------------------------
def delete_book():
    book_id = input("Enter Book ID: ")

    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            print("Book Deleted Successfully!")
            return
    print("Book Not Found.")

#------------------------------ MENU ----------------------------------
def menu():
    while True:
        print("\n======MENU======")
        print("1. Add Book")
        print("2. View Book")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Delete Book")
        print("7. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_book()
        elif choice == "3":
            search_book()
        elif choice == "4":
            issue_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            delete_book()
        elif choice == "7":
            print("Thank You")
            break
        else:
            print("Invalid Choice")

if login():
    menu()
