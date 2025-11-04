from Book import Book
from LibraryManager import LibraryManager

books = [
    Book(1, "Python Basics", "John Smith", 2020, "Programming", "available", 3),
    Book(2, "Data Structures", "Alice Brown", 2018, "Computer Science", "borrowed", 2),
    Book(3, "Network Security", "James Lee", 2022, "Cybersecurity", "borrowed", 0),
    Book(4, "Linear Algebra", "David Kim", 2019, "Mathematics", "available", 5),
]

if __name__ == "__main__":
    manager = LibraryManager(books)

    while True:
        try:
            choice = int(input(
                '======================= LIBRARY MANAGEMENT ======================\n'
                'What do you want to do? Please select from the following options \n'
                '1 : Add book \n'
                '2 : Edit book \n'
                '3 : Delete book \n'
                '4 : Display all books \n'
                '5 : Search book \n'
                '6 : Borrow book \n'
                '7 : Return book \n'
                '8 : Display all borrowed book \n'
                '9 : Display books following the category \n'
                '10: Show most popular books in descending order \n'
                '11: Export data book to file .txt \n'
                '12: Import data book from file .txt \n'
                '====================================================================\n'
                'Enter your selection: '

            ))
        except:
            print('Please enter number from 1 to 12')
            continue
        if choice not in range(1, 13):
            print('Please enter number from 1 to 12')
            continue

        if choice == 1:
            manager.Addbook()
        if choice == 2:
            manager.Editbook()
        if choice == 3:
            manager.Deletebook()
        if choice == 4:
            manager.Displaybooklist()
        if choice == 5:
            manager.Searchforbooks()
        if choice == 6:
            manager.borrowBook()
        if choice == 7:
            manager.returnBook()
        if choice == 8:
            manager.listBorrowedBooks()
        if choice == 9:
            manager.booksByCategory()
        if choice == 10:
            manager.mostBorrowedBooks()
        if choice == 11:
            manager.saveToFile()
        if choice == 12:
            manager.loadFromFile()

        yesno = input('Do you want to continue? Yes/No ')
        if yesno.strip().lower() == "yes":
            continue
        else:
            break

    print('Goodbye')