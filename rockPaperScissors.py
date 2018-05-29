#!/usr/bin/env python 3.4

from random import randint

def isValid(move):  #checks to see if the user input is valid
    if move == 'r' or move == 'p' or move == 's':
        return(True)
    else:
        return(False)


playerMove = input("Pick a move, rock (r), paper (p) or scissors (s): ")
if not isValid(playerMove):
    print("Error: Invalid move")
    quit()

computer = randint(1, 3)
if (computer == 1):
    computer = 'r'
elif (computer == 2):
    computer = 'p'
else:
    computer = 's'

print(playerMove, "vs", computer)
if (playerMove == computer):
    print("DRAW!")
elif (playerMove == 'r' and computer ==
      's') or (playerMove == 'p' and computer == 'r') or (playerMove == 's' and computer == 'p'):
    print("You Win")
else:
    print("Computer Win")
