# game.py

print("Rock, Paper, Scissors, Shoot!")
user_choice = input ("Choose one of 'Rock', 'Paper', 'Scissors': ")

if (user_choice == "Rock") or (user_choice == "Paper") or (user_choice == "Scissors"):
    print("VALID entry! Your choice is: ", user_choice)

else:
    print("Sorry this is not a valid entry... please check for typos and try again!")
    quit()

valid_options = ["Rock","Paper","Scissors"]
computer_choice = random.choice(valid_options)
print ("the computer choice is:", computer_choice)

if (user_choice == "Rock") and (computer_choice == "Scissors"):
    print ("You WIN!")

elif (user_choice == "Paper") and (computer_choice == "Rock"):
    print ("You WIN!")

elif (user_choice == "Scissors") and (computer_choice == "Paper"):
    print ("You WIN!")

elif (computer_choice == "Rock") and (user_choice == "Scissors"):
    print ("You LOSE!")

elif (computer_choice == "Paper") and (user_choice == "Rock"):
    print ("You LOSE!")

elif (computer_choice == "Scissors") and (user_choice == "Paper"):
    print ("You LOSE!")

elif (computer_choice == "Rock") and (user_choice == "Rock"):
    print ("TIE!")

elif (computer_choice == "Paper") and (user_choice == "Paper"):
    print ("TIE!")

elif (computer_choice == "Scissors") and (user_choice == "Scissors"):
    print ("TIE!")

else:
    print ("ERROR")

print ("THIS IS THE END OF OUR GAME, PLEASE PLAY AGAIN")