import random, sys

print("ROCK PAPER SCISSORS ")
wins = 0
losses = 0
ties = 0
while True:
    print("% wins,% losses,% ties",(wins,losses,ties))
    while True:
        print("type (r)ock (p)aper (s)cissor or (q)uit")
        playerMove = input("Enter your move here! ")
        if playerMove == "q":
            sys.exit()
        if playerMove == "r" or playerMove == "p" or playerMove == "s":
            break
        print("Type r p s or q")
    if playerMove == "r":
        print("ROCK VERSUS...")
    elif playerMove == "p":
        print("PAPER VERSUS...")
    elif playerMove == "s":
        print("SCISSOR VERSUS...")

    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = "r"
        print("ROCK")
    elif randomNumber == 2:
        computerMove = "p"
        print("PAPER")
    elif randomNumber == 3:
        computerMove = "s"
        print("SCISSOR")

    if playerMove == computerMove:
        print("It's a tie!")
        ties = ties+1
    elif playerMove == "r" and computerMove == "p":
        print("Computer won! ")
        losses = losses+1
    elif playerMove == "r" and computerMove == "s":
        print("You won! ")
        wins = wins+1
    elif playerMove == "p" and computerMove == "r":
        print("You won! ")
        wins = wins+1
    elif playerMove == "p" and computerMove == "s":
        print("Computer won! ")
        losses = losses+1
    elif playerMove == "s" and computerMove == "r":
        print("Computer won!")
        losses = losses+1
    elif playerMove == "s" and computerMove == "p":
        print("You won! ")
        wins = wins+1
