class PasswordsDoesntMatchException(Exception):
    def __init__(self):
        super().__init__("Passwords doesn't match")
