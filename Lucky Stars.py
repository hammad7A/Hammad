import random, sys

stars = 0
attempts = 0
skulls = 0
print("There are 5 numbers and 1 correct guess = 1 star goodluck!")

while True:

    print(f"Stars({stars}) Attempts({attempts}) Skulls({skulls})")
    computer_roll = random.randint(0, 6)
    user_guesser = (input("Enter your number: (u can press q to quit) "))
    if user_guesser == "q":
        sys.exit()
    user_guesser = int(user_guesser)
    if user_guesser == computer_roll:
        print("You guessed the number")
        stars = stars+1
    else:
        print("You failed to guess the number! ")
        attempts = attempts+1
    if attempts == 10:
        skulls += 1
        attempts = 0
        if skulls == 5 and stars < 3:
            print("You failed the game! ")
            sys.exit()







    