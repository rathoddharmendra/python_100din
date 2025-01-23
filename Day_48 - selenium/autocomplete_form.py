from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By

URL = 'https://secure-retreat-92358.herokuapp.com/'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(URL)

first_name = driver.find_element(By.NAME, 'fName')
last_name = driver.find_element(By.NAME, 'lName')
email = driver.find_element(By.NAME, 'email')
button = driver.find_element(By.CSS_SELECTOR, 'button[type=submit]')

first_name.send_keys('Hello Angela')
last_name.send_keys('From deepest part of me ')
email.send_keys('iWantToSay@ThankYou.ToYou')
button.click()