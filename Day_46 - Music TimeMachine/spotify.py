import requests
from datetime import datetime as dt


# Get current date and time
current_time = dt.datetime.now()
today = f'{current_time.strftime("%Y-%m-%d")}'