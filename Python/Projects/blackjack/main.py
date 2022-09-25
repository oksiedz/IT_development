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

# variable creation
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def calculate_sum_of_cards(deck):
    """function calculates sum of card in the deck
    returns sum of cards"""
    sum_of_cards = 0
    for card in deck:
        sum_of_cards += card
    return sum_of_cards


def add_card(deck):
    """function selects the random card and add it to the deck
    if the card is ace and sum of cards with ace is higher than 21
    then it counts ace as 1
    returns extended deck"""
    new_card = random.choice(cards)
    if new_card == 11 and (calculate_sum_of_cards(deck) + new_card) > 21:
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
    if calculate_sum_of_cards(deck_of_player) > 21:
        return 1
    elif calculate_sum_of_cards(deck_of_dealer) == 21:
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
    print(f"Your deck is: {show_cards(deck, 1)}, with sum of cards equal = {calculate_sum_of_cards(deck)}")


def play_blackjack():
    game_over = False
    while not game_over:
        # empty decks
        players_deck = []
        dealers_deck = []
        # two cards for computer and for player
        for i in range(2):
            players_deck.append(random.choice(cards))
            dealers_deck.append(random.choice(cards))

        # first check if after first cards game can continue
        if check_two_card_conditions(deck1=players_deck, deck2=dealers_deck) == 0:
            game_over = True

        print(f"First card of the dealer is: {show_cards(dealers_deck, 0)}")
        print_players_deck(players_deck)

        take_next_card = ""
        while take_next_card not in ("yes","no"):
            take_next_card = input("Do you want to take another card? yes/no").lower()
            if take_next_card == "yes":
                game_over = False
                # take new card and check game over conditions
            elif take_next_card == "no":
                game_over = True
                # stop taking cards for the player and continue with dealer

        # check of game status to be checked after each card is taken
        if check_game_status(deck_of_player=players_deck, deck_of_dealer=dealers_deck) == 1:
            print("Player's cards exceed 21 - you lose")
            game_over = True
        elif check_game_status(deck_of_player=players_deck, deck_of_dealer=dealers_deck) == 2:
            print("Dealer has blackjack - you lose")
            game_over = True

        print(players_deck)
        print(calculate_sum_of_cards(players_deck))

        print(dealers_deck)
        print(calculate_sum_of_cards(dealers_deck))

        game_over = True
