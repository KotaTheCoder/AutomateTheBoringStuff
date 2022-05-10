import random, sys
print("Rock, Paper, Scissors")

#These variables keep track of the number of wins, losses and ties.
wins = 0
losses = 0
ties = 0

while True: # Main game loop
    print("%s Wins, %s Losses, %s Ties" % (wins, losses, ties))
    while True: #Player input loop
        print("Enter your move: (r)ock, (p)aper, (s)cissors, or (q)uit")
        playerMove = input()

        if playerMove == 'q':
            sys.exit() #quit the program

        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break

        print("type one of r, p, s, or q.")

    #Display player choice
    if playerMove == "r":
        print("Rock versus...")
    elif playerMove == "p":
        print("Paper versus...")
    elif playerMove == 's':
        print("Scissors versus...")

    secret_number = random.randint(1, 3)
    computerMove = ""
    if secret_number == 1:
        computerMove = "r"
        print("Rock")
    elif secret_number == 2:
        computerMove = "p"
        print("Paper")
    elif secret_number == 3:
        computerMove = "s"
        print("Scissors")

    if playerMove == computerMove:
        print("It's a tie!")
        ties += 1
    elif playerMove == "r" and computerMove == "s":
        print ("You win!")
    elif playerMove  == "p" and computerMove == "r":
        print("You win!")
        wins += 1
    elif playerMove == "s" and computerMove == "p":
        print("You win!")
        wins += 1
    elif playerMove == "r" and computerMove == "p":
        print("You lose!")
        losses += 1
    elif playerMove == "p" and computerMove == "s":
        print("You lose!")
        losses += 1
    elif playerMove == "r" and computerMove == "p":
        print("You lose!")
        losses += 1
    elif playerMove == "s" and computerMove == "r":
        print("You lose!")
        losses += 1


