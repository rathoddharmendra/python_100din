import requests
from bs4 import BeautifulSoup
import lxml, os

BASE_URL = 'https://www.billboard.com/charts/hot-100/'

# Create a directory for storing the HTML files
filename = os.path.join(os.path.dirname(__file__), 'billboard_')
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

# Write your code below this line ��
class BillBoard:
    '''Class representing a Billboard Hot 100 chart for a given year.'''
    def __init__(self):
        '''Initialize the Billboard object with the given year.'''
        self.set_new_billboard_date()
        # self.billboard_date = input('Enter a year to search the billboard (in YYYY-MM-DD format): ')
        self.url = f'{BASE_URL}{self.billboard_date}'
        
    def set_new_billboard_date(self):
        '''Update the Billboard object with the next year's Billboard Hot 100 chart.
        Return:
         new_billboard_date [str]: the new Billboard date in YYYY-MM-DD format.
         '''
        # Implement this method to find the next year's Billboard Hot 100 chart and update the Billboard object.
        self.billboard_date = input('Enter a year to search the billboard (in YYYY-MM-DD format): ')

    def get_top_songs(self):

        '''Implement this method to fetch the top 100 songs from the Billboard Hot 100 chart for the given year. 
        Return:
         song-titles [list[tuple[str, str]]]: a list of song titles.
         '''
        response = requests.get(self.url, headers=header) 
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'lxml')
        
        soup_song_titles = soup.select(selector='h3#title-of-a-story.a-no-trucate')
        soup_authors = soup.select(selector='h3#title-of-a-story + span')
        # print(song_titles)
        # print(authors)
        song_titles = []
        # with open(f'{filename}{self.billboard_date}', mode='w') as file:
        for i, (title, author) in enumerate(zip(soup_song_titles, soup_authors), start=1):
                # print(f'{title}: By {author}')
                # file.write(f'{title.getText().strip()} -by- {author.getText().strip()}\n')
            song_titles.append((f'{title.getText().strip()}',f'{author.getText().strip()}'))
            # <h3 id="title-of-a-story" class="c-title  a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet">
        return ({"date": self.billboard_date , "titles": song_titles[:10]})
            # <span class="c-label  a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only u-font-size-20@tablet">
            # first_story_paragraph.find_next_sibling("p")

# bill_board = BillBoard()
# bill_board.billboard_date

# top_songs = bill_board.get_top_songs()
# top_songs_1 = bill_board.get_top_songs()
# print(top_songs)