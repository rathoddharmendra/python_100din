# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas, os

filename = os.path.join(os.path.dirname(__file__),'nato_phonetic_alphabet.csv')

data = pandas.read_csv(filename)
# data.to_dict()
#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [{letter: phonetic_dict[letter]} for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()

