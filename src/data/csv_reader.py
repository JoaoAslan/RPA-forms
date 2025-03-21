# Code for read CSV
import pandas as pd
import datetime as dt

def printa():
    print("teste")

def readLine(config) :

    df = pd.read_csv(config.sheet)

    # Converting values to Integer and String
    df['MATRICULA'] = pd.to_numeric(df['MATRICULA'], errors='coerce')
    df['MATRICULA'] = df['MATRICULA'].fillna(0)
    df['MATRICULA'] = df['MATRICULA'].astype(int)

    df['LOCOMOTIVA'] = pd.to_numeric(df['LOCOMOTIVA'], errors='coerce')
    df['LOCOMOTIVA'] = df['LOCOMOTIVA'].fillna(0)
    df['LOCOMOTIVA'] = df['LOCOMOTIVA'].astype(str)
    df['LOCOMOTIVA'] = df['LOCOMOTIVA'].str.zfill(5)

    return df
    '''
    for index, row in df.iterrows() :

        if (index > 5) :
            break

        row_name = row["NOME DO COLABORADOR"]
        row_mat = row["MATRICULA"]
        row_loc = row["LOCOMOTIVA"]
        row_time = row["HORA"]
        
        name = str(row_name)
        mat = str(row_mat)
        loc = str(row_loc)
        
        # Time formatter
        time_split = row_time.split(":")
        time = [int(value) for value in time_split]
        date_temp = dt.datetime(2000, 1, 1,time[0],time[1],time[2])
        delta = dt.timedelta(minutes=10)
        final_date_temp = date_temp + delta

        start_time = date_temp.time()
        final_time = final_date_temp.time()

        # Date formatter
        col_data = row["DATA"]
        data_split = col_data.split("/")
        dataf = [int(valor) for valor in data_split]
        data = dt.date(dataf[2], dataf[1], dataf[0])

        print(row)
        print(f'{index}, {name}, {mat}, {loc}, {start_time} -> {final_time} {data}')'
    '''