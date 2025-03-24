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
    notFound = (By.XPATH, '/html/body/cl-root/cl-hall/div/div/div/cl-pre-apply-shell/cl-main-content/div[2]/div/div/cl-step-unit/div/div[2]/cl-empty-states/cl-empty-state/div/div[2]/span[1]')
    searchElement(searchElements(search, elements, notFound, loc), loc).click()

    findElement((By.XPATH, '/html/body/cl-root/cl-hall/div/div/div/cl-pre-apply-shell/cl-main-content/div[2]/div/div/cl-step-checklist/div/div[2]/div/cdk-virtual-scroll-viewport/div[1]/cl-pre-apply-option/div')
                ).click()

def checklist_infopage(line) :
    # Search place
    search = (By.XPATH, '/html/body/cl-root/cl-feature-shell/div[2]/div/div[2]/div/cl-categories/cl-main-content-card/div/cdk-virtual-scroll-viewport/div[1]/div[2]/cl-item/div/div[1]/cl-scale-selection/cl-multiselect/cl-multiselect-input/mat-form-field/div[1]/div[2]/div[1]/input')
    elements = (By.CSS_SELECTOR , '.multiselect-option[_ngcontent-ng-c1069702620]')
    notFound = (By.XPATH, '/html/body/div[5]/div[3]/div/cl-multiselect-options/div/div[1]/span')
    searchElement(searchElements(search, elements, notFound, "FJC - P1-07"), "FJC - P1-07 (MG)").click()

    # Search name or registration
    search = (By.XPATH, '/html/body/cl-root/cl-feature-shell/div[2]/div/div[2]/div/cl-categories/cl-main-content-card/div/cdk-virtual-scroll-viewport/div[1]/div[3]/cl-item/div/div[1]/cl-scale-selection/cl-multiselect/cl-multiselect-input/mat-form-field/div[1]/div[2]/div[1]/input')
    elements = (By.CSS_SELECTOR, '.multiselect-option-text[_ngcontent-ng-c1069702620]')
    input = employeeRegistration(line[0], line[1])
    notFound = (By.XPATH, '/html/body/div[5]/div[2]/div/cl-multiselect-options/div/div[1]/span')
    searchElement(searchElements(search, elements, notFound, input), input).click()

    findElement((By.XPATH, '/html/body/cl-root/cl-feature-shell/div[2]/div/div[2]/div/cl-categories/cl-main-content-card/div/cdk-virtual-scroll-viewport/div[1]/div[5]/cl-item/div/div[1]/cl-scale-date/mat-form-field/div[1]/div[2]/div[1]/input')
                ).send_keys(line[5])
    
    findElement((By.XPATH, '/html/body/cl-root/cl-feature-shell/div[2]/div/div[2]/div/cl-categories/cl-main-content-card/div/cdk-virtual-scroll-viewport/div[1]/div[6]/cl-item/div/div[1]/cl-scale-hour/mat-form-field/div[1]/div[2]/div[1]/input')
                ).send_keys(line[3])
    
    findElement((By.XPATH, '/html/body/cl-root/cl-feature-shell/div[2]/div/div[2]/div/cl-categories/cl-main-content-card/div/cdk-virtual-scroll-viewport/div[1]/div[7]/cl-item/div/div[1]/cl-scale-hour/mat-form-field/div[1]/div[2]/div[1]/input')
                ).send_keys(line[4])

    findElement((By.XPATH, '/html/body/cl-root/cl-feature-shell/div[2]/div/div[2]/div/cl-categories/cl-apply-navigation/div/a[2]')
                ).click()
    
def checklistItems() :
    # Check all to Yes
    findElement((By.XPATH, '/html/body/cl-root/cl-feature-shell/div[2]/div/div[2]/div/cl-categories/cl-main-content-card/div/cdk-virtual-scroll-viewport/div[1]/div[1]/cl-category-header/div/button/span[3]')
                ).click()
    findElement((By.CSS_SELECTOR, '.mat-mdc-menu-panel .mat-mdc-menu-item')
                ).click() # apply to all items
    findElement((By.XPATH, '//*[@id="mat-mdc-dialog-0"]/div/div/cl-item-answer-all-dialog/mat-dialog-content/cl-evaluative/div[3]')
                ).click() # yes
    findElement((By.XPATH, '//*[@id="mat-mdc-dialog-0"]/div/div/cl-item-answer-all-dialog/mat-dialog-actions/cl-button-with-loading/button')
                ).click() # confirm
    findElement((By.CSS_SELECTOR, '.completed-actions[_ngcontent-ng-c3959942450] button[_ngcontent-ng-c3959942450]'), 60
                ).click() # ok
    
    # Check all breakdowns N/A
    findElement((By.XPATH, '/html/body/cl-root/cl-feature-shell/div[2]/div/div[2]/div/cl-categories/cl-main-content-card/div/cdk-virtual-scroll-viewport/div[1]/div[9]/cl-subcategory-header/div/button/span[3]')
                ).click()
    findElement((By.CSS_SELECTOR, '.mat-mdc-menu-panel .mat-mdc-menu-item')
                ).click() # apply to all items in breakdowms
    findElement((By.XPATH, '//*[@id="mat-mdc-dialog-1"]/div/div/cl-item-answer-all-dialog/mat-dialog-content/cl-evaluative/div[1]')
                ).click() # n/a
    findElement((By.XPATH, '//*[@id="mat-mdc-dialog-1"]/div/div/cl-item-answer-all-dialog/mat-dialog-actions/cl-button-with-loading/button')
                ).click() # confirm
    findElement((By.CSS_SELECTOR, '.completed-actions[_ngcontent-ng-c3959942450] button[_ngcontent-ng-c3959942450]')
                ).click() # ok
    
    # Finish the checklist
    findElement((By.XPATH, '//*[@id="cl-root"]/cl-feature-shell/div[2]/div/div[2]/div/cl-categories/cl-apply-navigation/div/a[2]')
                ).click() # next (1/4)
    findElement((By.XPATH, '//*[@id="cl-root"]/cl-feature-shell/div[2]/div/div[2]/div/cl-categories/cl-apply-navigation/div/a[2]')
                ).click() # next (2/4)
    findElement((By.XPATH, '//*[@id="cl-root"]/cl-feature-shell/div[2]/div/div[2]/div/cl-general-sharing/cl-apply-navigation/div/a[2]')
                ).click() # next (3/4)
    findElement((By.XPATH, '//*[@id="cl-root"]/cl-feature-shell/div[2]/div/div[2]/div/cl-general-comment/cl-apply-navigation/div/a[2]')
                ).click() # next (4/4)
    findElement((By.XPATH, '//*[@id="cl-root"]/cl-feature-shell/div[2]/div/div[2]/div/cl-checklist-signatures/cl-apply-navigation/div/button')
                ).click() # finish (1/2)
    #findElement((By.XPATH, '//*[@id="mat-mdc-dialog-2"]/div/div/cl-conclusion-dialog/cl-dialog-confirm-conclusion/mat-dialog-actions/cl-button-with-loading/button')
    #            ).click() # finish (2/2)
    #findElement((By.XPATH, '//*[@id="mat-mdc-dialog-3"]/div/div/cl-dialog-conclusion-success/div/button')
    #            ).click() # ok

def findElement(seletor, tempo_limite=10):
    try:
        element = WebDriverWait(driver, tempo_limite).until(
            EC.presence_of_element_located(seletor)
        )
        return element
    except TimeoutException:
        return None

def findElementsList(seletor, tempo_limite=10):
    try:
        elements = WebDriverWait(driver, tempo_limite).until(
            EC.presence_of_all_elements_located(seletor)
        )
        return elements
    except TimeoutException:
        return None

def pageIsLoaded(seletor) :
    try:
        if findElement(seletor) != None:
            return True
        raise InvalidSelectorException("Unable to locate element: "+ seletor[1])
    except InvalidSelectorException as e:
        print(f"Erro: {e}")

# Use search bar to give a list of all elements found
def searchElements(search, elements, notFoundpath, input=None) :
    if (input != None) :
        findElement(search).send_keys(input)
    else:
        findElement(search).click()
    notFound = findElement(notFoundpath, 1)
    if (notFound != None) :
        return None
    return findElementsList(elements)

# Search element by element.text
def searchElement(listElements, foundText) :
    try :
        for element in listElements:
            if foundText in element.text :
                return element
    except TypeError as e:
        print("Could not find any element with input: "+ foundText)

def employeeRegistration(name, reg) :
    return str(reg) + " - " + name