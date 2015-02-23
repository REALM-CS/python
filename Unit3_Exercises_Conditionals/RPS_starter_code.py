import random
import sys

# This function collects the human's choice: rock, paper or scissors.
def makeYourChoice():
    userChoice = raw_input("Let's play! Enter rock, paper or scissors:").lower()
    if userChoice == "rock" or userChoice == "paper" or userChoice == "scissors":
        return userChoice
    elif userChoice == "no" or userChoice == "quit":
        sys.exit(0)
    else:
        print "Nope, not valid. Try again."
        makeYourChoice()

# This function collects the computer's choice: rock, paper or scissors.
def computerRandom():
    options = ["rock","paper","scissors"]
    randomChoice = random.randint(0,2)
    return options[randomChoice]

# This function below takes two parameters, humanChoice and computerChoice, and compares them according to the rules of RPS.
# This is where we should learn whether the human or the computer has won, based on their choices.
# This is the only function you need to write, and the only part of the entire program you need to edit.

def comparison(humanChoice, computerChoice):









# This is the program that actually calls the functions above. Without this part, the program will not run.
while True:
    humanChoice = makeYourChoice()
    computerChoice = computerRandom()

    print "You chose", humanChoice
    print "The computer chose", computerChoice

    comparison(humanChoice, computerChoice)
    print " " # This prints a space between rounds.

# This game does not keep score, but we will implement a score function soon.
# This project is a variation on a problem written by Trevor Appleton.


