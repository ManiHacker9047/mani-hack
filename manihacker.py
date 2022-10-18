class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("Books present in this library are: ")
        for book in self.books: 
            print(" *" + book)
    
    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. Please keep it safe and return it within 30 days")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry, This scripts is either not available or has already been issued to someone else. Please wait until the scripts is available")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning this scripts ! Hope you enjoyed reading it. Have a great day ahead!")

class Student: 
    def requestBook(self):
        self.book = input("Enter the name of the scripts you want to Mani hack: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the scripts you want to return: ")
        return self.book
         

if __name__ == "__main__":
    centraLibrary = Library(["whatsapp hack", " phone hack", "Camera hack", "Python hack list "])
    student = Student()
    # centraLibrary.displayAvailableBooks()
    while(True):
        welcomeMsg = '''\n ====== Welcome to MANi.... Hacker ======
        Please choose an option:
        1. List all hackes
        2. Request a hack scripts
        3. Add/Return a scripts
        4. Exit the ....Mani Hacker...
        '''
        print(welcomeMsg)
        a = int(input("Enter a choice: "))
        if a == 1:
            centraLibrary.displayAvailableBooks()
        elif a == 2:
            centraLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centraLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks for choosing ..Mani Hacker... Have a great day ahead!")
            exit()
        else:
            print("Invalid Choice!")