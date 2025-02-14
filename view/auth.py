class AuthView:
    def welcome(self):
        print("Welcome to the digital library system!\n\n")

    def options(self):
        print("1. Login\n")
        print("2. Register\n")
        print("3. Exit\n")

        value = int(input("Choose an option: "))

        return value

    def login(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        return username, password

    def register(self):
        username = input("Enter a username to register: ")
        password = input("Create a password: ")
        user_type = int(
            input("What type of user are you?\n1. Admin\n2. Student\n===> "))

        return username, password, user_type

    def login_error(self):
        print("Incorrect username or password")

    def register_error(self):
        print("This username has already been taken")
