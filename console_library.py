import json

class BookError(BaseException):
    def __str__(self):
        return "Something went wrong with your book. Please check again its title and status."

class BookOut(BookError) :
    def __str__(self):
        return "Book unavailable."

class UnknownBook(BookError) :
    def __str__(self):
        return "Book unknown."

class BookIn(BookError) :
    def __str__(self):
        return "Book already in."


class Book :
    nb_book = 0
    def __init__(self, title, author, year, id=0, status='avail'):
        Book.nb_book += 1
        self.__id = Book.nb_book if id == 0 else id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def get_info(self):
        infos = {
            'title' : self.title,
            'author' : self.author,
            'year' : self.year,
            'status' : self.status,
            'id' : self.__id
        }
        return infos

    def __repr__(self):
        present = ''
        infos = self.get_info()
        for key in infos.keys() :
            present += f"{key} : {infos[key]} \n"
        return present

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.year}) - {'Available' if self.status == 'avail' else 'Borrowed'}"

    def borrow(self):
        if self.status != 'avail' : raise BookOut
        else :
            self.status = 'notavail'
            print(f"You successfully borrowed the book '{self.title}'.")
            return True

    def bback(self):
        if self.status != 'notavail' : raise BookIn
        else :
            self.status = 'avail'
            print(f"You successfully returned the book '{self.title}'.")
            return True

class Library :
    def __init__(self):
        self.book_list = []

    def __repr__(self):
        return self.book_list

    def __str__(self):
        return f"Library containing {len(self.book_list)} books."

    def display_avail_books(self):
        print("Here are available books : ")
        i=0
        for book in self.book_list :
            if book.status == "avail" :
                print(book)
                i+=1
        if i == 0 : print("No book available.")
        return i

    def add_book(self, book):
        title = book.title.strip().lower()
        auth = book.author.lower()
        ad = True
        for bk in self.book_list :
            if title == bk.title.strip().lower() and auth == bk.author.lower() :
                ad = False
                break

        if ad : self.book_list.append(book)
        return ad

    def search_title(self, title):
        titlebook = []
        for book in self.book_list :
            if book.title.strip().lower() == title.lower() :
                titlebook.append(book)
        if len(titlebook) == 0 :
            raise UnknownBook
        else :
            return titlebook

    def search_author(self, author):
        authbook = []
        for book in self.book_list :
            if book.author.lower() == author.lower() :
                authbook.append(book)
        if len(authbook) == 0 :
            raise UnknownBook
        else :
            return authbook

    def search_keyword(self, keyw):
        keybook = []
        for book in self.book_list :
            if (keyw.lower() in book.title.lower()) or (keyw.lower() in book.author.lower()) or (keyw.lower() in book.year.lower()) :
                keybook.append(book)

        if len(keybook) == 0:
            raise UnknownBook
        else:
            return keybook

    def borrow_book(self, title):
        bor = False
        try :
            books = self.search_keyword(title)
            if len(books) == 1 :
                bor = books[0].borrow()
            else :
                i=1
                print("Please chose the book to borrow : ")
                for bk in books :
                    if bk.status == 'avail' :
                        print(f"{i} : {bk}")
                        i+=1
                while True :
                    nb = input("Nb (0 to borrow nothing) : ")
                    if not nb.isdigit() : continue
                    if nb == '0' : break
                    try :
                        bor = books[int(nb)-1].borrow()
                        break
                    except IndexError :
                        continue
                    except BookOut :
                        print("Sorry, this book is not available.")
                    except Exception as e:
                        print(f"Something went wrong : {e}")
                        break

        except (UnknownBook, BookOut) as e :
            print(f"Sorry, this book does not exist or is already out : {e}")
        except Exception as e:
            print(f"Unknown error in borrowing system. Message : {e}")
        finally :
            return bor

    def return_book(self, title):
        ret = False
        try :
            books = self.search_keyword(title)
            if len(books) == 1:
                ret = books[0].bback()
            else:
                i = 1
                print("Please chose the book to return : ")
                for bk in books:
                    if bk.status == 'notavail':
                        print(f"{i} : {bk}")
                        i += 1
                while True:
                    nb = input("Nb (0 to borrow nothing) : ")
                    if not nb.isdigit(): continue
                    if nb == '0': break
                    try:
                        ret = books[int(nb) - 1].bback()
                        break
                    except IndexError:
                        continue
                    except BookIn:
                        print("Sorry, this book is already in.")
                    except Exception as e:
                        print(f"Something went wrong : {e}")
                        break
        except (UnknownBook, BookIn) as e :
            print(f"Sorry, this book does not exist or is already in : {e}")
        except Exception as e :
            print(f"Unknown error in returning system : {e}.")
        finally :
            return ret

    def save_library(self):
        list_book = []
        for book in self.book_list :
            list_book.append(book.get_info())

        with open("lib1.json", "w") as f:
            json.dump(list_book, f, indent=2)

        return print("Library saved.")

    def load_library(self, lib="lib1.json"):
        books = []
        try :
            with open(lib, "r") as f:
                data = json.load(f)
                books = [Book(**entry) for entry in data]
                for book in books:
                    self.add_book(book)
        except OSError as e :
            print(e)
            return
        except json.JSONDecodeError:
            print("Corrupted or wrong format file.")
            return
        except TypeError as e :
            print("Sorry, unable to load your books : one or several metadatas are wrong.")
            print(f"Here is the full message : {e}")
        except :
            print("Unable to load your library.")
            return
        avail = 0
        for bk in books :
            if bk.status == 'avail' : avail += 1
        return print(f"Library loaded. \n{len(books)} total books, {avail} available.")

def create_new_book() :
    title = input("What's the book title ?")
    author = input("Who is the author ?")
    year = ''
    while True :
        year = input("What's the year ?")
        if not year.isdigit() : continue
        break

    return Book(title, author, year)

bibli = Library()
bibli.load_library()

menu = (f"{'_'*12}MENU{'_'*12}\n"
        f"1 : Add new book.\n"
        f"2 : Borrow a book.\n"
        f"3 : Return a book.\n"
        f"4 : Display available books.\n"
        f"5 : Save library.\n"
        f"6 : Load new library.\n"
        f"7 : Quit.\n"
        f"--> Your choice : ")

while True :
    choice = input(menu)
    if not choice.isdigit() : continue
    if int(choice) < 1 or int(choice) > 7 : continue
    match choice :
        case '1' :
            addbk = create_new_book()
            print("Book successfully added.") if bibli.add_book(addbk) else print("Sorry, unable to add this book.")
        case '2' :
            bortitle = input("What is the title you want to borrow ?")
            bibli.borrow_book(bortitle.strip())
        case '3' :
            rettitle = input("What is the title you want to return ?")
            bibli.return_book(rettitle)
        case '4' :
            bibli.display_avail_books()
        case '5' :
            bibli.save_library()
        case '6' :
            newlib = input("What is the path to the new lib ?")
            bibli.load_library(newlib)
        case '7' :
            break


