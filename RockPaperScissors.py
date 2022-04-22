
import random
from time import sleep

computer_name = "Deep Blue"
name = input("What's your name?: ").upper()

print("\nLoading....")
sleep(2)

print(f"\nHello {name}, Welcome to Rock, Paper, Scissors. \n")

sleep(2)

print("Loading game....")
sleep(2)

player_wins = 0
computer_wins = 0

options = ["Rock", "Paper", "Scissors"]

while True:


    player_choice = input("\nMake a choice. Rock/Paper/Scissors or 'Q' to quit: ").capitalize()
    sleep(1.5)

    if player_choice == 'Q':
        print(f"\nYou have {player_wins} wins. {computer_name} has {computer_wins} wins.")
        print("Goodbye!")
        break

    if player_choice not in options:
        continue

    computer_choice = random.choice(options)
    print(f"\n{computer_name} chose {computer_choice}.\n")

    if player_choice == computer_choice:
        print("It's a TIE!")
        sleep(2)


    elif player_choice == "Rock" and computer_choice == "Scissors":
        print("You win!")
        sleep(1.5)
        player_wins +=1
        print(f"You have {player_wins} wins")
        sleep(2)



    elif player_choice == "Paper" and computer_choice == "Rock":
        print("You win!")
        sleep(1.5)
        player_wins +=1
        print(f"You have {player_wins} wins")
        sleep(2)



    elif player_choice == "Scissors" and computer_choice == "Paper":
        print("You win!")
        sleep(1.5)
        player_wins +=1
        print(f"You have {player_wins} wins")
        sleep(2)


    else:
        print(f"{computer_name} wins. You're such a loser -_- ")
        sleep(1.5)
        computer_wins +=1
        print(f"{computer_name} has {computer_wins} wins")
        sleep(2)
        continue
        
        


