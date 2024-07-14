import random,sys
print("Welcome to number guessing game")
Attemps = 0
Wins = 0

while True:
    print(f"Attemps , Wins {Attemps} , {Wins}")
    while True:
        print("Please choose your number between 1 and 7 ")
        print("You can quit the game if you want by pressing q")
        playerInput = int(input("Enter your number/move here "))
        if playerInput == "q":
            sys.exit()
        computerMove = random.randint(1,7)
        if playerInput == computerMove:
            print("You guessed the number")
            Wins = Wins+1
        elif playerInput != computerMove:
            Attemps = Attemps+1
            break
        else:
            print("Better luck next time")
