#write functions here, don't add input('') statements here!

import random

def test_config():
    return True

def get_random_number(min, max):
    number = random.randint(min, max)
    return number

def random_guesser():
    choice = "Y"
    while (choice == "Y" or choice == "y"):
        value = get_random_number(1, 5)
        guess = int(input("Guess a number between 1 and 5: "))
        if guess == value:
            print("You win!")
            choice = input("Press 'Y' to play again: ")
            if choice == "Y" or "y":
                continue
            else:
                print("Thanks for playing.")
                break
        elif guess != value:
            input("Try again? (Y): ")
            if choice == ("Y" or "y"):
                continue
            else:
                print("Thanks for playing.")
                break

random_guesser()