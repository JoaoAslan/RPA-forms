import web.form_controller as controller
import config.configuration as config

from data import csv_reader as reader
from data import csv_writer as writer

import time

# Reading informations
sheet = reader.readCSV(config.SHEET)
base = reader.readCSV(config.BASE)
temp = sheet[:] # copy of sheet

writer.createFiles(config.ERROR, ["NOME", "MATRICULA", "LOCOMOTIVA", "DATA", "HORA"])
writer.createFiles(config.DONE, ["NOME", "MATRICULA", "LOCOMOTIVA", "DATA", "HORA INICIAL", "HORA FINAL"])

gui = controller.defineGUI()
times = controller.defineTimes(sheet)
controller.init(config, gui)
controller.login()

count_errors = 0
start_time = time.time()
for index, line in enumerate(sheet) :
        try:
            if index == times:
                break
            controller.printInfo(index, line)
            start_time_line = time.time()
            temp.pop(0)
            validLine = reader.validate(base, line, index)
            controller.init_checklist(validLine)
            controller.checklist_info(validLine)
            controller.checklist_items()
        except Exception as e:
            count_errors = controller.errorOccured(count_errors, e, config.ERROR, line)
        else:
            writer.writeAppend(config.DONE, validLine)
        finally:
            writer.overWrite(config.SHEET, temp)
            end_time_line = time.time() - start_time_line
            print(f"Running for {end_time_line:.3f}s")
end_time = time.time() - start_time
controller.printTime(end_time, index, count_errors)