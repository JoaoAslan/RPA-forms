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
    validLine = datareader.validate(config, line, index)
    print(validLine)

loc = None
controller.init_checklist(config, loc) # locomotiva value here
controller.checklist_infopage()