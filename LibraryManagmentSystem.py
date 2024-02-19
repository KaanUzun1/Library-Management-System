class Library:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(self.filename, "a+")



    def list_book(self):
        self.file.seek(0)
        books = self.file.read().splitlines()


        """I only want to print the author's name and the title of the book. Since these datas are stored before the second comma,
        I am finding the second index of the second comma and print what it says before"""
        for book in books:
            slicing_point = 0
            commas_found = 0
            for i in range(len(book)):
                if book[i] == ",":
                    commas_found += 1
                    if commas_found == 2:
                        slicing_point = i
                        break
            book = book[0:slicing_point]
            print(book)


    def add_book(self):
        title = input("Enter the book title: ")
        author = input("Enter the author: ")
        release_date = input("Enter the release year: ")
        page_number = input("Enter the number of pages: ")
        
        input_data = "Book: " + title + ", " + "Author: " + author + ", " + "Release date: " + release_date + ", " + "Number of pages: " + page_number + "\n"
        print(input_data)
        self.file.write(input_data)
        print("The book is succesfuly added!")


    def remove_book(self):
        title = input("Enter the title of the book you want to remove: ")
        self.file.seek(0)
        books = self.file.read().splitlines()
        removed = False
            
        """The name of the book is written after the index 6 and before the first appearance of a comma.
        So I am comparing the title that the user entered with the sliced string"""
        for i in range(len(books)):
            slicing_point = 0
            commas_found = 0
            for j in range(len(books[i])):
                if books[i][j] == ",":
                    commas_found += 1
                    if commas_found == 1:
                        slicing_point = j
                        break
            book_to_remove = books[i][6:slicing_point]
            if title == book_to_remove:
                books.pop(i)
                removed = True
                break
        
        #I am writing all of the txt file's content without the book that is removed
        with open(self.filename, "w") as file:
            for book in books:
                book = book + "\n"
                self.file.write(book)
            if removed:
                print("The book is Succesfuly removed")
            else:
                print("The book you entered was not found. You may have entered the title incorrectly.")

    def __del__(self):
        self.file.close()


#This function is to make sure that the user entered a proper input
def get_input():
    while True:
        action_p = input("""
 \n***MENU***
1) List Books
2) Add Book
3) Remove Book
q) Quit
Enter your choice (1-3 or q): """)
            
        if action_p == "1" or action_p == "2" or action_p == "3" or action_p == "q":
                return action_p

        else:
            print("Improper Usage!")



def main():
    lib = Library("books.txt")
    while True:
        action = get_input()

        if action == "1":
            lib.list_book()

        elif action == "2":
            lib.add_book()

        elif action == "3":
            lib.remove_book()

        elif action == "q":
            return 1

main()