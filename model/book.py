from schema.book_schema import BookSchema
from .loader import Loader

books_json = "books.json"
books_io = Loader(books_json, BookSchema)


class Book:
    def add(self, code, title, author, stock):
        books = books_io.load()
        for book in books:
            if book.code == code:
                book.stock += stock
                return

        new_book = BookSchema(code, title, author, stock)
        books.append(new_book)
        books_io.save(books)

    def search(self, code):
        books = books_io.load()
        for book in books:
            if book.code == code:
                return book

        raise Exception("Not found")

    def get_available(self):
        books = books_io.load()
        return [book for book in books if book.stock > 0]

    def update_stock(self, code, new_stock):
        books = books_io.load()
        for book in books:
            if book.code == code:
                book.stock += new_stock

        books_io.save(books)

    def loan_copy(self, code):
        self.update_stock(code, -1)

    def return_copy(self, code):
        self.update_stock(code, 1)
