
import json


def show_books(books):
    print("Your books:")

    if len(books) == 0:
        print("No books found.")
    else:
        for book in books:
            print("Book:", book["name"])
            print("Priority:", book["priority"])
            print("--------------------")

def display_books(books):
    if not books:
        print("No books found.")
    else:
        for book in books:
            print(f"Book Name: {book['name']}")
            print(f"Book Priority: {book['priority'].upper()}")
            print("------------------------------")



def save_books(books):
    with open("books.json", "w", encoding="utf-8") as file:
        json.dump(books, file, ensure_ascii=False, indent=4)


def load_books():
    try:
        with open("books.json", "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

