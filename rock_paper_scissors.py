# Exercise 8
# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
# Remember the rules:
# Rock beats scissors
# Scissors beats paper
# Paper beats rock

import random

new = True
while new:
    print("\nRock Paper Scissors\n1. Rock\n2. Paper\n3. Scissors\n")
    user = int(input("Input your choice : "))
    comp = random.randint(1, 3)

    if user == comp:
        print("It's a draw")
    elif user == 1 and comp == 3:
        print("Congratulations! Rock beats Scissors, User Wins")
    elif user == 1 and comp == 2:
        print("Oh no! Paper beats Rock, Computer Wins")
    elif user == 2 and comp == 1:
        print("Congratulations! Paper beats Rock, User Wins")
    elif user == 2 and comp == 3:
        print("Oh no! Scissors beat Paper, Computer Wins")
    elif user == 3 and comp == 1:
        print("Oh no! Rock beats Scissors, Computer Wins")
    elif user == 3 and comp == 2:
        print("Congratulations! Scissors beat Paper, User Wins")
    else:
        print("Invalid choice")
        
    new = input("Enter 'y' to play again or 'n' to stop: ").lower() == 'y'

