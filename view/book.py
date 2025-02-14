class BookView:
    def show_book(self, book):
        print("Showing information about the book\n")

        code = book.code
        title = book.title
        author = book.author
        stock = book.stock

        print(f"Code: {code}\n")
        print(f"Title: {title}\n")
        print(f"Author: {author}\n")
        print(f"Stock: {stock}\n")
