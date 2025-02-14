from .loader import Loader
from schema.user_schema import UserSchema, Admin, Student

users_json = "users.json"

users_io = Loader(users_json, UserSchema)


class User:
    def register(self, username, password, user_type):
        users = users_io.load()
        for user in users:
            if user.username == username:
                raise Exception("User already exists")

        if user_type == "admin":
            new_user = Admin(username, password)

        if user_type == "student":
            new_user = Student(username, password)

        users.append(new_user)
        users_io.save(users)
        return new_user

    def login(self, username, password):
        users = users_io.load()

        for user in users:
            if user.username == username and user.password == password:
                return user

        raise Exception("Incorrect login")
