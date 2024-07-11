import random

options = "rock","paper","scissor"
user_choice = input("Please choose either rock paper or scissor ").lower()
while user_choice not in options:
    user_choice = input("Please enter a valid value: ")
computer_choice = random.choice(options)
if user_choice == computer_choice:
    print("It's a tie")
elif user_choice == "rock" and computer_choice == "paper":
    print("Computer won!")
elif user_choice == "rock" and computer_choice == "scissor":
    print("You won! ")
elif user_choice == "paper" and computer_choice == "rock":
    print("You won!")
elif user_choice == "paper" and computer_choice == "scissor":
    print("Computer won!")
elif user_choice == "scissor" and computer_choice == "paper":
    print("You won!")
elif user_choice == "scissor" and computer_choice == "rock":
    print("Computer won!")

