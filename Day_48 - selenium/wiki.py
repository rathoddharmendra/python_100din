from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = 'https://en.wikipedia.org/wiki/Main_Page'
# Set Chrome options to open a new Chrome browser in a detached window
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

# Open a new Chrome browser in a detached window
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)
# article_count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/ul/li[2]/a[1]' )
# print('Total articles:', article_count.text)

# Wikivoyage = driver.find_element(By.LINK_TEXT, 'Wikivoyage')

# Wikivoyage.click()

click_input = driver.find_element(By.XPATH, "//div[@id='p-search']/a[@class='search-toggle']")
click_input.click()


search_input = driver.find_element(By.NAME, 'search')
search_input.send_keys('Python', Keys.ENTER)



# Wait for the search results to load
driver.implicitly_wait(5)

# search_results = driver.find_elements(By.CSS_SELECTOR, '.mw-search-result-heading a')

# for result in search_results:
    # print(result.text)
driver.quit()


