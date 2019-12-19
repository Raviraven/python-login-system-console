import User

usersDB = []


def add_user(new_user):
    usersDB.append(new_user)


def add_user_parametrized(name, password, email):
    new_user = User(name=name, pwd=password, email=email)
    add_user(new_user)


def get_users():
    return usersDB
