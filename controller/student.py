class StudentController:
    def __init__(self, book_model, loan_model):
        self.book_model = book_model
        self.loan_model = loan_model

    def get_books(self):
        return self.book_model.get_available()

    def reserve_book(self, book):
        code = book.code
        self.book_model.loan_copy(code)

    def loan_books(self, books, username):
        try:
            for book in books:
                code = book.code
                self.loan_model.loan_book(username, code)

            return True
        except:
            return False

    def return_book(self, book):
        code = book.code
        self.book_model.return_copy(code)

    def return_books(self, books):
        for book in books:
            self.return_book(book)

    def get_loans(self, username):
        return self.loan_model.get_loans(username)
