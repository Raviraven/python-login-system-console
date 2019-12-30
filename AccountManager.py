from UsersManager import add_user
from UsersManager import get_users
from FilesOperations import save_users_to_file

from Exceptions.UserExistsException import UserExistsException
from Exceptions.PasswordExceptions import PasswordsDoesntMatchException
from Exceptions.InvalidEmailException import InvalidEmailException

import User
import re


def register_account(name, password, repeat_password, email):
    try:
        username_validation(name)
        password_validation(password, repeat_password)

        new_user = User.User(name=name, pwd=password, email=email)
        add_user(new_user)
        save_users_to_file()
    except UserExistsException as error:
        print(error)
    except PasswordsDoesntMatchException as error:
        print(error)
    except Exception as error:
        print("An error occured: {0}".format(error))
    else:
        print("Congratulations {0} ! You successfully created an account!".format(new_user.name))


def login_account(username, password):
    for user in get_users():
        if username == user.name and password == user.password:
            print("successfully logged in")
            return
    print("wrong username or password")


def username_validation(username):
    for user in get_users():
        if user.name == username:
            raise UserExistsException


def password_validation(password, repeat_password):
    if password != repeat_password:
        raise PasswordsDoesntMatchException


def email_validation(email):
    match = re.fullmatch("pattern", email)
    if match is None:
        raise InvalidEmailException
