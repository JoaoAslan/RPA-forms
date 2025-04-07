from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

from data import csv_writer as writer
from data import csv_reader as reader

import time

# Define some global variables
def init(main_config, headless) :
    global driver
    global config
    config = main_config
    driver = config.driver(headless)

def defineGUI() :
    gui = input("HIDE or SHOW WebDriver GUI? [H/S]: ")
    select = { "H" : True, "S" : False }
    try :
        return select[gui.upper()]
    except Exception :
        print(f"""
Selected input {gui} for GUI is not supported
Initiallizing with SHOW option""")
        return False

def defineTimes(sheet) :
    rows_count = reader.totalLines(sheet)
    times = int(input(f"How many lines do you want to run? (MAX: {rows_count}): "))
    if times > rows_count :
        times = 3
        print("""
It's impossible to run {times} times on length {rows_count}
Default value defined: 3 times""")
    return times

def errorOccured(count_errors, error, csv, line) :
    count_errors += 1
    printError(error)
    writer.writeAppend(csv, reader.readLine(line))
    return count_errors

def printInfo(index, line) :
    print(f"""
Index: {index}
Value: {line}""")

def printError(error) :
    print(f"""
An error occured!
Error message: {error}""")

def printTime(end, index, count) :
    print(f"""
Running {index} times in {end:.3f}s
Avarage time per line {end/(index+1):.3f}s
{count} errors occured!""")

# Login in
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

def checklist_info(line) :
    # Search place CONST
    findElement((By.XPATH, "/html/body/cl-root/cl-feature-shell/div[2]/div/div[2]/div/cl-categories/cl-main-content-card/div/cdk-virtual-scroll-viewport/div[1]/div[2]/cl-item/div/div[1]/cl-scale-selection/cl-multiselect/cl-multiselect-input/mat-form-field/div[1]/div[2]/div[1]/input")
                ).send_keys("FJC - P1-07")
    findElementByText("span", "FJC - P1-07  (MG)").click()
    
    # Search name or registration
    value_name = employeeRegistration(line[0], line[1])
    findElement((By.XPATH, "/html/body/cl-root/cl-feature-shell/div[2]/div/div[2]/div/cl-categories/cl-main-content-card/div/cdk-virtual-scroll-viewport/div[1]/div[3]/cl-item/div/div[1]/cl-scale-selection/cl-multiselect/cl-multiselect-input/mat-form-field/div[1]/div[2]/div[1]/input")
                ).send_keys(value_name)
    findElementByText("span", value_name).click()

    # Date
    input_date = (By.XPATH, "/html/body/cl-root/cl-feature-shell/div[2]/div/div[2]/div/cl-categories/cl-main-content-card/div/cdk-virtual-scroll-viewport/div[1]/div[5]/cl-item/div/div[1]/cl-scale-date/mat-form-field/div[1]/div[2]/div[1]/input")
    value_date = line[3]
    findElement(input_date).send_keys(value_date)
    findElementByText("span", "2 de 7").click() # random element click
    tryUntilFill(input_date, value_date)

    # Start time
    input_start = (By.XPATH, "/html/body/cl-root/cl-feature-shell/div[2]/div/div[2]/div/cl-categories/cl-main-content-card/div/cdk-virtual-scroll-viewport/div[1]/div[6]/cl-item/div/div[1]/cl-scale-hour/mat-form-field/div[1]/div[2]/div[1]/input")
    value_start = line[4]
    findElement(input_start).send_keys(value_start)
    findElementByText("span", "2 de 7").click() # random element click
    tryUntilFill(input_start, value_start)
    
    # Finish time
    input_finish = (By.XPATH, "/html/body/cl-root/cl-feature-shell/div[2]/div/div[2]/div/cl-categories/cl-main-content-card/div/cdk-virtual-scroll-viewport/div[1]/div[7]/cl-item/div/div[1]/cl-scale-hour/mat-form-field/div[1]/div[2]/div[1]/input")
    value_finish = line[5]
    findElement(input_finish).send_keys(value_finish)
    findElementByText("span", "2 de 7").click() # random element click
    tryUntilFill(input_finish, value_finish)

    savingData()
    findElementByText("span", "Próximo").click()
    
def checklist_items() :
    # Check all to Yes
    findElement((By.XPATH, "/html/body/cl-root/cl-feature-shell/div[2]/div/div[2]/div/cl-categories/cl-main-content-card/div/cdk-virtual-scroll-viewport/div[1]/div[1]/cl-category-header/div/button")
                ).click()                                                                                                             # ...
    findElementByText("span", "Aplicar resposta a todos ").click()                                                                    # apply to all
    findElement((By.XPATH, '//*[@id="mat-mdc-dialog-0"]/div/div/cl-item-answer-all-dialog/mat-dialog-content/cl-evaluative/div[3]')
                ).click()                                                                                                             # yes
    findElementByText("span", "Confirmar ").click()                                                                                   # confirm
    findElementByText("span", "Ok", 75).click()                                                                                       # ok
    
    # Check all breakdowns N/A
    findElement((By.XPATH, '/html/body/cl-root/cl-feature-shell/div[2]/div/div[2]/div/cl-categories/cl-main-content-card/div/cdk-virtual-scroll-viewport/div[1]/div[9]/cl-subcategory-header/div/button/span[3]')
                ).click()                                                                                                             # ...
    findElementByText("span", "Aplicar resposta a todos").click()                                                                     # apply to all
    findElement((By.XPATH, '//*[@id="mat-mdc-dialog-1"]/div/div/cl-item-answer-all-dialog/mat-dialog-content/cl-evaluative/div[1]')
                ).click()                                                                                                             # n/a
    findElementByText("span", "Confirmar ").click()                                                                                   # confirm
    findElementByText("span", "Ok").click()                                                                                           # ok
    
    # Finish the checklist
    for i in range(4):                                                                                                                # next (1 -> 4)
        time.sleep(0.3)
        findElementByText("span", "Próximo").click()
    findElementByText("span", " Concluir ").click()                                                                                   # finish (1/2)
    
    if (findElementByText("span", "Existem itens obrigatórios pendentes nesta aplicação (lista abaixo). Deseja revisar ou continuar depois?", 1) != None):
        raise Exception("Error to complete checklist...")
    else:
        findElementByText("span", "Concluir ").click()                                                                                # finish (2/2)
        findElementByText("span", " Ok ").click()                                                                                     # ok
    
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

# Wait save data
def savingData():
    while (findElementByText("mat-hint", " Salvando... ", 0.2) != None):
        time.sleep(0.35)

# Verify if elemets has a value (text)
def isBlank(element, text) :
    if (not text in element.get_attribute("value")) :
        return True
    return False

# Try to fill index with value (3 times)
def tryUntilFill(index, value) :
    i = 0
    element = findElement(index)
    while (isBlank(element, value)) :
        if (i == 2):
            raise TypeError(f"Cant fill with {value}")
        time.sleep(1)
        element.send_keys(value)
        findElementByText("span", "2 de 7").click() # random element click
        i = i+1

# Search element by element.text
def findElementByText(typeHTML, text, timeout=5) :
    try :
        element = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((By.XPATH, f"//{typeHTML}[text()='{text}']"))
        )
        return element
    except TimeoutException as e:
        return None

# Format name and registration
def employeeRegistration(name, reg) :
    return str(reg) + " - " + name