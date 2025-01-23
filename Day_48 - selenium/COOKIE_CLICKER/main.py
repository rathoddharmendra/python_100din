from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By

URL = 'https://orteil.dashnet.org/experiments/cookie/'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(URL)

cookie = driver.find_element(By.ID, 'cookie')

def buy_helpers(id: str):
    try:
        driver.find_element(By.ID, id).click()
    except WebDriverException:
        print(f'Unable to find button with ID: {id}')

buy_triggers = {
    20: 'buyCursor', 
    120: 'buyGrandma', 
    590: 'buyFactory', 
    2700: 'buyMine',
    7500: 'buyShipment',
    50000: 'buyAlchemy lab',
    1000000: 'buyPortal',
    123456789: 'buyTime machine',
    1234567890: 'buyElder Pledge'}

for trigger, id in buy_triggers.items():
    for i in range(trigger):
        cookie.click()
    buy_helpers(id)


