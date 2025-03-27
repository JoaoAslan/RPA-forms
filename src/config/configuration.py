from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

import os
from dotenv import load_dotenv

# Load chrome driver for Selenium
def driver() :
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

# Enviroment Variables
load_dotenv()

LOGIN_URL=os.getenv("LOGIN_URL")
USER=os.getenv("USER")
PASSWORD=os.getenv("PASSWORD")
CHECKLIST_URL=os.getenv("CHECKLIST_URL")
CLEANING_URL=os.getenv("CLEANING_URL")
APPLYCHECKLIST_URL=os.getenv("APPLYCHECKLIST_URL")
INFOCHECKLIST_URL=os.getenv("INFOCHECKLIST_URL")
SHEET=os.getenv("SHEET")
BASE=os.getenv("BASE")
