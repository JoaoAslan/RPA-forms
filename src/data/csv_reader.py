# Code for read CSV
import csv
import datetime as dt

def readCSV(path) :
    return csv.DictReader(open(path, 'r', encoding='utf-8'))

def validate(config, line, index=0) :
    try :
        name = line["NOME DO COLABORADOR"]
        mat = line["MATRICULA"]
        loc = line["LOCOMOTIVA"]
        time = line["HORA"]

        base_mats = tupleToList(baseToList(readCSV(config.base)), 1)
        if (not mat in base_mats) :
            raise ValueError()

        # Time formatter
        time_split = time.split(":")
        time = [int(value) for value in time_split]
        date_temp = dt.datetime(2000, 1, 1,time[0],time[1],time[2])
        delta = dt.timedelta(minutes=10)
        final_date_temp = date_temp + delta

        start_time = date_temp.time()
        final_time = final_date_temp.time()

        # Date formatter
        col_date = line["DATA"]
        data_split = col_date.split("/")
        datef = [int(valor) for valor in data_split]
        date = dt.date(datef[2], datef[1], datef[0])
        
        return [name, mat, loc, start_time, final_time, date]
    except ValueError as e:
        print("Error to validate index:", index)

def baseToList(csv) :
    return [[line["NOME"], line["MAT"]] for line in csv]

def tupleToList(tuple, index) :
    return [line[index] for line in tuple]