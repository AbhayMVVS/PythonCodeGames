"""
Title: PIG Dice Game 

This code simulates a dice game where there are multiplayers (range of 2 to 4 players in this code) who can take turns to roll the dice. 
The Rules are as follows:
(1) You get the choice to roll the dice, and if you get a number between 2 and 6, you get another turn and the score will keep adding up 
(2) But if you roll a 1, your score will go back to 0 
(3) You get to choose the maximum score limit till which you want to play the game for.

NOTE: There can be a chance where a player may have more the the max score limit, but this way we can ensure that every player has got equal number of turn overall.

"""
import random
def roll():
    min_val = 1
    max_val = 6
    roll = random.randint(min_val, max_val)
    return roll

while True:
    players_num = input("How many players do you wish to play with (1-4)? ")
    if  players_num.isdigit() and 2 <= int(players_num) <= 4 :
        players = int(players_num)
        
        if 2 <= int(players) <= 4:
            break
    else:
        print("Sorry,it must be between 2 to 4 players. Try again.")

print("You chose to play with ", players, "players.")

while True:
    max_score = input("\nEnter the maximum score limit you want to play the game for: ")
    if max_score.isdigit():
        max_score = int(max_score)
        break
    else:
        print("Invalid input!")
player_scores = [0 for i in range(players)]
print(player_scores)

while max(player_scores) < max_score:
    for p in range(players):
        print("\nPlayer",p+1,"turn has started!\n")
        print("Reminder! Your total score is:", player_scores[p],"\n")
        curr_score = 0 
        
        while True:
            dice_roll = input("Do you want to roll the dice (y/n)? ")
        
            if dice_roll.lower() != "y" and dice_roll.lower() != "n":
                print("Invalid input, enter Y or N")
                continue
            elif dice_roll.lower() == "n":
                break
        
            value = roll()
            if value == 1:
                print("You got a 1! Your turn is done.")
                curr_score = 0
                break
            else:
                print("You got a",str(value) + "!" )
                curr_score += value
                print("Your current score is: ",curr_score)
        player_scores[p] += curr_score
        print("Your total score is:", player_scores[p])

print("\nOverall scores: ",player_scores)
max_score = max(player_scores)
winner = player_scores.index(max_score)
print("\nPlayer",winner+1,"is the winner with a score of:", max_score )


