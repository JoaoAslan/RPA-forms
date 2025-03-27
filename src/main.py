import web.form_controller as controller
import data.csv_reader as datareader
import config.configuration as config

controller.init(config)
controller.login()

# Reading informations
csv = datareader.readCSV(config.SHEET)
temp = csv[:]
for index, line in enumerate(csv) :
    try:
        if index > 0:
            break
        validLine = datareader.validate(config.BASE, line, index)
        controller.init_checklist(validLine)
        controller.checklist_infopage(validLine)
        controller.checklistItems()
    except Exception as e:
        # csvError()
        print(f"Error on index: {index}\n",
              f"Error: {e}")
