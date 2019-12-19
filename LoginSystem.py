import FilesOperations
from User import User
import AccountManager


def register():
    new_username = input("Your username: ")
    new_password = input("Password: ")
    #repeat_password = input("Repeat password: ")
    new_email = input("Email: ")

    new_user = User(name=new_username, pwd=new_password, email=new_email)
    AccountManager.register_account(new_user)


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