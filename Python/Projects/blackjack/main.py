# ############## Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

# import section
import random


def add_card(deck):
    """function selects the random card and add it to the deck
    if the card is ace and sum of cards with ace is higher than 21
    then it counts ace as 1
    returns extended deck"""
    # variable creation
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    new_card = random.choice(cards)
    if new_card == 11 and (sum(deck) + new_card) > 21:
        new_card = 1
    deck.append(new_card)
    return deck


def show_cards(deck, mode):
    """function shows the cards from a deck
    mode = 0 only first card
    mode = 1 all cards"""
    if mode == 0:
        return deck[0]
    elif mode == 1:
        return deck


def check_game_status(deck_of_player, deck_of_dealer):
    """function checks end of game conditions:
    - if sum of players cards exceeds 21 - player loses return 1
    - if sum of dealers cards is 21 - player loses return 2"""
    if sum(deck_of_player) > 21:
        return 1
    elif sum(deck_of_dealer) == 21:
        return 2


def check_two_card_conditions(deck1, deck2):
    """deck 1 - players deck
    deck 2 - dealers deck
    it's checking if two first cards give blackjack"""
    if 10 in deck2 and 11 in deck2:
        print("Dealer's blackjack - you lose")
        return 0
    elif 10 in deck1 and 11 in deck1:
        print("Player's blackjack - you won")
        return 0


def print_players_deck(deck):
    print(f"Your deck is: {show_cards(deck, 1)}, with sum of cards equal = {sum(deck)}")


def calculate_score(deck):
    """Function Calculates the score"""
    # if there are two cards, and it's blackjack - specific situation
    if len(deck) == 2 and sum(deck) == 21:
        return -1
    return sum(deck)


def play_blackjack():
    # empty decks
    players_deck = []
    dealers_deck = []

    # two cards for computer and for player
    for i in range(2):
        add_card(deck=players_deck)
        add_card(deck=dealers_deck)

    # flag for game loop
    game_over = False
    while not game_over:
        # calculation of the sum of cards
        user_score = calculate_score(players_deck)
        dealers_score = calculate_score(dealers_deck)

        print_players_deck(players_deck)
        print(f"First card of the dealer is: {show_cards(dealers_deck, 0)}")

        # if after two cards, and it's blackjack or player has more than 21 - game_over
        if user_score == -1 or dealers_score ==-1 or user_score > 21:
            game_over = True
        else:
            take_next_card = ""
            while take_next_card not in ("yes", "no"):
                take_next_card = input("Do you want to take another card? yes/no\n").lower()
                if take_next_card == "yes":
                    # take new card
                    add_card(deck=players_deck)
                elif take_next_card == "no":
                    # stop taking cards for the player
                    game_over = True

play_blackjack()