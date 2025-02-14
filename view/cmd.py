from .admin import AdminView
from .auth import AuthView
from .student import StudentView
from .book import BookView
from .loan import LoanView

from model.book import Book
from model.user import User
from model.loan import Loan

from controller.auth import AuthController
from controller.admin import AdminController
from controller.student import StudentController

auth_view = AuthView()
admin_view = AdminView()
book_view = BookView()
student_view = StudentView()
loan_view = LoanView()

auth_controller = AuthController(User())
admin_controller = AdminController(Book())
student_controller = StudentController(Book(), Loan())


def render():
    auth_view.welcome()

    option = 0
    while option != 3:
        option = auth_view.options()

        user = None

        if option == 1:
            username, password = auth_view.login()
            user = auth_controller.login(username, password)

            if not user:
                auth_view.login_error()
        elif option == 2:
            username, password, user_type = auth_view.register()
            user = auth_controller.register(username, password, user_type)

            if not user:
                auth_view.register_error()

        elif option == 3:
            print("Thanks for your visit!\n")
        else:
            print("Enter a valid option\n")

        if user:
            redirect_user(user)


def redirect_user(user):
    user_type = user.user_type

    if user_type == "admin":
        admin(user)

    if user_type == "student":
        student(user)


def admin(user):
    admin_view.welcome(user.username)

    option = 0

    while option != 3:
        option = admin_view.options()

        if option == 1:
            code, title, author, stock = admin_view.add_book()
            book = admin_controller.add_book(code, title, author, stock)
            admin_view.successfully_added()
        elif option == 2:
            code = admin_view.get_info()
            book = admin_controller.search_info(code)
            if book:
                book_view.show_book(book)
            else:
                admin_view.no_results()
        elif option != 3:
            print("Choose a valid option\n")

    print("Returning\n")


def student(user):
    username = user.username
    student_view.welcome(username)

    option = 0

    while option != 3:
        option = student_view.options()

        if option == 1:
            loan_process(username)
        elif option == 2:
            loans = student_controller.get_loans(username)
            student_view.show_loans(loans)
        elif option == 3:
            print("Returning...\n")
        else:
            print("You should choose a valid option\n")


def loan_process(username):
    books = student_controller.get_books()

    loan_books = []
    for book in books:
        lend_book = student_view.lend_book(book)

        if lend_book:
            student_controller.reserve_book(book)
            loan_books.append(book)

    if len(loan_books) == 0:
        print("No books to loan\n")
        return

    confirmed = student_view.confirm_loan()

    if confirmed:
        loan_res = student_controller.loan_books(loan_books, username)
        loan_view.status_message(loan_res)
        return
    elif confirmed is False:
        print("Returning reserverd books\n")
    else:
        print("You should choose a valid option\n")

    student_controller.return_books(loan_books)
