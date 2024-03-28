# TODO 1. Create a dictionary in this format:

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas
nato_alphabet = pandas.read_csv("Input_files/nato_phonetic_alphabet.csv")
dictionary = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}
print(dictionary)

input_text = input("Please write text: ")

list_of_letters = [letter.upper() for letter in input_text if letter != " "]

list_of_alpha = [dictionary[letter] for letter in list_of_letters]
print(list_of_alpha)
