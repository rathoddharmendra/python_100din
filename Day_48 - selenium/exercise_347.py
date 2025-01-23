from selenium import webdriver
from selenium.webdriver.common.by import By

URL = 'https://www.python.org/'

# Set Chrome options to open a new Chrome browser in a detached window
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

# Open a new Chrome browser in a detached window
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

events_date = driver.find_elements(By.CSS_SELECTOR, 'div.medium-widget.event-widget.last time')
events_name = driver.find_elements(By.CSS_SELECTOR, 'div.medium-widget.event-widget.last li a')

events = {}
for idx, event in enumerate(zip(events_date, events_name)):
    events[idx] = {'time': event[0].text, 'name': event[1].text}

print(events)

driver.quit()