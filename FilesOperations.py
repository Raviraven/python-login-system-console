from UsersManager import add_user
from UsersManager import get_users
from User import User

import json


def parse_dict_to_user(dict):
    parsed = User(name=dict["name"], pwd=dict["password"], email=dict["email"])
    return parsed


def read_users_from_file(filename):
    try:
        f = open(filename, "r")
        for user in f.readlines():
            loaded_user = parse_dict_to_user(json.loads(user))
            add_user(loaded_user)
        f.close()
    except Exception as error:
        print("Some error occured during reading from file: {0}".format(error))


def save_users_to_file(filename):
    try:
        f = open(filename, "a")
        for user in get_users():
            json.dump(user.get_user_as_dict(), f)
        f.close()
    except Exception as error:
        print("Some error occured during writing to file: {0}".format(error))
