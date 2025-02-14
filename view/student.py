from schema.book_schema import BookSchema
from .book import BookView
from .loan import LoanView


class StudentView:
    def welcome(self, username):
        print(f"Welcome back student {username}!\n")

    def options(self):
        print("1. Lend a book\n")
        print("2. Show past loans\n")
        print("3. Return\n")

        return int(input("Choose an option: "))

    def lend_book(self, book: BookSchema):
        BookView().show_book(book)

        choosen = input(
            "Do you want to lend this book? (y) to lend, (enter) to pass ")

        return choosen == "y"

    def confirm_loan(self):
        val = input(
            "Do you want to make a loan of the selected book? (y) yes (n) no: \n")

        if val == "y":
            return True
        elif val == "n":
            return False

        return None

    def show_loans(self, loans):
        if len(loans) == 0:
            print("No loans found!!!\n")
            return

        print("Current loans: \n")

        for loan in loans:
            LoanView().show(loan)
