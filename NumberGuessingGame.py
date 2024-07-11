import random

options = ["1","2","3"]
user_choice = (input("Choose your number from 1 2 or 3: "))
computer_choice = (random.choice(options))
while user_choice not in options:
    user_choice = (input("Please enter a valid value: "))
if user_choice == computer_choice:
    print("You gusessed the number!")
else:
    print("Try again! ")
