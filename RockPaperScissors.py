import random

user_score = 0
computer_score = 0
options = ["rock","paper","scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or q to Quit: ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue 
    random_number = random.randint(0,2) # This will assing the integers to the options we have mentioned 

    computer_input = options[random_number]
    print("The computer has picked: ",computer_input )

    if user_input== "rock" and computer_input == "scissors":
        print("You win" )
        user_score += 1

    elif user_input== "pcissors" and computer_input == "paper":
        print("You win")
        user_score += 1
    
    elif user_input== "paper" and computer_input == "Rock":
        print("You win")
        user_score += 1
    
    elif user_input == computer_input:
        print("It was a draw")

    else:
        print("You lose")
        computer_score += 1
print(" Your score is: ", user_score)
print("Computer score is: ", computer_score)
print("End of the game.")    
