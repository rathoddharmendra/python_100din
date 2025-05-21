# type: ignore
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
import os, time, csv

BASE_URL = 'https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors/page/'
FILENAME = os.path.join(os.path.dirname(__file__), 'final-post-college-salaries.csv')

# global variable
page_number = 9

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# TODO 1: first get the header
def update_header(elem):
    # calculate data
    head = [tag.text for tag in elem]
    with open(FILENAME, 'a') as file:
        writer = csv.writer(file)
        writer.writerow(head)

# TODO 2: then, run loop to get all elements
# TODO 3: then update csv row
def update_rows(elem):
    with open(FILENAME, 'a') as file:
        writer = csv.writer(file)
        for table_row in elem:
            cells = table_row.find_elements(By.TAG_NAME, 'td')
            row = [cell.text for cell in cells]
            writer.writerow(row)
    # reads a row
    # opens csv, and adds a row

def check_data(elem) -> bool:
    return len(elem) != 0

# Main Program

is_data = True
while is_data:
    driver.get(BASE_URL + str(page_number))

    try:
        table = driver.find_element(By.CLASS_NAME, 'data-table')
        body = table.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
    except Exception as e:
        print(f'Exception Occured with error {e}')
        break

    is_data = check_data(body)
    if is_data:
        if page_number == 1:
            # better to see if file exists
            table_head = table.find_element(By.TAG_NAME, 'thead').find_elements(By.TAG_NAME, 'th')
            update_header(table_head)
        # Update rows in a CSV file
        update_rows(body)

    # slow down execution
    page_number += 1
    time.sleep(5)
    
