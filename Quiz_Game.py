
import time


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print("Let's Get Quizzical!")


name = input("What is your name?: ").upper()

time.sleep(1)
print(f"Hello {name}, Welcome to Let's Get Quizzical!\n")
time.sleep(2)
print("Loading....\n")
time.sleep(3)

while True:

    guesses = 3
    points = 0

    print("There's 3 categories to choose from: \n 1. History \n 2. Science \n 3. General True/False")
    time.sleep(1.5)
    quiz_category = int(input("Which category would you like?: "))

    if quiz_category == 1:
        time.sleep(1.3)
        print("\nLet me get my time machine while you get ready!")
        time.sleep(1.5)
        print("Game will be ready in :")
        countdown(5)
        time.sleep(1.1)

        Q1 = input("\n1. Which country started World War 2?: ").title()

        if Q1 == "Germany":
            print("\nThat's correct. That was an easy one. Let's get serious now!")
            points += 1
            time.sleep(1.3)
            print(f"You have {points} point!\n")

        else:
            print(
                f"\nWrong! That was such an easy one {name}. The answer is Germany.")
            guesses -= 1
            time.sleep(1.3)
            print(f"You have {guesses} guesses left\n")

        Q2 = input(
            "2. Which continent is said to the the origin of Mankind?: ").title()

        if Q2 == "Africa":
            print("\nThat's correct! Get ready for another one.")
            points += 1
            time.sleep(1.3)
            print(f"You have {points} points!\n")

        else:
            print(f"\nOh {name}, that was Wrong!. The answer is Africa.")
            guesses -= 1
            time.sleep(1.3)
            print(f"You have {guesses} guesses left\n")

        Q3 = input(
            "Which country was the first to create a civilized society?: ").title()

        if Q3 == "Egypt":
            print("That's correct! You're really good.")
            points += 1
            time.sleep(1.3)

            if points == 3:
                print(
                    f"\nYou have {points} points! \nYou win!! But you just got lucky -_-")

            else:
                print(f"\nYou have {points} points. You won! But barely.")

            break

        else:
            print(f"\nWrong again! The answer is Egypt.")

            if points <= 1:
                print(
                    f"\nYou have {points} points. \nYou lost! Try another category :)")

            elif points == 2:
                print(f"\nYou have {points} points. You won! But barely.")
            break

    elif quiz_category == 2:
        print(
            f"Get your geek on {name}, and let's see if you give Einstein a run for his money")
        print("Game will be ready in :")
        countdown(5)
        time.sleep(1.1)

        Q1 = input(
            "\n1. Who wrote either Special Relativity or General Relativity?: ").title()

        if (Q1 == "Albert Einstein") or (Q1 == "Einstein"):
            print("That's correct. That was an easy one. Let's get serious now!")
            points += 1
            time.sleep(1.3)
            print(f"You have {points} point!")

        else:
            print(
                f"Wrong! That was such an easy one {name}. The answer is Albert Einstein.")
            guesses -= 1
            time.sleep(1.3)
            print(f"You have {guesses} guesses left")

        Q2 = input(
            "\n2. Which energy field gives particles their mass?: ").title()

        if (Q2 == "Higgs Field"):
            print(f"Correct {name}!")
            points += 1
            time.sleep(1.3)
            print(f"You have {points} point!")

        else:
            print(f"Wrong! The answer is Higgs Field.")
            guesses -= 1
            time.sleep(1.3)
            print(f"You have {guesses} guesses left")

        Q3 = int(
            input("\n3. How many laws of motion did Sir Isaac Newton theorize?: "))

        if (Q3 == 3):
            print("Correct again. Are you a science major? Because that's cheating :D")
            points += 1
            time.sleep(1.3)

            if points == 3:
                print(
                    f"\nYou have {points} points! \nYou win!! But you just got lucky -_-")

            else:
                print(f"\nYou have {points} points. You won! But barely.")

            break

        else:
            print(f"\nWrong again?! The answer is 3.")

            if points <= 1:
                print(
                    f"\nYou have {points} points. \nYou lost! Try another category :)")

            elif points == 2:
                print(f"\nYou have {points} points. You won! But barely.")
            break

    elif quiz_category == 3:
        print(f"Fast paced questions. Nice one {name}")
        time.sleep(1.5)
        print("Game will be ready in :")
        countdown(5)
        time.sleep(1.1)

        Q1 = input("\n1. The longest river in the world is the Amazon River: ").title()

        if Q1 == "False":
            print("That's correct. That was an easy one. Let's get serious now!")
            points += 1
            time.sleep(1.3)
            print(f"You have {points} point!")

        else:
            print(f"Wrong! Amazon is the largest, the Nile is the longest.")
            guesses -= 1
            time.sleep(1.3)
            print(f"You have {guesses} guesses left")
        
        Q2 = input("\n2. The Atlantic Ocean is the world’s biggest ocean: ").title()

        if Q2 == "False":
            print("That's correct.")
            points += 1
            time.sleep(1.3)
            print(f"You have {points} point!")

        else:
            print(f"Wrong! It is the Pacific Ocean.")
            guesses -= 1
            time.sleep(1.3)
            print(f"You have {guesses} guesses left")

        Q3 = input("\n3. The world’s best-selling music album of all times belongs to The Beatles: ").title()

        if Q3 == "False":
            print("That's correct! You're really good.")
            points += 1
            time.sleep(1.3)

            if points == 3:
                print(f"\nYou have {points} points! \nYou win!! But you just got lucky -_-")
                break

            else:
                print(f"\nYou have {points} points. You won! But barely.")
                break
            
        else:
            print(f"\nWrong again! The best-selling music album of all times is Michael Jackson’s 'Thriller'.")

            if points <= 1:
                print(f"\nYou have {points} points. \nYou lost! Try another category :)")
                break

            elif points == 2:
                print(f"\nYou have {points} points. You won! But barely.")
                break
            
    else:
        print(f"{name}, don't make me doubt your intelligence.")
        time.sleep(1.5)
        continue
