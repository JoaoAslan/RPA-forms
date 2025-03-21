from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

import configparser

# Carregar as credenciais para acesso da plataforma
configp = configparser.ConfigParser()
configp.read("C:\codes\RPA-Forms\src\web\config\config.ini")

login = configp.get('credenciais', 'login')
usuario = configp.get('credenciais', 'usuario')
senha = configp.get('credenciais', 'senha')
checklist_1 = configp.get('credenciais', 'checklist_1')
checklist_2 = configp.get('credenciais', 'checklist_2')
sheet = configp.get('credenciais', 'sheet')
base = configp.get('credenciais', 'base')


# Carregar o driver do navegador para o Selenium
def driver() :
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def loadPage(driver, url) :
    return driver.get(url)

