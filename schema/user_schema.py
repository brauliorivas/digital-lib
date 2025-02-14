class UserSchema:
    def __init__(self, username, password, user_type):
        self.username = username
        self.password = password
        self.user_type = user_type

    @staticmethod
    def to_dict(user: User):
        return vars(user)

    @staticmethod
    def from_dict(user):
        username = user["username"]
        password = user["password"]
        user_type = user["user_type"]

        if user_type == "student":
            return Student(username, password)

        if user_type == "admin":
            return Admin(username, password)


class Admin(UserSchema):
    def __init__(self, username, password):
        super().__init__(username, password, "admin")


class Student(UserSchema):
    def __init__(self, username, password):
        super().__init__(username, password, "student")
