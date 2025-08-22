from bs4 import BeautifulSoup
import requests, lxml

URL = 'https://news.ycombinator.com/news'

def fetch_html(url: str):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

content = fetch_html(url=URL)
print(f'{content=}')

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(content, 'lxml')

# Find all the <a> tags in the HTML
# <a href="https://www.jofreeman.com/joreen/tyranny.htm">The Tyranny of Structurelessness (1970)</a>
anchor_tags = soup.select(selector='span.titleline > a')
# <span class="score" id="score_42786962">1520 points</span>
# Find all the points element in the HTML
point_elements = soup.select(selector='span.score')

max = 0
index = 0
# Find the article with the highest pozints
for point in point_elements:
    point_int = int(point.get_text().split()[0])
    if point_int > max:
        max = point_int
        index = point_elements.index(point)
        

output = f'Article with the highest points: {anchor_tags[index].getText()}({anchor_tags[index].get('href')}) with {max} score'
print(output)

with open('output.text', 'a') as file:
    file.write(+ output + '\n')



#     if max < point.string():