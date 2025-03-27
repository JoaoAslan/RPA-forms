import web.form_controller as controller
import data.csv_reader as reader
import data.csv_writer as writer

import config.configuration as config

# Verify if error.csv exists
if not writer.verifyFile(config.ERROR) :
    fieldnames = ["NOME", "MATRICULA", "LOCOMOTIVA", "DATA", "HORA"]
    writer.createCSV(config.ERROR, fieldnames)

controller.init(config)
controller.login()

# Reading informations
csv = reader.readCSV(config.SHEET)
temp = csv[:]

for index, line in enumerate(csv) :
    try:
        if index == 3:
            break
        temp.pop(0)
        validLine = reader.validate(config.BASE, line, index)
        controller.init_checklist(validLine)
        controller.checklist_infopage(validLine)
        controller.checklistItems()
    except Exception as e:
        print(line)
        writer.errorCSV(config.ERROR, line)
        print(f"Error on index: {index}\nError: {e}")
writer.overWrite(config.SHEET, temp)