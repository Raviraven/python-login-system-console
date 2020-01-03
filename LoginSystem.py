import FilesOperations
import AccountManager
from getpass import getpass
from Exceptions.ExitException import ExitException
import os


clear = lambda: os.system("cls")


def get_input(input_prompt):
    temp = input(input_prompt)
    if temp == 'q':
        raise ExitException
    return temp


def register():
    new_username = input("Your username: ")
    new_password = getpass(prompt="Password: ") # input("Password: ")   # will work outside pycharm
    repeat_password = getpass(prompt="Repeat_password: ") # input("Repeat password: ")
    new_email = input("Email: ")

    AccountManager.register_account(name=new_username, password=new_password, repeat_password=repeat_password,
                                    email=new_email)


def login():
    username = input("Enter username: ")
    password = getpass("Enter password: ")
    AccountManager.login_account(username=username, password=password)


clear()
FilesOperations.read_users_from_file()
print("Hi! Do you want to register a new account or log in into existing one?")

try:
    while True:
        print("\n(1) Register")
        print("(2) Log in")
        print("(q) Exit")

        chosenOption = get_input("Option: ")

        if chosenOption == '1':
            clear()
            register()
        elif chosenOption == '2':
            clear()
            login()
        else:
            print("wrong command")

except ExitException as error:
    print(error)
