

print("hello world")

while book_choice is None:
    try:
        book_choice = int(input(">>> "))
    except ValueError:
        if book_choice != int:
            print("Invalid input; enter a valid number")
        elif book_choice <= 0:
            print("Number must be > 0")
        elif book_choice > len(books):
            print("Invalid book number")