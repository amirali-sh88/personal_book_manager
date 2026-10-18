import os
from dotenv import load_dotenv
from books import show_books, save_books, load_books

load_dotenv()

name = input("Enter your name: ")

print("Welcome to Personal Book Manager,", name)

admin_choice = input("Do you want to enter Admin Mode? (yes/no): ")

if admin_choice.lower() == "yes":
    password = input("Enter admin password: ")
    admin_password = os.getenv("BOOK_MANAGER_ADMIN_PASSWORD")

    if admin_password is not None and password == admin_password:
        print("Admin Mode activated.")
    else:
        print("Wrong password.")

books = load_books()

print("Your saved books:")
show_books(books)

number_of_books = int(input("How many new books do you want to add? "))

for i in range(number_of_books):
    book_name = input("Enter book name: ")
    books.append(book_name)

save_books(books)

print("Books saved successfully.")

show_books(books)
