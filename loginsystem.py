# Project 9: Login System:

from getpass import getpass
from datetime import datetime

def load_user():
    with open("user2.txt", "r") as file:
        username = file.readline().strip()
        password = file.readline().strip()
    return username, password

def save_password(username, password):
    with open("user2.txt", "w") as file:
        file.write(username + "\n")
        file.write(password)

def login(username, password):
    user = input("\nUsername: ")
    pwd = getpass("Password: ")
    return user == username and pwd == password

def show_login_time():
    print(f"Login Successful! ✅ \nLogin time:", datetime.now().strftime("%d-%m-%Y %I:%M %p"))

def menu():
    print("\n1. View Profile \n2. Change Password \n3. Logout")
    return input("\nOption: ")

def view_profile(username):
    print("Username:", username)

def change_password():
    global password
    new_password = input("New password: ")
    password = new_password
    save_password(username, password)
    print("Password changed successfully.✅")

def dashboard():
    while True:
        option = menu()

        if option == "1":
            view_profile(username)
        elif option == "2":
            change_password()
        elif option == "3":
            print("Logged out.📤")
            break

username, password = load_user()

for attempts in range(5): # attempts = 5
    if login(username, password):
        show_login_time()
        dashboard()
        break
    print("⚠️ Wrong credentials.")
else:
    print("Account locked.⛔")
