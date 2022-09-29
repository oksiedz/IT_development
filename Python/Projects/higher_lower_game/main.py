from game_data import data
from random import choice
from art import logo, vs


def start_new_game():
    answer = ""
    while answer not in ("yes", "no"):
        answer = input("Do you want to play new game? yes/no ").lower()
    if answer == "yes":
        higher_lower_game()
    else:
        return


def higher_lower_game():
    score = 0
    the_end = 0
    first_choice = {}
    second_choice = {}
    list_of_options = data

    while the_end == 0:
        if score == 0:
            first_choice = choice(data)
            data.remove(first_choice)
        else:
            first_choice = second_choice

        second_choice = choice(data)
        data.remove(second_choice)

        print(logo)
        if score != 0:
            print(f"You are right! Current score: {score}")
        print(f"Compare A: {first_choice['name']}, a {first_choice['description']}, from {first_choice['country']}")
        print(vs)
        print(f"Against B: {second_choice['name']}, a {second_choice['description']}, from {second_choice['country']}")
        answer = ""
        while answer not in ("a", "b"):
            answer = input("Who has more followers? A or B: ").lower()

        if answer == "a" and first_choice['follower_count'] > second_choice['follower_count'] or answer == "b" and first_choice['follower_count'] < second_choice['follower_count']:
            score += 1
        else:
            the_end = 1

        if len(list_of_options) == 0:
            the_end = 2

        if the_end == 1:
            print(f"Sorry that's wrong. Final score {score}")
            start_new_game()
        elif the_end == 2:
            print(f"You answered correctly all comparisons. Bravo, your final score {score}")
            start_new_game()


higher_lower_game()