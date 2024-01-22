import os
import sys
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from datetime import datetime
from random import randint


try:
    options = webdriver.FirefoxOptions()
    options.add_argument('-headless')
    driver = webdriver.Firefox(options=options)

    # Textual month, day and year
    today_date = datetime.now().strftime('%d %B %Y')
    today_day = datetime.now().strftime('%A')

    with open('data/Holiday_List.csv', 'r') as holiday_list:
        holiday_list = holiday_list.read()

    if today_date not in holiday_list or today_day != 'Sunday' or today_day != 'Saturday':

        # Retrieve contents from .env file
        load_dotenv('/app/data/.env')
        URL = os.getenv('URL')
        LOGIN = os.getenv('LOGIN')
        PASSWORD = os.getenv('PASSWORD')

        # Pick a random number between 1 and 1800/3600 seconds (within 30 minutes or an hour)
        random = randint(1, 1800)

        # Sleep for the random number before logging into HRMS
        time.sleep(random)

        # Open HRMS Page
        driver.get(URL)

        # Wait
        driver.implicitly_wait(15)

        # Enter Username
        driver.find_element(By.ID, 'txtUserName').send_keys(LOGIN)

        # Enter password
        driver.find_element(By.ID, 'txtPassword').send_keys(PASSWORD)

        time.sleep(15)

        # Click on the Login Button
        driver.find_element(By.ID, 'btnLogin').click()

        driver.implicitly_wait(15)

        # # Click on the Check-in/Check-out button
        driver.find_element(By.ID, 'btnCheckin').click()

        time.sleep(15)

except Exception as e:
    with open('data/Error.txt', 'w') as f:
        print(e, file=f)

finally:
    driver.quit()
    sys.exit()
