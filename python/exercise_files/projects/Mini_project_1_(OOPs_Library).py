class Library:
    def __init__(self, list, name):
        self.booksList = list
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f'We have following books in our library: {self.name}')
        for book in self.booksList:
            print(book)

    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print('Lender-Book database has been updated. You can take the book now')
        else:
            print(f"Book is already being used by {self.lendDict[book]}")

    def addBook(self, book):
        self.booksList.append(book)
        print('Book has been added to the book list')
        
    def returnBook(self, book):
        self.lendDict.pop(book)
        print('The book has been successfully returned...')

if __name__ == '__main__':
    harry = Library(['Python', 'Rich Daddy Poor Daddy', 'Harry Potter', 'C++ Basics', 'Algorithms by CLRS'], 'Zarir Bookstore')

    while(True):
        print(f'Welcome to the {harry.name} library....\nEnter your choice to continue')
        print('1: \tDisplay Books')
        print('2: \tLend a Book')
        print('3: \tAdd a Book')
        print('4: \tReturn a Book')
        usr_chice = int(input())

        if usr_chice==1:
            harry.displayBooks()

        elif usr_chice==2:
            book = input('Enter the name of the book you want to lend: ')
            user = input('Enter your name: ')
            harry.lendBook(user, book)

        elif usr_chice==3:
            book = input('Enter the name of the book you want to add: ')
            harry.addBook(book)

        elif usr_chice==4:
            book = input('Enter the name of the book you want to return: ')
            harry.returnBook(book)

        else:
            print('Not a valid option....')


        print('Press q to quit anc c to continue....')
        usr_chice2 = ''
        while(usr_chice2!='c' and usr_chice2!='q'):
            usr_chice2 = input()
            if usr_chice2=='q':
                exit()
            if usr_chice2=='c':
                continue


#16:00/25:59