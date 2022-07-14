# game.py
import random
import os

print("Rock, Paper, Scissors, Shoot!")
user_choice = raw_input ("Choose one of 'Rock', 'Paper', 'Scissors': ")

user_choice = user_choice.lower()

if (user_choice == "rock") or (user_choice == "paper") or (user_choice == "scissors"):
    print("VALID entry! Your choice is: ", user_choice)

else:
    print("Sorry this is not a valid entry... please check for typos and try again!")
    quit()

valid_options = ["rock","paper","scissors"]
computer_choice = random.choice(valid_options)
print ("the computer choice is:", computer_choice)

if (user_choice == "rock") and (computer_choice == "scissors"):
    print ("You WIN!")

elif (user_choice == "paper") and (computer_choice == "rock"):
    print ("You WIN!")

elif (user_choice == "scissors") and (computer_choice == "paper"):
    print ("You WIN!")

elif (computer_choice == "rock") and (user_choice == "scissors"):
    print ("You LOSE!")

elif (computer_choice == "paper") and (user_choice == "rock"):
    print ("You LOSE!")

elif (computer_choice == "scissors") and (user_choice == "paper"):
    print ("You LOSE!")

elif (computer_choice == "rock") and (user_choice == "rock"):
    print ("TIE!")

elif (computer_choice == "paper") and (user_choice == "paper"):
    print ("TIE!")

elif (computer_choice == "scissors") and (user_choice == "scissors"):
    print ("TIE!")

else:
    print ("ERROR")

print ("THIS IS THE END OF OUR GAME, PLEASE PLAY AGAIN")