from stock_analyst import StockAnalyzer
from news import NewsAPI
from sms import SmsClient
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

stock_analyzer = StockAnalyzer(stock_symbol=STOCK)
direction, stock_variation_data = stock_analyzer.check_stock_variation()
movement_symbol = '🔺' if direction == 0 else '🔻'
# if more than 5% fluctuation, check news
if stock_variation_data > 1:
    # fetch new stock
    news = NewsAPI(stock_name=COMPANY_NAME)
    news_data = news.get_news()

    message = f'''
    \n
    {STOCK}: {movement_symbol}{stock_variation_data}%
    Headline: {news_data[0]}
    Brief: {news_data[1]}
    '''
    # send news via sms
    SmsClient().send_sms(msg=message)