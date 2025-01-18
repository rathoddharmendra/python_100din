import datetime as dt
import os
import pandas 
filename = os.path.join(os.path.dirname(__file__), 'birthdays.csv')

class Persons:
    def __init__(self):
        try:
            self.df = pandas.read_csv(filename)
        except FileNotFoundError:
            raise FileNotFoundError(f'Could not find file: {filename}')
        else:
            self.persons = [Person(row['name'], row['email'],row['month'],row['day']) for index, row in self.df.iterrows()]
        
    def __iter__(self):
        return iter(self.persons)
class Person:
    def __init__(self, name: str, email: str, month: int, day: int):
        self.name = name.title()
        self.email = email.lower()  # Normalize email to lowercase for comparison purposes.  # type: str
        self.month = month
        self.day = day
        self.calculate_birthday()  # Calculate the birthday date immediately upon object creation.  # type: dt.datetime
        self.is_birthday = self.is_birthday_today()
    
    def calculate_birthday(self):
        """
        Calculate the birthday date for the given month and day.
        Returns:
            birthday = datetime object: The calculated birthday date.
        """
        current_year = dt.datetime.now().year
        self.birthday = dt.datetime(current_year, self.month, self.day)

    def is_birthday_today(self):
        if self.birthday.month == dt.datetime.now().month and self.birthday.day == dt.datetime.now().day:
            return True
        return False

