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
def init_checklist(main_config, text) :
    if (pageIsLoaded((By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[1]/div/a/img'))):
        driver.get(main_config.checklist_1)
    findElementOnSearch(text).click()
    if (pageIsLoaded((By.XPATH, '/html/body/cl-root/cl-hall/div/div/div/cl-pre-apply-shell/cl-main-content/div[2]/div/div/cl-step-checklist/div/div[1]/cl-step-identification[1]/div'))):
        driver.get(main_config.checklist_2)

def checklist_infopage(csv_line) :
    findElement((By.XPATH, '/html/body/cl-root/cl-feature-shell/div[2]/div/div[2]/div/cl-categories/cl-main-content-card/div/cdk-virtual-scroll-viewport/div[1]/div[2]/cl-item/div/div[1]/cl-scale-selection/cl-multiselect/cl-multiselect-input/mat-form-field/div[1]/div[2]/div[1]/input')
                ).click()
    findElement((By.XPATH, '/html/body/div[5]/div[3]/div/cl-multiselect-options/div/div/cdk-virtual-scroll-viewport/div[1]/cl-multiselect-option[5]/div/cl-multiselect-option-value')
                ).click()
    return True

def findElement(seletor, tempo_limite=10):
    try:
        element = WebDriverWait(driver, tempo_limite).until(
            EC.presence_of_element_located(seletor)
        )
        return element
    except TimeoutException:
        return None

def findElementsList(by, path):
    if (findElement((by, path)) != None):
        return driver.find_elements(by, path)
    return None

def pageIsLoaded(seletor) :
    try:
        if findElement(seletor) != None:
            return True
        raise InvalidSelectorException("Impossível localizar o elemento: "+ seletor[1])
    except InvalidSelectorException as e:
        print(f"Erro: {e}")

def search(input, notFoundElement, text) :
    # Search bar input
    findElement(input).send_keys(text)
    if (notFoundElement != None) :
        return None
    else:
        return findElementsList(By.CLASS_NAME, 'pre-apply-option__text')
    
def findElementOnSearch(text) :
    input = (By.XPATH, '/html/body/cl-root/cl-hall/div/div/div/cl-pre-apply-shell/cl-main-content/div[2]/div/div/cl-step-unit/div/div[1]/cl-unit-filters/div/div/mat-form-field/div[1]/div/div[3]/input')
    notFoundElement = findElement((By.XPATH, '/html/body/cl-root/cl-hall/div/div/div/cl-pre-apply-shell/cl-main-content/div[2]/div/div/cl-step-unit/div/div[2]/cl-empty-states/cl-empty-state/div/div[2]/span[1]'), 0.5)
    listElements = search(input, notFoundElement, text)
    try :
        for element in listElements:
            if element.text == text :
                return element
    except TypeError as e:
        print("Não foi possivel localizar nenhum elemento com o input: "+ text)