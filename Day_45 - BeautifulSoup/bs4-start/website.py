import os
from bs4 import BeautifulSoup
import lxml

# Parse the HTML content using BeautifulSoup
filename = os.path.join(os.path.dirname(__file__), 'website.html')
with open(filename, 'r') as file:
    content = file.read()
    # print(content)

soup = BeautifulSoup(content, 'html.parser')
# soup = BeautifulSoup(content, 'lxml')

# print(soup.find_all(name='li')) # find all li elements
# print(soup.title)

# anchor_tags = soup.find_all(name='a')
# for anchor in anchor_tags:
#     # href = anchor.get('href') # get value of the attributes
#     print(anchor.getText()) # get value of the element text

# find element by id
heading = soup.find(name='h1', id='name')
print(heading.getText())

# find element by class
company_url = soup.select_one(selector="p a").get('href')
print(company_url) # get value of the attribute