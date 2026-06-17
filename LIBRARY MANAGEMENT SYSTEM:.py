# LIBRARY MANAGEMENT SYSTEM: 

from datetime import datetime                          # how to know today's date.

def load_book():
    with open("books.txt", "r") as f:
        available_books = f.readlines()
    with open("issued_book.txt", "r") as f:
        borrowed_books = f.readlines()
    return available_books, borrowed_books

def save_books(available_books, borrowed_books):  
    with open("books.txt", "w") as f:
        f.writelines(available_books)                
    with open("issued_book.txt", "w") as f:
        f.writelines(borrowed_books)

def add_book(available_books, borrowed_books):     
    new_book = input("Add book: ")

    available_books.append(new_book + "\n")
    save_books(available_books, borrowed_books)
    print("New book added successfully.✅")

def issue_book(available_books, borrowed_books):   
    borrower = input("Borrower Name: ")
    book_name = input("Issue Book: ").strip()            # kept the original input
    date = datetime.now().strftime("%d-%m-%Y")           # today's date in formate
    found = False                                        # flag to limit the no. of 'not available to issue' messages
    for book in available_books:
        if book_name.lower() == book.strip().lower():    # Then compare using .lower():
            record = f"{book.strip()}|{borrower}|{date}\n"       # record formate
            found = True
            available_books.remove(book)
            borrowed_books.append(record)                # stores the record with the above formate
            save_books(available_books, borrowed_books)
            print("Book Issued. ✅")
            break
    if not found:
        print("Not Available to Issue!")

def return_book(available_books, borrowed_books):  
    book_name = input("Return book: ").strip()
    found = False                                          # added flag to track if book found
    for record in borrowed_books:                         # iterate through records to find borrower and date
        parts = record.split("|")
        if book_name.lower() == parts[0].lower():          # logic to check if book matches
            
            title = parts[0]
            borrowed_books.remove(record)
            available_books.append(title + "\n")           # not 'book', since only book_name is to add in available_books file
            save_books(available_books, borrowed_books)
            print("Book returned. ✅")
            found = True
            break

    if not found:
        print("Book was not borrowed.")

def search_book(available_books):
    key_word = input("Search book: ").strip().lower()         
    found = False
    for book in available_books: 
        if key_word in book.lower():
            print("📔", book.strip())
            found = True
    if not found:
        print("Book Not Found!")
            
def display_book(available_books):
    print("\n📚 Available Books:\n")
    for index, book in enumerate(available_books, start = 1):
            print(f"{index}. {book.strip()}")

def menu():
    print("\n1. Add Book \n2. Issue Book \n3. Return Book \n4. Search Book \n5. Display Books \n6. Exit")
    return input("\nOption: ")

def main():
    available_books, borrowed_books = load_book()
    while True:
        option = menu()
        if option == "1":
            add_book(available_books, borrowed_books)
        elif option == "2":
            issue_book(available_books, borrowed_books)
        elif option == "3":
            return_book(available_books, borrowed_books)
        elif option == "4":
            search_book(available_books)
        elif option == "5":
            display_book(available_books)
        else:
            break

if __name__ == "__main__":
    main()
