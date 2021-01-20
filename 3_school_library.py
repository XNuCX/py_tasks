def add_book(old_shelf, book):
    old_shelf.insert(0, book)
    return old_shelf


def take_book(old_shelf, book):
    while book in old_shelf:
        old_shelf.remove(book)
    return old_shelf


def swap_books(old_shelf, book, book2):
    first_book_index = 0
    second_book_index = 0
    if book in old_shelf and book2 in old_shelf:
        for index, name in enumerate(old_shelf):
            if name == book:
                first_book_index = index
            if name == book2:
                second_book_index = index
        old_shelf[first_book_index], old_shelf[second_book_index] = old_shelf[second_book_index], \
                                                                    old_shelf[first_book_index]
        return old_shelf
    else:
        return old_shelf


def insert_books(old_shelf, book):
    old_shelf.append(book)
    return old_shelf


def check_book(old_shelf, index):
    name = old_shelf[index]
    return name


shelf_with_books = input().split("&")
act = ""
book_1 = ""
book_2 = ""
command = ""
while True:
    command = input()
    if command == "Done":
        break
    command = command.split(" | ")
    act = command[0]
    book_1 = command[1]
    if len(command) == 3:
        book_2 = command[2]
    if book_1 in shelf_with_books:
        pass

    if act == "Add Book":
        if book_1 not in shelf_with_books:
            shelf_with_books = add_book(shelf_with_books, book_1)
        else:
            continue

    elif act == "Take Book":
        if book_1 in shelf_with_books:
            shelf_with_books = take_book(shelf_with_books, book_1)
        else:
            continue

    elif act == "Swap Books":
        shelf_with_books = swap_books(shelf_with_books, book_1, book_2)
    elif act == "Insert Book":
        shelf_with_books = insert_books(shelf_with_books, book_1)

    elif act == "Check Book":
        if book_1.isdigit():
            if int(book_1) in range(len(shelf_with_books)):
                name_book = check_book(shelf_with_books, int(book_1))
                print(name_book)
            else:
                continue
        else:
            continue

print(f"{', '.join(shelf_with_books)}")
