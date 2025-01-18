from random import choice
import os

filename = os.path.join(os.path.dirname(__file__), 'quotes.txt')
class Quotes:
    def __init__(self):
        try:
            with open(filename) as f:
                self.quote = choice(f.readlines())
        except:
            raise('Could not open quotes file: %s' % filename)