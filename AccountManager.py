from UsersManager import add_user
from UsersManager import get_users
from FilesOperations import save_users_to_file

from Exceptions.UserExistsException import UserExistsException
from Exceptions.PasswordExceptions import PasswordsDoesntMatchException
from Exceptions.InvalidEmailException import InvalidEmailException

import User
import re
import string
import secrets
import hashlib


salt_length = 8


def register_account(name, password, repeat_password, email):
    try:
        username_validation(name)
        password_validation(password, repeat_password)
        email_validation(email)

        salt = generate_salt(salt_length=salt_length)
        password_hashed = hash_password(password=password, salt=salt)

        new_user = User.User(name=name, pwd=password_hashed, email=email, salt=salt)
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
    email_pattern = "(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
    match = re.fullmatch(email_pattern, email)
    if match is None:
        raise InvalidEmailException


def generate_salt(salt_length):
    alphabet = string.ascii_letters + string.digits
    salt = ''.join(secrets.choice(alphabet) for i in range(salt_length))
    return salt


def hash_password(password, salt):
    password_salted = password + salt
    password_hashed = hashlib.sha256(password_salted.encode()).hexdigest()
    return password_hashed
