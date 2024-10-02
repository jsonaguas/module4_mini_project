class Book:
    def __init__(self, title, author, genre, publication_date, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.publication_date = publication_date    
        self.available = True

    def is_available(self):
        if self.available:
            return True
        else:
            return False
    
def add_book(library):
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    genre = input("Enter the genre of the book: ")
    publication_date = input("Enter the publication date of the book: ")
    isbn = input("Enter the ISBN of the book: ")
    library[isbn]= Book(title, author, genre, publication_date, isbn)
    

def check_out(library, isbn, user):
    if library[isbn].is_available():
        library[isbn].available = False
        print(f"{library[isbn].title} has been checked out.")
        user.loan_book(library[isbn])

def return_book(library,isbn):
    if not library[isbn].is_available():
        library[isbn].available = True
        print(f"{library[isbn].title} has been returned.")



class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.loaned_books = []

    def loan_book(self, book):
        self.loaned_books.append(book)
        print(f"{book.title} has been loaned to {self.name}.")
    
    def get_user_details(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.id}")
        print("Loaned Books:")
        for book in self.loaned_books:
            print(f"ISBN: {book.isbn}")




class Author:
    def __init__(self, name):
        self.name = name
        self.biography = None
def add_author(authors):
    name = input("Enter the name of the author: ")
    biography = input("Enter the biography of the author: ")
    authors[name] = Author(name, biography)
def display_author(writer, authors):
    for author in authors.values():
        if author.name == writer:
            print(f"Name: {author.name}")
            print(f"Biography: {author.biography}")




def main():
    library = {}
    users = {}
    authors = {}
    while True:
        print("Welcome to the Library Management System!")
        print(
        '''Main Menu
        1. Book Operations
        2. User Operations
        3. Author Operations
        4. Quit
         ''')
        choice = input("Please enter your choice: ")
        if choice == '1':
            print('''Book Operations
                  1. Add a new book
                  2. Borrow a book
                  3. Return a book
                  4. Search for a book
                  5. Display all books''')
            book_choice = input("Please enter your choice: ")
            if book_choice == '1':
                add_book(library)
            if book_choice == '2':
                isbn = input("Enter the ISBN of the book you'd like to borrow: ")
                try:
                    user_id = input("Enter your user ID: ")
                except KeyError:
                    print("User does not exist. Please add the user first.")
                    continue
                check_out(library, isbn, users[user_id])
            if book_choice == '3':
                isbn = input("Enter the ISBN of the book you'd like to return: ")
                return_book(library,isbn)
            if book_choice == '4':
                search_book = input("Enter the title of the book you'd like to search for: ")
                for isbn, book in library.items():
                    if book.title == search_book:
                        print(f"Title: {book.title}")
                        print(f"Author: {book.author}")
                        print(f"Genre: {book.genre}")
                        print(f"Publication Date: {book.publication_date}")
                        print(f"ISBN: {book.isbn}")
                        if book.available:
                            print("Status: Available")
                        else:
                            print("Status: Checked Out")
            if book_choice == '5':
                for isbn, book in library.items():
                    print(f"Title: {book.title}")
                    print(f"Author: {book.author}")
                    print(f"Genre: {book.genre}")
                    print(f"Publication Date: {book.publication_date}")
                    print(f"ISBN: {book.isbn}")
                    if book.available:
                        print("Status: Available")
                    else:
                        print("Status: Checked Out")
        elif choice == '2':
            print('''User Operations
                    1. Add a new user
                    2. View user details
                    3. Display all users''')
            user_choice = input("Please enter your choice: ")
            if user_choice == '1':
                user = input("Enter the name of the user: ")
                id = input("Enter the ID of the user: ")
                new_user = User(user, id)
                users[id] = new_user
            elif user_choice == '2':
                user_id = input("Enter the ID of the user you'd like to view: ")
                users[user_id].get_user_details()
            else:
                print("Invalid choice. Please try again.")
                continue
        elif choice == '3':
                print('''Author Operations
                      1. Add a new author
                      2. View author details
                      3. Display all authors''')
                author_choice = input("Please enter your choice: ")
                if author_choice == '1':
                    add_author(authors)
                elif author_choice == '2':
                    writer = input("Enter the name of the author you'd like to view: ")
                    display_author(writer, authors)
                elif author_choice == '3':
                    for author in authors.values():
                        print(f"Name: {author.name}")
                        print(f"Biography: {author.biography}")
                else:
                    print("Invalid choice. Please try again.")
                    continue
        elif choice == '4':
                break
        else:
                print("Invalid choice. Please try again.")
                continue
if __name__ == '__main__':
    main()


