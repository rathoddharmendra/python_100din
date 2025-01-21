import requests, os, json
from html import unescape

API_KEY = os.environ.get('NEWS_API')
BASE_URL = 'https://newsapi.org/v2/everything'

# example: https://newsapi.org/v2/everything?q=Tesla%20Inc&sortBy=popularity&language=en&pageSize=3&apiKey=02681927410544b984e1fc850852a140

class NewsAPI:
    def __init__(self, stock_name: str):
        self.url = BASE_URL
        self.parameters = {
            'q': stock_name,
            'sortBy': 'popularity',
            'language': 'en',
            'pageSize': 3,
            'apiKey': API_KEY
        }

    def get_news(self) -> tuple[str, str]:
        response = requests.get(self.url, params=self.parameters)
        response.raise_for_status()
        data = response.json()

        with open(os.path.join(os.path.dirname(__file__),'news.json'), mode='w') as news_file:
            json.dump(data, news_file, indent=4)
        headline = data['articles'][0]['title']
        brief = unescape(data['articles'][0]['content'])
        return (headline, brief)
    

