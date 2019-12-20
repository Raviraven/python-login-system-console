class UserExistsException(Exception):
    def __init__(self):
        super().__init__("User already exists in database")
