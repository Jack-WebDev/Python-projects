
import random

name = input("What's your name?: ").upper()
print(f"Hello {name}, Welcome to Password Generator!\n")

characters = "qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM1234567890!@#$_-"

number_of_passwords = int(input(f"So {name}, how many passwords do you want to generate?: "))
length_of_password = int(input("How many characters must the password contain?: "))

print("\nBelow are your generated password(s): ")

count = 0

for pwd in range(number_of_passwords):
    if number_of_passwords > 1:
        count +=1
        passwords = ''

    for len in range(length_of_password):
        passwords += random.choice(characters)
    print(f"{count}. {passwords}")
