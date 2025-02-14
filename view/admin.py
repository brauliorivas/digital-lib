class AdminView:
    def welcome(self, username):
        print(f"Welcome back {username}\n")

    def options(self):
        print("1. Add a new book\n")
        print("2. Get information from book\n")
        print("3. Return\n")

        option = int(input("Choose an option: "))

        return option

    def add_book(self):
        print("Adding a new book to the system\n")

        code = input("Enter the code: ")
        title = input("Enter the title: ")
        author = input("Enter the author: ")
        stock = input("Enter the stock: ")

        return code, title, author, stock

    def get_info(self):
        print("Get information from the book\n")

        code = input("Enter the code: ")

        return code

    def successfully_added(self):
        print("The book has been successfully added\n")

    def no_results(self):
        print("No books have been found\n")
