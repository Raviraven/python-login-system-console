from UsersManager import add_user
from UsersManager import get_users
from FilesOperations import save_users_to_file
import User


def register():
    new_username = input("Your username: ")
    new_password = input("Password: ")
    #repeat_password = input("Repeat password: ")
    new_email = input("Email: ")

    new_user = User(name=new_username, pwd=new_password, email=new_email)
    add_user(new_user)
    save_users_to_file()

    #some try - except action,

    print("Congratulations {0} ! You successfully created an account!")


def login(username, password):
    for user in get_users():
        if username == user.name and password == user.password:
            print("successfully logged in")
            break

    print("wrong username or password")

