from classes.formatting import bcolors
from classes.checker import data_check
from pymongo import MongoClient


# Database
client = MongoClient('localhost', 27017)
db = client.db
collections = db.user

loop = True
while loop:
    # This code simulates a Sign up and Log in system
    print(bcolors.HEADER + "\n" + "Welcome to Rapture, please select an option." + bcolors.ENDC)
    choice = int(input("(1 for Register, 2 for Log In):"))
    # Selection loop
    username = input("Username: ")
    password = input("Password: ")
    if choice == 1:
        data = data_check(username, password)
        print(data.user_check(), "\n" + data.pass_check())
        if data.user_check() == "Valid Username." and data.pass_check() == "Valid password.":
            collections.insert_one({'username': username, 'password': password})
            print(bcolors.OKGREEN + "You have successfully registered!" + bcolors.ENDC)
    elif choice == 2:
        logged = collections.find_one({'username': username, 'password': password})
        if logged == "None":
            print("Invalid Username")
        else:
            print(bcolors.OKBLUE + "You have successfully logged!" + bcolors.ENDC)
            loop = False
