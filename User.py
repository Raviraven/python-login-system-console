class User:

    def __init__(self, name, pwd, email, salt):
        self.name = name
        self.password = pwd
        self.email = email
        self.salt = salt

    def __str__(self):
        return "User: {0}, email: {1}".format(self.name, self.email)

    def get_user_as_dict(self):
        result = {
            "name": self.name,
            "password": self.password,
            "email": self.email,
            "salt": self.salt
        }
        return result
