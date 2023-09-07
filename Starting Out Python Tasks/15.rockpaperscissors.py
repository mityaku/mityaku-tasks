import random #imports the random module
import random
choices = ["R", "P", "S"] #A list of choices the program chooses from
choice = input().upper() #Allows the user to enter their choice
randomChoice = random.choice(choices) #Picks a random choice from the list of choices

if choice == randomChoice: #compares the user choice to the random choice
    print("Tie") #prints tie indicating that the user has lost
elif ((choice == "R" and randomChoice == "S") or (choice == "P" and randomChoice == "R") or (choice == "S" and randomChoice == "P")): #Makes if statements that compare the values to winning values
    print("You win") #Prints "You Win" indicating that the user has won
else: #A final else statement to print out that the user has lost
    print("You loose") #Prints "You loose" indicating that the user has lost
#end if