class User:

    def __init__(self, name, pwd, email):
        self.name = name
        self.password = pwd
        self.email = email

    def __str__(self):
        return "User: {0}, email: {1}".format(self.name, self.email)