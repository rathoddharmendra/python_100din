from stock_analyst import StockAnalyzer
from news import NewsAPI
from sms import SmsClient
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


# The program runs at 6 AM EST before market opens at 09:30 FileExistsError
# Checks to see if there is more than 5% fluctuations in the portfolio of tesla


# if yes, it checks any relevant news to back the movements

# And, sends the message via sms


# check to see if the last 2 days delta is more than 5 %
    # read data from api
    # evaluate last 2 days delta

stock_analyzer = StockAnalyzer(stock_symbol=STOCK)
direction, stock_variation_data = stock_analyzer.check_stock_variation()
# if more than 5% fluctuation, check news
if stock_variation_data > 1:
    movement_symbol = '🔺' if direction == 0 else '🔻'
    news = NewsAPI(stock_name=COMPANY_NAME)
    news_data = news.get_news()
    # send news via sms
    message = f'''
    \n
    {STOCK}: {movement_symbol}{stock_variation_data}%
    Headline: {news_data[0]}
    Brief: {news_data[1]}
    '''
    SmsClient().send_sms(msg=message)