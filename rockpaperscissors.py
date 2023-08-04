#Importing random module

import random

#The computer chooses rock, paper, or scissors and this choice is stored in "z"

choices = ["rock", "paper", "scissors"]
z = random.choice(choices)

#While true statement allows us to end the game when we need

while True:

    #Asking for user input for rock, paper, or scissors and storing that choice in "playerChoice"
    
    playerChoice = input("Rock, Paper, or Scissors?: ").lower()

    #Checking for tie between player and computer

    if playerChoice == z:
        print("Computer: " + z)
        print("You: " + playerChoice)
        print("Tie!")

    #Checking for player loss

    elif playerChoice == 'rock' and z == 'paper':
        print("Computer: " + z)
        print("You: " + playerChoice)
        print("You Lost :(")

    elif playerChoice == 'paper' and z == 'scissors':
        print("Computer: " + z)
        print("You: " + playerChoice)
        print("You Lost :(")

    elif playerChoice == 'scissors' and z == 'rock':
        print("Computer: " + z)
        print("You: " + playerChoice)
        print("You Lost :(")

    #Checking for player victory

    elif playerChoice == 'rock' and z == 'scissors':
        print("Computer: " + z)
        print("You: " + playerChoice)
        print("You Won! :)")

    elif playerChoice == 'paper' and z == 'rock':
        print("Computer: " + z)
        print("You: " + playerChoice)
        print("You Won! :)")

    elif playerChoice == 'scissors' and z == 'paper':
        print("Computer: " + z)
        print("You: " + playerChoice)
        print("You Won! :)")

    #If something other than rock, paper, or scissors was given as the input, the player will be told to put
    #a valid input

    else:
        print("Please Put In A Valid Choice")

    #At the end of each round we ask if the player wants to go again
    #If the player says yes, the while loop continues. If the player does not say yes, the while loop is
    #terminated

    playAgain = input("Do You Want To Play Again? yes/no: ").lower()
    if playAgain != 'yes':
        break

    #Bye!
    
print("Bye!")