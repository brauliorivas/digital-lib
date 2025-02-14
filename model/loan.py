from schema.loan_schema import LoanSchema
from model.book import books_io
from .loader import Loader
from datetime import date, timedelta

loans_file = "loans.json"

loan_io = Loader(loans_file, LoanSchema)


class Loan:
    def loan_book(self, username, code):
        books = books_io.load()
        loans = loan_io.load()

        book_to_loan = None
        for book in books:
            if book.code == code:
                book_to_loan = book

        if book_to_loan is None:
            raise Exception("Could not find this book")

        today = date.today()

        for loan in loans:
            same_user = loan.username == username
            same_book = loan.code == code
            in_range = loan.due_date > today
            valid_loan = same_user and same_book and in_range

            if valid_loan:
                raise Exception("Can't loan this book")

        due_date = today + timedelta(days=30)

        loan = LoanSchema(username, code,  book_to_loan.title,
                          book_to_loan.author, today, due_date)

        loans.append(loan)
        loan_io.save(loans)

    def get_loans(self, username):
        loans = loan_io.load()

        user_loans = [loan for loan in loans if loan.username == username]

        return user_loans
