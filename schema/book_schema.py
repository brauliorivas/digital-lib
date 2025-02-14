class BookSchema:
    def __init__(self, code, title, author, stock):
        self.code = code
        self.title = title
        self.author = author
        self.stock = int(stock)

    @staticmethod
    def to_dict(book: BookSchema):
        return vars(book)

    @staticmethod
    def from_dict(book_dict):
        code = book_dict["code"]
        title = book_dict["title"]
        author = book_dict["author"]
        stock = book_dict["stock"]

        return BookSchema(code, title, author, stock)
