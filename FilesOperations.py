from UsersManager import add_user
from UsersManager import get_users


def read_users_from_file(filename):
    try:
        f = open(filename, "r")
        for user in f.readlines():
            add_user(user)
        f.close()
    except Exception as error:
        print("Some error occured during reading from file: {0}".format(error))


def save_users_to_file(filename):
    try:
        f = open(filename, "a")
        for user in get_users():
            f.write(user + "\n")
        f.close()
    except Exception as error:
        print("Some error occured during writing to file: {0}".format(error))