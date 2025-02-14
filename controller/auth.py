class AuthController:
    def __init__(self, model):
        self.model = model

    def login(self, username, password):
        try:
            return self.model.login(username, password)
        except:
            return False

    def register(self, username, password, user_type):
        user_type = "admin" if user_type == 1 else "student"
        try:
            return self.model.register(username, password, user_type)
        except:
            return False
