import requests, os, json
from datetime import datetime, timedelta

class StockAnalyzer:
    def __init__(self, stock_symbol: str):
        self.url = 'https://www.alphavantage.co/query'
        self.parameters: dict = {
            'function': 'TIME_SERIES_DAILY',
            'symbol': stock_symbol,
            'apikey': os.environ.get('ALPHAVANTAGE_API_KEY')
        }

    def check_stock_variation(self) -> tuple[int, float]:
        response = requests.get(self.url, params=self.parameters)
        response.raise_for_status()
        data = response.json()
        with open(os.path.join(os.path.dirname(__file__),'data.json'), mode='w') as file:
            json.dump(data, file, indent=4)

        closing_day = data["Meta Data"]["3. Last Refreshed"]
        day_before_closing_day = self.get_day_before_closing_day(closing_day)
        closing_day_closing_price = float(data["Time Series (Daily)"][closing_day]["4. close"])
        day_before_closing_day_closing_price = float(data["Time Series (Daily)"][day_before_closing_day]["4. close"])
        
        # if there is a more than 5% gap, then there is a chance of volatility
        direction = 0 if closing_day_closing_price - day_before_closing_day_closing_price > 0 else -1
        closing_gap = abs(closing_day_closing_price - day_before_closing_day_closing_price)
        closing_gap_percentage = round((closing_gap / day_before_closing_day_closing_price) * 100, 2)
        return (direction, closing_gap_percentage)

    def get_day_before_closing_day(self, closing_day: str):
        yesterday_datetime_obj: datetime = datetime.strptime(closing_day, '%Y-%m-%d') - timedelta(days=1)
        yesterday_date: str = yesterday_datetime_obj.strftime('%Y-%m-%d')
        return yesterday_date
    



