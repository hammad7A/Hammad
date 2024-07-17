import sys

def sign_up():
    user_name = input("Please make your username: ")
    pass_word = int(input("Please make  your password: "))
    listHistory = [user_name,pass_word]
    return listHistory


def make_passwords(password_history):
    while True:

        create_password = input("Please create your password(only alphabets): ")
        password_history.append(create_password)
        print(f"Current password history: {create_password}")
        quit_choice = input(
            "If you want to keep making passwords press y and if you want to view passwords press n: y/n ")
        if quit_choice == "n":
            return password_history
    return password_history


def view_passwords(password_history):
    view_choice = input("Do you want to view passwords and if not press y otherwise press any other alphabet key: ")
    if view_choice.lower() == "y":
        sys.exit()
    else:
        print("Password History: ",password_history)

password_history = []

print("sign_up , make_passwords , view_passwords , all_functions are the functions you can type and use: ")
user_choice = input("Which function do you want to access: ")
if user_choice == "sign_up":
    print(sign_up())
elif user_choice == "make_passwords":
    print(make_passwords(password_history))
elif user_choice == "view_passwords":
    print(view_passwords(password_history))
elif user_choice == "all_functions":
    print(sign_up())
    print(make_passwords(password_history))
    print(view_passwords(password_history))
else:
    print("Please enter a valid name! 

