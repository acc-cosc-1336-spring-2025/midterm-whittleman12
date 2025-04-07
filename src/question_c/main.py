#add import
import question_c

def random_guesser():
    choice = "Y"
    while (choice == "Y" or choice == "y"):
        value = question_c.get_random_number(1, 5)
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
            choice = input("Try again? (Y): ")
            if choice == "Y" or "y":
                
                continue
            else:
                print("Thanks for playing.")
                break

random_guesser()