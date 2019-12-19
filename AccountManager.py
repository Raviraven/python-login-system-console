from UsersManager import add_user
from UsersManager import get_users
from FilesOperations import save_users_to_file
import User


def register_account(new_user):
    add_user(new_user)
    save_users_to_file()

    #some try - except action,

    print("Congratulations {0} ! You successfully created an account!".format(new_user.name))


def login_account(username, password):
    for user in get_users():
        if username == user.name and password == user.password:
            print("successfully logged in")
            return
    print("wrong username or password")

