from books import show_books, save_books, load_books

name = input("Enter your name: ")

print("Welcome to Personal Book Manager,", name)

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