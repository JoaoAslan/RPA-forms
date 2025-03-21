from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

driver = None
def init(main_driver) :
    global driver
    driver = main_driver

def login(main_driver, main_config) :
    main_config.loadPage(main_driver, main_config.login)

    findElement((By.XPATH, '/html/body/cl-root/cl-login-feature-shell/cl-user-identify-wrapper/div/section/main/cl-shell-component/div/div[2]/cl-login-feature-identifier/cl-username-input/form/mat-form-field/div[1]/div[2]/div/input')
                ).send_keys(main_config.usuario)
    
    findElement((By.XPATH, '//*[@id="cl-root"]/cl-login-feature-shell/cl-user-identify-wrapper/div/section/main/cl-shell-component/div/div[2]/cl-login-feature-identifier/cl-username-input/form/cl-button-with-loading/button')
                ).click()
    
    findElement((By.XPATH, '/html/body/cl-root/cl-login-feature-shell/cl-user-identify-wrapper/div/section/main/cl-shell-component/div/div[1]/cl-login-feature-authenticate/cl-password-input/form/div[2]/mat-form-field/div[1]/div[2]/div[1]/input')
                ).send_keys(main_config.senha)
    
    findElement((By.XPATH, '/html/body/cl-root/cl-login-feature-shell/cl-user-identify-wrapper/div/section/main/cl-shell-component/div/div[1]/cl-login-feature-authenticate/cl-password-input/form/cl-button-with-loading/button')
                ).click()

# Go to checklist page
def init_checklist(main_config, loc) :
    if (pageIsLoaded((By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[1]/div/a/img'))):
        driver.get(main_config.checklist_1)

    elements = (By.CLASS_NAME, 'pre-apply-option__text')
    search = (By.XPATH, '/html/body/cl-root/cl-hall/div/div/div/cl-pre-apply-shell/cl-main-content/div[2]/div/div/cl-step-unit/div/div[1]/cl-unit-filters/div/div/mat-form-field/div[1]/div/div[3]/input')
    notFound = findElement((By.XPATH, '/html/body/cl-root/cl-hall/div/div/div/cl-pre-apply-shell/cl-main-content/div[2]/div/div/cl-step-unit/div/div[2]/cl-empty-states/cl-empty-state/div/div[2]/span[1]'), 0.5)
    
    elementsList = searchElements(search, loc, elements, notFound)
    searchElement(elementsList, loc).click()

    if (pageIsLoaded((By.XPATH, '/html/body/cl-root/cl-hall/div/div/div/cl-pre-apply-shell/cl-main-content/div[2]/div/div/cl-step-checklist/div/div[1]/cl-step-identification[1]/div'))):
        driver.get(main_config.checklist_2)

def checklist_infopage() :
    return True

def findElement(seletor, tempo_limite=10):
    try:
        element = WebDriverWait(driver, tempo_limite).until(
            EC.presence_of_element_located(seletor)
        )
        return element
    except TimeoutException:
        return None

def findElementsList(seletor):
    if (findElement(seletor) != None):
        by, path = seletor
        return driver.find_elements(by, path)
    return None

def pageIsLoaded(seletor) :
    try:
        if findElement(seletor) != None:
            return True
        raise InvalidSelectorException("Impossível localizar o elemento: "+ seletor[1])
    except InvalidSelectorException as e:
        print(f"Erro: {e}")

# Seach input in search bar and give list of all elements found
def searchElements(search, input, elements, notFound) :
    findElement(search).send_keys(input)
    if (notFound != None) :
        return None
    return findElementsList(elements)

# Search element by element.text
def searchElement(listElements, foundText) :
    try :
        for element in listElements:
            if element.text == foundText :
                return element
    except TypeError as e:
        print("Não foi possivel localizar nenhum elemento com o input: "+ foundText)