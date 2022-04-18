
import random

computer_name = "Deep Blue"
name = input("What's your name?: ").upper()

print(f"Hello {name}, Welcome to Rock, Paper, Scissors and 'Q' to quit\n")

player_wins = 0
computer_wins = 0

options = ["Rock", "Paper", "Scissors"]

while True:
    player_choice = input("Make a choice. Rock/Paper/Scissors: ").capitalize()

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


    elif player_choice == "Rock" and computer_choice == "Scissors":
        print("You won!")
        player_wins +=1
        print(f"You have {player_wins} wins")


    elif player_choice == "Paper" and computer_choice == "Rock":
        print("You won!")
        player_wins +=1
        print(f"You have {player_wins} wins")


    elif player_choice == "Scissors" and computer_choice == "Paper":
        print("You won!")
        player_wins +=1
        print(f"You have {player_wins} wins")

    else:
        print(f"{computer_name} wins. You're such a loser -_- ")
        computer_wins +=1
        print(f"{computer_name} has {computer_wins} wins")
        continue


