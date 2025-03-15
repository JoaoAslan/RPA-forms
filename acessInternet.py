from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import configparser

import time

# Carregar as credenciais
config = configparser.ConfigParser()
config.read('config/config.ini')

driver = webdriver.Chrome()
driver.get(config['credenciais']['url'])

# Funçao que aguarda e retorna o elemento carregado
def elementFindByXpath(driver, xpath):
    return WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )

try :

    # Login da plataforma
    elementFindByXpath(driver,'//*[@id="mat-input-1"]'
                       ).send_keys(config['credenciais']['usuario'])

    elementFindByXpath(driver, '//*[@id="cl-root"]/cl-login-feature-shell/cl-user-identify-wrapper/div/section/main/cl-shell-component/div/div[2]/cl-login-feature-identifier/cl-username-input/form/cl-button-with-loading'
                       ).click()

    elementFindByXpath(driver, '//*[@id="mat-input-0"]'
                       ).send_keys(config['credenciais']['senha'])
    
    elementFindByXpath(driver, '//*[@id="cl-root"]/cl-login-feature-shell/cl-user-identify-wrapper/div/section/main/cl-shell-component/div/div[1]/cl-login-feature-authenticate/cl-password-input/form/cl-button-with-loading/button'
                       ).click()

    # Driver quit
    input("Pressione Enter para fechar o navegador...")
    driver.quit()

except Exception as e :
    print(f"Erro: {e}")
    driver.quit()
