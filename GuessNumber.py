
from random import randint

name = input("What's your name: ").upper()
print(f"\nHello {name}, Welcome to Guess The Number!")

player_input = input("\nType a max number (i.e 10 for 1-10. 50 for 1-50. 100 for 1-100): ")


if player_input.isdigit():
    player_input = int(player_input)

    if player_input <= 0:
        print(f"Type a number larger than 0 {name}")

else:
    print(f"Type a number {name}!!")

random_number = randint(0, player_input)

guess_count = 5

while True:

    player_guess = input("Enter your guess: ")

    if player_guess.isdigit():
        player_guess = int(player_guess)

        if player_guess == random_number:
            print(f"\nWell done {name}. That's correct!")
            break

        elif (player_guess > random_number) and (guess_count != 1):
            print(f"Your guess is too high {name}. Try again \n")
            guess_count -= 1
            print(f"You have {guess_count} guesses left!\n")

        elif (player_guess < random_number) and (guess_count != 1):
            print(f"Your guess is too low {name}. Try again!\n")
            guess_count -= 1
            print(f"You have {guess_count} guesses left!\n")
        
        else:
            print("Oops! You're out of guesses. You lose!")
            break

    else:
        print(f"Type a number {name}!!\n")

