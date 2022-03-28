import os, time, datetime

# Set current directory
#os.chdir(os.path.dirname(sys.argv[0]))
os.chdir(os.getcwd())

from dotenv import load_dotenv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from random import *
from datetime import datetime

load_dotenv()

# Textual month, day and year
todays_date = datetime.now().strftime("%d %B %Y")
todays_day = datetime.now().strftime("%A")
              
with open('Holiday_List.csv', 'r') as holiday_list:
    if todays_date in holiday_list.read() or todays_day == "Sunday" or todays_day == "Saturday":
        print ("It's a holiday today")
    else:
        # Pick a random number between 1 to 3600 seconds (within an hour)
        random = randint(1, 3600)

        # Sleep for the random number before logging into HRMS
        time.sleep(random)

        # Retrieve contents from .env file
        URL = os.getenv("URL")
        LOGIN = os.getenv("LOGIN")
        PASSWORD = os.getenv("PASSWORD")

        driver = webdriver.Chrome(ChromeDriverManager().install())

        # Open HRMS Page
        driver.get(URL)

        # Wait
        driver.implicitly_wait(15)

        # Enter Username
        driver.find_element_by_id("txtUserName").send_keys(LOGIN)

        # Enter password
        driver.find_element_by_id ("txtPassword").send_keys(PASSWORD)

        # Click on the Login Button
        driver.find_element_by_id("btnLogin").click()
        
        time.sleep(15)

        # # Click on the Check-in/Check-out button
        driver.find_element_by_id("btnCheckin").click()
        
        time.sleep(15)

        driver.quit()