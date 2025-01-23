from selenium import webdriver
from selenium.webdriver.common.by import By

# Set Chrome options to open a new Chrome browser in a detached window
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

# Open a new Chrome browser in a detached window and navigate to Amazon.com
driver = webdriver.Chrome(options=chrome_options)
# driver.get('https://www.amazon.de/-/en/Indian-Idli-Rice-Cake-Steamer/dp/B0020IT00Q/ref=pd_ci_mcx_mh_mcx_views_0_title?pd_rd_w=Bc7M7&content-id=amzn1.sym.7f9b9996-bc03-4d04-b9b7-40b61293137b%3Aamzn1.symc.ca948091-a64d-450e-86d7-c161ca33337b&pf_rd_p=7f9b9996-bc03-4d04-b9b7-40b61293137b&pf_rd_r=NFTEJRZZR61XNDY6DBXQ&pd_rd_wg=PTOkU&pd_rd_r=42903c9f-32b5-4528-aa21-6ea3d371934f&pd_rd_i=B0020IT00Q#customerReviews')

# price_euro = driver.find_element(by=By.CLASS_NAME, value='a-price-whole')
# price_cent = driver.find_element(by=By.CLASS_NAME, value='a-price-fraction')

# print(f'The price of the idli rice cake is {price_euro.text}.{price_cent.text} EUR.')

driver.get('https://sheralkaren.github.io/git-pages/public/BBG/')

# email_subscription = driver.find_element(By.ID, 'email-input')
# email_subscription = driver.find_element(By.NAME, 'email-input')
# print(f"{email_subscription.get_attribute('placeholder')}")
# print(f"{email_subscription.tag_name}")
# print(f"{email_subscription.text}")

# using css selector

# using xpath div>p>a
random_text = driver.find_element(By.XPATH, '/html/body/footer/p')
print(random_text.text)
driver.quit()
# driver.close()