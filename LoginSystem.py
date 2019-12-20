import FilesOperations
import AccountManager
from getpass import getpass


def register():
    new_username = input("Your username: ")
    new_password = input("Password: ") # getpass(prompt="Password: ")  # will work outside pycharm
    repeat_password = input("Repeat password: ") # getpass(prompt="Repeat_password: ")
    new_email = input("Email: ")

    AccountManager.register_account(name=new_username, password=new_password, repeat_password=repeat_password, email=new_email)


def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    AccountManager.login_account(username=username, password=password)


FilesOperations.read_users_from_file()

print("Hi! Do you want to register a new account or log in into existing one?")
print("1. Register")
print("2. Log in")

done = False
while(not done):
    chosenOption = input("Option: ")
    if chosenOption == '1':
        register()
        done = True
    elif chosenOption == '2':
        login()
        done = True
    else:
        print("wrong command")

print("The end :V ")