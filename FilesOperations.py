from UsersManager import add_user
from UsersManager import get_users
from User import User

import json

filename = "users.txt"

"""
Needs refactorization - single responsibility!
"""

# transfer into User class to store parsing only in one file?
def parse_dict_to_user(dict):
    parsed = User(name=dict["name"], pwd=dict["password"], email=dict["email"], salt=dict["salt"])
    return parsed


def read_users_from_file():
    try:
        f = open(filename, "r")
        for user in f.readlines():
            loaded_user = parse_dict_to_user(json.loads(user))
            add_user(loaded_user)
        f.close()
    except Exception as error:
        print("Some error occured during reading from file: {0}".format(error))


def save_users_to_file():
    try:
        f = open(filename, "w")
        for user in get_users():
            userStr = json.dumps(user.get_user_as_dict()) + "\n"
            f.write(userStr)
        f.close()
    except Exception as error:
        print("Some error occured during writing to file: {0}".format(error))
