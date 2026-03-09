import random
import logo_art

EASY_LEVEL_ATTEMPT = 10
HARD_LEVEL_ATTEMPT = 5

def set_difficulty(level_choosen):
    if level_choosen == "easy":
        return EASY_LEVEL_ATTEMPT
    else:
        return HARD_LEVEL_ATTEMPT
    
def check_number(guessed_number,answer,attempts):
    if guessed_number<answer:
        print("Your guess is too low")
        return attempts-1
    elif guessed_number>answer:
        print("Your guess is too high")
        return attempts-1
    else:
        print(f"Your guess is coorect to the number{answer}")

def game():
    print(logo_art.logo)
    print("Let me think a number between 1 to 50")
    answer = random.randint(1,50)
    # print(answer)
    level = input("Choose the level easy or hard : ")
    attempts = set_difficulty(level)

    guessed_number= 0
    while guessed_number != answer:
        print(f"You have number of {attempts} left to guess the number")
        guessed_number = int(input("Guessed the number: "))
        attempts =check_number(guessed_number,answer,attempts)
        if attempts == 0:
            print("You are out of guess ... you loss")
            return
        elif guessed_number != attempts:
            print("Guess again")

game()