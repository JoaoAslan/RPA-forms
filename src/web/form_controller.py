from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

from time import sleep

# Define Driver and Config global
def init(main_config) :
    global driver
    global config
    config = main_config
    driver = config.driver()

def login() :
    loadPage(config.LOGIN_URL)
    findElement((By.NAME, "user-name")).send_keys(config.USER)
    findElement((By.XPATH, "//span[text()=' Continuar ']")).click()
    findElement((By.NAME, "user-password")).send_keys(config.PASSWORD)
    findElement((By.XPATH, "//span[text()=' Entrar ']")).click()
    
    if (pageIsLoaded(config.CHECKLIST_URL)) :
        loadPage(config.APPLYCHECKLIST_URL)

# Go to checklist page
def init_checklist(line) :
    loadPage(config.APPLYCHECKLIST_URL)
    findElement((By.ID, "field-search-1")).send_keys(line[2])
    findElementByText("div", line[2], 3).click()
    findElementByText("div", "Limpeza de Cabine de Locomotivas", 5).click()
    
def checklist_infopage(line) :
    
    # Search place
    findElement((By.XPATH, "/html/body/cl-root/cl-feature-shell/div[2]/div/div[2]/div/cl-categories/cl-main-content-card/div/cdk-virtual-scroll-viewport/div[1]/div[2]/cl-item/div/div[1]/cl-scale-selection/cl-multiselect/cl-multiselect-input/mat-form-field/div[1]/div[2]/div[1]/input")
                ).send_keys("FJC - P1-07")
    findElementByText("span", "FJC - P1-07  (MG)").click()

    # Search name or registration
    input = employeeRegistration(line[0], line[1])
    findElement((By.XPATH, "/html/body/cl-root/cl-feature-shell/div[2]/div/div[2]/div/cl-categories/cl-main-content-card/div/cdk-virtual-scroll-viewport/div[1]/div[3]/cl-item/div/div[1]/cl-scale-selection/cl-multiselect/cl-multiselect-input/mat-form-field/div[1]/div[2]/div[1]/input")
                ).send_keys(input)
    findElementByText("span", input).click()

    # Date
    findElement((By.XPATH, "/html/body/cl-root/cl-feature-shell/div[2]/div/div[2]/div/cl-categories/cl-main-content-card/div/cdk-virtual-scroll-viewport/div[1]/div[5]/cl-item/div/div[1]/cl-scale-date/mat-form-field/div[1]/div[2]/div[1]/input")
                ).send_keys(line[3])
    
    # Start time
    findElement((By.XPATH, "/html/body/cl-root/cl-feature-shell/div[2]/div/div[2]/div/cl-categories/cl-main-content-card/div/cdk-virtual-scroll-viewport/div[1]/div[6]/cl-item/div/div[1]/cl-scale-hour/mat-form-field/div[1]/div[2]/div[1]/input")
                ).send_keys(line[4])
    
    # Finish time ERROR BY TIME
    findElement((By.XPATH, "/html/body/cl-root/cl-feature-shell/div[2]/div/div[2]/div/cl-categories/cl-main-content-card/div/cdk-virtual-scroll-viewport/div[1]/div[7]/cl-item/div/div[1]/cl-scale-hour/mat-form-field/div[1]/div[2]/div[1]/input")
                ).send_keys(line[5])

    sleep(1)
    findElementByText("span", "Próximo").click()
    
def checklistItems() :
    # Check all to Yes
    findElement((By.XPATH, "/html/body/cl-root/cl-feature-shell/div[2]/div/div[2]/div/cl-categories/cl-main-content-card/div/cdk-virtual-scroll-viewport/div[1]/div[1]/cl-category-header/div/button")
                ).click()                                                                                                             # ...
    findElementByText("span", "Aplicar resposta a todos ").click()                                                                    # apply to all
    findElement((By.XPATH, '//*[@id="mat-mdc-dialog-0"]/div/div/cl-item-answer-all-dialog/mat-dialog-content/cl-evaluative/div[3]')
                ).click()                                                                                                             # yes
    findElementByText("span", "Confirmar ").click()                                                                                   # confirm
    findElementByText("span", "Ok", 60).click()                                                                                       # ok
    
    # Check all breakdowns N/A
    findElement((By.XPATH, '/html/body/cl-root/cl-feature-shell/div[2]/div/div[2]/div/cl-categories/cl-main-content-card/div/cdk-virtual-scroll-viewport/div[1]/div[9]/cl-subcategory-header/div/button/span[3]')
                ).click()                                                                                                             # ...
    findElementByText("span", "Aplicar resposta a todos").click()                                                                     # apply to all
    findElement((By.XPATH, '//*[@id="mat-mdc-dialog-1"]/div/div/cl-item-answer-all-dialog/mat-dialog-content/cl-evaluative/div[1]')
                ).click()                                                                                                             # n/a
    findElementByText("span", "Confirmar ").click()                                                                                   # confirm
    findElementByText("span", "Ok", 7).click()                                                                                        # ok
    
    # Finish the checklist
    for i in range(4):                                                                                                                # next (1 -> 4)
        sleep(0.5)
        findElementByText("span", "Próximo").click()
    findElementByText("span", " Concluir ").click()                                                                                   # finish (1/2)
    findElementByText("span", "Concluir ").click()                                                                                    # finish (2/2)
    findElementByText("span", " Ok ").click()                                                                                         # ok
    
# Find a element by seletor
def findElement(seletor, timeout=10):
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(seletor)
        )
        return element
    except TimeoutException:
        return None

# Find all elements by seletor and return a list
def findElementsList(seletor, timeout=10):
    try:
        elements = WebDriverWait(driver, timeout).until(
            EC.visibility_of_all_elements_located(seletor)
        )
        return elements
    except TimeoutException:
        return None

# Wait DOM load and return a bool
def pageIsLoaded(url_loaded, timeout=10) :
    try:
        page = WebDriverWait(driver, timeout).until(
            EC.url_contains(url_loaded)
        )
        return page
    except InvalidSelectorException as e:
        print(f"Error: {e}")

def loadPage(url_to_be_loaded):
    driver.get(url_to_be_loaded)

# Search element by element.text
def findElementByText(typeHTML, text, timeout=5) :
    try :
        element = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, f"//{typeHTML}[text()='{text}']"))
        )
        return element
    except Exception as e:
        print(f"Could not find any element {typeHTML} with text()='{text}'")

# Format name and registration
def employeeRegistration(name, reg) :
    return str(reg) + " - " + name