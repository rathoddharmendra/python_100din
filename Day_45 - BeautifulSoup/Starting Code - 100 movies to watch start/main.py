import requests
from bs4 import BeautifulSoup
import lxml, os

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
filename = os.path.join(os.path.dirname(__file__),'movies.txt')
# Write your code below this line 👇

# <h3 class="title">99) Raging Bull</h3>

response = requests.get(URL)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'lxml')

title_element = soup.find_all(name='h3', class_='title')
# titles = []

# for title in title_element.reverse():
#     try:
#         titles.append(title.getText().split(')')[1].strip())
#     except Exception as e:
#         print('No titles found.')

with open(filename, 'w') as file:
    index = 1
    for title in title_element[::-1]:
        file.write(f'{title.text.strip()} {'\n'}')
        index += 1

