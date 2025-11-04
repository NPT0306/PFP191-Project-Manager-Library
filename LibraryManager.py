from Book import Book
class LibraryManager:
    def __init__(self,books):
        self.books = books

    def Addbook(self):
        while True:
            try:
                ID = int(input("Enter Book ID: "))
                break
            except ValueError:
                print("Invalid input! Please enter a number for Book ID.")
        for book in self.books:
            if book.get_ID() == ID:
                print(f"Book with ID {book.get_ID()} already exists! ID current is {self.books[len(self.books)-1].get_ID()}")
                return
        author = input("Enter Author: ")
        while True:
            try:
                publication_year = int(input("Enter Publication Year: "))
                break
            except ValueError:
                print("Invalid input! Please enter a number for Publication Year.")
        category = input("Enter Category: ")
        title = input("Enter Title: ")
        while True:
            availability = input("Enter Availability (available/borrowed): ").lower()
            if availability in ["available", "borrowed"]:
                break
            else:
                print("Invalid input! Please enter only 'available' or 'borrowed'.")
        count = 0

        new_book = Book(ID, title, author, publication_year, category, availability, count)
        self.books.append(new_book)
        print("Book added successfully!")

    def Editbook(self):
        while True:
            ID = input("Enter Book ID to edit: ")
            if ID.isdigit():
                ID = int(ID)
                break
            else:
                print("Invalid input! Please enter a number for Book ID.")
        for book in self.books:
            if book.get_ID() == ID:
                print(f"Editing book: {book.title}")
                book.author = input("New Author: ")
                while True:
                    try:
                        book.publication_year = int(input("New Publication Year: "))
                        break
                    except ValueError:
                        print("Invalid input! Please enter a number for Publication Year.")
                book.category = input("New Category: ")
                book.title = input("New Title: ")
                while True:
                    try:
                        book.count = int(input("New Count: "))
                        break
                    except ValueError:
                        print("Invalid input! Please enter a number for Count.")
                while True:
                    availability = input("Enter Availability (available/borrowed): ").strip().lower()
                    if availability in ["available", "borrowed"]:
                        book.availability = availability
                        break
                    else:
                        print("Invalid input! Please enter only 'available' or 'borrowed'.")
                print(" Book updated successfully!")
                return
        print(" Book not found!")

    def Deletebook(self):
        while True:
            ID = input("Enter Book ID to delete: ")
            if ID.isdigit():
                ID = int(ID)
                break
            else:
                print("Invalid input! Please enter a number for Book ID.")
        for book in self.books:
            if book.get_ID() == ID:
                self.books.remove(book)
                print(" Book deleted successfully!")
                return
        print(" Book not found!")

    def Displaybooklist(self):
        if not self.books:
            print(" No books available.")
            return
        self.books.sort(key = lambda b: b.get_ID())
        print("\n=== Books List ===")
        for book in self.books:
            book.display()

    def Searchforbooks(self):
        keyword = input("Enter keyword (ID / Category / Author / Publication_Year / Title / Availability): ").lower()
        results = []
        for book in self.books:
            if (keyword == str(book.get_ID()) or
                    keyword == book.category.lower() or
                    keyword == book.author.lower() or
                    keyword == str(book.publication_year) or
                    keyword == book.title.lower() or
                    keyword == book.availability.lower()):
                results.append(book)

        if results:
            print(f" Found {len(results)} result(s):")
            for book in results:
                book.display()
        else:
            print(" No matching books found.")

    def borrowBook(self):
        while True:
            id = input("Enter Book ID to borrow: ")
            if id.isdigit():
                id = int(id)
                break
            else:
                print("Invalid input! Please enter a number for Book ID.")

        for book in self.books:
            if book.get_ID() == id:
                if book.availability == 'available':
                    book.availability = 'borrowed'
                    book.count += 1
                    print('Borrowed successfully!')
                else:
                    print('Already borrowed!')
                return

        print('Not Found')

    def returnBook(self):
        while True:
            id = input("Enter Book ID to return: ")
            if id.isdigit():
                id = int(id)
                break
            else:
                print("Invalid input! Please enter a number for Book ID.")

        for book in self.books:
            if book.get_ID() == id:
                if book.availability == 'borrowed':
                    book.availability = 'available'
                    print('Returned successfully!')
                else:
                    print('Not borrowed!')
                return

        print('Not Found')

    def listBorrowedBooks(self):
        check = False
        for book in self.books:
            if book.availability == 'borrowed':
                book.display()
                check = True

        if check == False:
            print('No books are current borrowed')

    def booksByCategory(self):
        category = input("Input category of book: ").lower()
        found_books = []
        for b in self.books:
            if b.category.lower() == category.lower():
                found_books.append(b)

        if not found_books:
            print(f"Not found: {category}")
            return

        print(f"Books in category '{category}':")
        for b in found_books:
            b.display()
        print(f"Total books in '{category.title()}': {len(found_books)}")

    def mostBorrowedBooks(self):
        borrowed_books = []
        for b in self.books:
            if b.count > 0:
                borrowed_books.append(b)

        if not borrowed_books:
            print("No borrowed books found.")
            return

        sorted_books = sorted(borrowed_books, key=lambda b: b.count, reverse=True)

        print("Most Borrowed Books:")
        for b in sorted_books:
            b.display()

    def loadFromFile(self):
        filename = input('Enter name of file to load (e.g., book.txt): ').strip()
        try:
            dem = 0
            with open(filename, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    parts = line.split(',')
                    if len(parts) != 7:
                        print(f'Invalid line format: {line}')
                        continue
                    ID, title, author, year, category, available, count = parts
                    ID = int(ID)
                    available = available
                    year = int(year)
                    count = int(count)
                    book = Book(ID, title, author, year, category, available, count)
                    self.books.append(book)
                    dem += 1
            print(f'Loaded {dem} books from {filename}')
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
        except Exception as e:
            print(f'Error reading file: {e}')

    def saveToFile(self):
        filename = input("Enter name of file to save: ")

        try:
            with open(filename, "w", encoding="utf-8") as file:
                file.write("ID,title,author,category,publication_Year,availability,count\n")

                for b in self.books:
                    line = f"{b.get_ID()},{b.title},{b.author}," \
                           f"{b.category},{b.publication_year},{b.availability},{b.count}\n"
                    file.write(line)

            print("All books saved successfully!")
            return True

        except Exception as e:
            print(f"Error: Cannot save file ({e})")
            return False

