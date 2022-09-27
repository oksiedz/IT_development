# import from other files
from graphics import logo
import random

print(logo)


def check_if_int(variable):
    try:
        int(variable)
        return True
    except ValueError:
        return False


def set_repetition_number(difficulty_level):
    if difficulty_level == "easy":
        return 10
    else:
        return 5


def ask_difficulty_level():
    level = ""
    while level not in ("easy", "hard"):
        level = input("Choose the difficulty level: easy or hard: ").lower()
    return level


def no_more_guesses(number):
    print(f"You lost. You didn't guess the number {number}")


def starting_new_game():
    start_new_game = ""
    while start_new_game not in ("yes", "no"):
        start_new_game = input("Do you want to start the new game? yes or no: ").lower()

    if start_new_game == "no":
        print("This is the end of game. Thank you for playing.")
        return 0
    else:
        play_game()


def play_game():

    max_number = ""
    while not check_if_int(max_number):
        max_number = input("Please provide max number in range for computer random number selection: ")

    print(f"I selected randomly number between 1 and {max_number}.")

    SELECTED_NUMBER = random.randint(1, int(max_number))
    REPETITION = set_repetition_number(ask_difficulty_level())
    available_repetition = REPETITION

    continue_guessing = True
    while continue_guessing:
        guessed_number = ""
        while not check_if_int(guessed_number):
            print(f"You have available {available_repetition} guesses.")
            guessed_number = input("Please guess the number: ")

        guessed_number = int(guessed_number)

        if guessed_number == SELECTED_NUMBER:
            print(f"Bravo, you guessed the number in {REPETITION - available_repetition - 1} attempts.")
            continue_guessing = False
            available_repetition = 0
            starting_new_game()
        elif guessed_number > SELECTED_NUMBER:
            print("Guessed number is too high.")
            continue_guessing = True
            available_repetition -= 1
            if available_repetition == 0:
                no_more_guesses(SELECTED_NUMBER)
                continue_guessing = False
                starting_new_game()
        else:
            print("Guessed number is too low.")
            continue_guessing = True
            available_repetition -= 1
            if available_repetition == 0:
                no_more_guesses(SELECTED_NUMBER)
                continue_guessing = False
                starting_new_game()

    # Task list
    # 1. Computer selects the random number ==> Done
    # 2. Set the difficulty level ==> Done
    # 3. Guess the number and evaluate the result
    # 4. Repeat above till the end of repetition
    # 5. Check if number is the one which was selected
    # 6. Finish repetition when the selected number was guessed
    # 7. Start new/game, or finish

play_game()