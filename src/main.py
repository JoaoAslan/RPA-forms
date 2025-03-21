import web.form_controller as controller
import data.csv_reader as datareader
import web.config.sel_config as config

#driver = config.driver()

csv = datareader.readLine(config)
for index, line in csv.iterrows():
    validateLine = datareader.validate(line)
    
#controller.init(driver)
#controller.login(driver, config)
# Looping for each line in CSV
#controller.init_checklist(config, "00751") # locomotiva value here
#controller.checklist_infopage("teste")