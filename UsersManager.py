import User

usersDB = []


def add_user(new_user):
    usersDB.append(new_user)


def get_users():
    return usersDB