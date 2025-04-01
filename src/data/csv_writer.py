import csv
import os.path as os
import data.csv_reader as reader

def createCSV(name, fieldnames) :
    with open (name, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        return writer

def writeLine(file, lines) :
    with open(file, 'w', newline='', encoding='UTF-8') as csv_file :
        writer = csv.writer(csv_file)
        writer.writerows(lines)

def overWrite(path, temp) :
    with open (path, 'w', newline='', encoding='UTF-8') as csv_file :
        writer = csv.writer(csv_file)
        writer.writerow(["NOME", "MATRICULA", "LOCOMOTIVA", "DATA", "HORA"])
        temp_lines = [reader.readLine(line) for line in temp]
        writer.writerows(temp_lines)

def writeAppend(path, line) :
    with open (path, 'a', newline='', encoding='UTF-8') as csv_file :
        writer = csv.writer(csv_file)
        writer.writerow(line)
        
def verifyFile(path) :
    if os.isfile(path):
        return True
    return False