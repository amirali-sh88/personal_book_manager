name = input("Enter your name: ")

print("Welcome to Personal Book Manager,", name)

books = []

number_of_books = int(input("How many books do you want to add? "))

for i in range(number_of_books):
    book_name = input("Enter book name: ")
    books.append(book_name)

print("Your books:")

for book in books:
    print(book)