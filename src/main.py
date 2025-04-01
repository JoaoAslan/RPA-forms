import web.form_controller as controller
import data.csv_reader as reader
import data.csv_writer as writer

import config.configuration as config
import time

# Verify if error.csv exists
if not writer.verifyFile(config.ERROR) :
    fieldnames = ["NOME", "MATRICULA", "LOCOMOTIVA", "DATA", "HORA"]
    writer.createCSV(config.ERROR, fieldnames)

if not writer.verifyFile(config.DONE) :
    fieldnames = ["NOME", "MATRICULA", "LOCOMOTIVA", "DATA", "HORA INICIAL", "HORA FINAL"]
    writer.createCSV(config.DONE, fieldnames)

controller.init(config)
controller.login()

# Reading informations
sheet = reader.readCSV(config.SHEET)
base = reader.readCSV(config.BASE)
temp = sheet[:]

start_time = time.time()
# All logic for running RPA
for index, line in enumerate(sheet) :
    try:
        if index == 20:
            break
        start_time_line = time.time()
        print(f"\n\nINDEX: {index}")
        print(f"Info: {line}")
        temp.pop(0)
        validLine = reader.validate(base, line, index)
        controller.init_checklist(validLine)
        controller.checklist_info(validLine)
        controller.checklist_items()
    except Exception as e:
        writer.writeAppend(config.ERROR, reader.readLine(line))
        print(f"Error: {e}")
    else:
        writer.writeAppend(config.DONE, validLine)
    finally:
        writer.overWrite(config.SHEET, temp)
        end_time = time.time() - start_time_line
        print(f"Running for {end_time:.3f}s")
end_time = time.time() - start_time
print(f"\nRunning {index} times in {end_time:.3f}s")
print(f"Avarage time per line {end_time/(index+1):.3f}s")