class LoanView:
    def show(self, loan):
        title = loan.title
        author = loan.author
        loan_date = loan.loan_date
        due_date = loan.due_date

        print(f"Showing loan\n")
        print(f"Book title: {title}\n")
        print(f"Book author: {author}\n")
        print(f"Loan date: {loan_date}\n")
        print(f"Due date: {due_date}\n")

    def status_message(self, res):
        if res:
            self.success()
        else:
            self.error()

    def success(self):
        print("Books lent successfully\n")

    def error(self):
        print("Could not lend books\n")
