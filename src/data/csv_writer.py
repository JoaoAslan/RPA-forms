import csv

def createCSV(name, fieldnames) :
    with open (name, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        return writer

def writeLine(file, lines) :
    with open(file, 'w', newline='', encoding='UTF-8') as csv_file :
        writer = csv.writer(csv_file)
        writer.writerows(lines)
        
fieldnames = ["NOME", "MATRICULA", "LOCOMOTIVA", "DATA", "HORA INICIAL", "HORA FINAL"]
createCSV("erros.csv", fieldnames)