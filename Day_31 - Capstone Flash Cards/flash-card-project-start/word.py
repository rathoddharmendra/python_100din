import csv, random
import pandas as pd
import os

# generates random word list
LANG = 'German'
file = './data/german.csv'
class WordListGenerator:
    def __init__(self):
        filename = os.path.join(os.path.dirname(__file__), file)
        self.df: pd.DataFrame = pd.read_csv(filename, delimiter=',') 
        self.word_dict = {index: [row[LANG],row['English']] for index, row in self.df.iterrows()}  # convert to list for easier manipulation
    
    def send_row(self):
        """Return a random LANG-English word pair"""
        if len(self.word_dict) > 0:
            chosen_index = random.choice([index for index in self.word_dict])
            return (chosen_index, self.word_dict[chosen_index])
        else:
            return None

    def remove_row(self, index: int) -> None:
        """Remove the word with the given index from the list"""
        print(f'removing {self.word_dict[index]}')
        del self.word_dict[index]