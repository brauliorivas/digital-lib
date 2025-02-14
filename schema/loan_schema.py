from schema.book_schema import BookSchema
from datetime import date


class LoanSchema:
    def __init__(self, username, code,  title, author, loan_date, due_date):
        self.username = username
        self.code = code
        self.title = title
        self.author = author
        self.loan_date = loan_date
        self.due_date = due_date

    @staticmethod
    def to_dict(loan: LoanSchema):
        d = vars(loan)
        d["loan_date"] = loan.loan_date.isoformat()
        d["due_date"] = loan.due_date.isoformat()
        return d

    @staticmethod
    def from_dict(loan_dict):
        username = loan_dict["username"]
        code = loan_dict["code"]
        title = loan_dict["title"]
        author = loan_dict["author"]
        loan_date = date.fromisoformat(loan_dict["loan_date"])
        due_date = date.fromisoformat(loan_dict["due_date"])

        return LoanSchema(username, code, title, author, loan_date, due_date)
