import sys

def sign_up():
    user_name = input("Please make your username: ")
    pass_word = int(input("Please make  your password: "))
    listHistory = [user_name,pass_word]
    return listHistory


def make_passwords(password_history):
    while True:
        quit_choice = input("If you want to quit do y and if you want to make more passwords do n or something else: y/n ")
        if quit_choice.lower() == "y":
            sys.exit()
        else:
            create_password = input("Please create your password(only alphabets): ")
            password_history.append(create_password)
            print(f"Current password history: {create_password}")
        return password_history


def view_passwords(password_history):
    view_choice = input("Do you want to view passwords and if not press y otherwise press any other alphabet key: ")
    if view_choice.lower() == "y":
        sys.exit()
    else:
        print("Password History: ",password_history)
password_history = []


make_account = sign_up()
putting_password = make_passwords(password_history)
checking_passwords = view_passwords(password_history)

