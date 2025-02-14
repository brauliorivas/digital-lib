class AdminController:
    def __init__(self, model):
        self.model = model

    def add_book(self, code, title, author, stock):
        return self.model.add(code, title, author, stock)

    def search_info(self, code):
        try:
            return self.model.search(code)
        except:
            return None
