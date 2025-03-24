import web.form_controller as controller
import data.csv_reader as datareader
import web.config.sel_config as config

# Initialization and login
driver = config.driver()
controller.init(driver)
controller.login(driver, config)

# Reading informations
csv = datareader.readCSV(config.sheet)
for index, line in enumerate(csv) :
    if index > 0:
        break
    validLine = datareader.validate(config, line, index)
    print(validLine)
    controller.init_checklist(config, validLine[2]) # locomotive value here
    controller.checklist_infopage(validLine)
    controller.checklistItems()