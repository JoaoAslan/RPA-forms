# Code for read CSV
import csv
import datetime as dt

def readCSV(path) :
    with open(path, 'r', newline='', encoding='utf-8') as csv_file:
        reader = list(csv.DictReader(csv_file))
        return reader

def validate(base, line, index=0) :
    try :
        name = line["NOME"].upper()
        mat = line["MATRICULA"]
        loc = line["LOCOMOTIVA"]
        time = line["HORA"]
        
        base_mats = tupleToList(baseToList(readCSV(base)), 1)
        if (not mat in base_mats) :
            raise ValueError("Employee registration not exits")

        # Time formatter
        time_split = time.split(":")
        time = [int(value) for value in time_split]
        date_temp = dt.datetime(2000, 1, 1,time[0],time[1],time[2])
        delta = dt.timedelta(minutes=10)
        final_date_temp = date_temp + delta

        start_time = str(date_temp.time().strftime("%H:%M"))
        final_time = str(final_date_temp.time().strftime("%H:%M"))

        # Date formatter
        col_date = line["DATA"]
        data_split = col_date.split("/")
        datef = [int(valor) for valor in data_split]
        date = str(dt.date(datef[2], datef[1], datef[0]).strftime("%d/%m/%Y"))
        
        return [name, mat, loc, date, start_time, final_time]
    except Exception :
        raise Exception("Error to validate index:", index)

def readLine(line) :
    return [line["NOME"], line["MATRICULA"], line["LOCOMOTIVA"], line["DATA"], line["HORA"]]
    

def baseToList(csv) :
    return [[line["NOME"], line["MAT"]] for line in csv]

def tupleToList(tuple, index) :
    return [line[index] for line in tuple]