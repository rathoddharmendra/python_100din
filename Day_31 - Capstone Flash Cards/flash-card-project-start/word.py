import csv, random
import pandas as pd
import os

# generates random word list
LANG = 'German'
FILE = 'german.csv'
class WordListGenerator:
    def __init__(self):
        try:
            filename = os.path.join(os.path.dirname(__file__), 'data/saved_' + FILE)
            self.df: pd.DataFrame = pd.read_csv(filename, delimiter=',') 
        except FileNotFoundError:
            filename = os.path.join(os.path.dirname(__file__), 'data/' + FILE)
            self.df: pd.DataFrame = pd.read_csv(filename, delimiter=',') 
        finally:
            print(filename)
            self.word_list = self.df.to_dict(orient='records')
            print(self.word_list)
            # self.word_dict = {index: [row[LANG],row['English']] for index, row in self.df.iterrows()}  # convert to list for easier manipulation
    
    def send_row(self):
        """Return a random LANG-English word pair"""
        if len(self.word_list) > 0:
            return random.choice(self.word_list)
        else:
            return None

    def remove_row(self, card: dict) -> None:
        """Remove the word with the given index from the list"""
        self.word_list.remove(card)
        self.new_df = pd.DataFrame(self.word_list)
        self.new_df.to_csv(os.path.join(os.path.dirname(__file__), 'data/saved_' + FILE), index=False)