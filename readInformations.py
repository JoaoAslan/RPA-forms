import pandas as pd
import datetime as dt
import configparser

config = configparser.ConfigParser()
config.read('config/config.ini')

df = pd.read_csv(config['credenciais']['sheet'])

# Conversão dos valores das colunas MATRICULA e LOCOMOTIVA para Integer e String
df['MATRICULA'] = pd.to_numeric(df['MATRICULA'], errors='coerce')
df['MATRICULA'] = df['MATRICULA'].fillna(0)
df['MATRICULA'] = df['MATRICULA'].astype(int)

df['LOCOMOTIVA'] = pd.to_numeric(df['LOCOMOTIVA'], errors='coerce')
df['LOCOMOTIVA'] = df['LOCOMOTIVA'].fillna(0)
df['LOCOMOTIVA'] = df['LOCOMOTIVA'].astype(str)
df['LOCOMOTIVA'] = df['LOCOMOTIVA'].str.zfill(5)

for index, row in df.iterrows() :

    if (index > 5) :
        break

    col_nome = row["NOME DO COLABORADOR"]
    nome = str(col_nome)

    col_matricula = row["MATRICULA"]
    mat = str(col_matricula)

    col_locomotiva = row["LOCOMOTIVA"]
    loc = str(col_locomotiva)

    # FORMATAÇÃO DO TEMPO INICIAL E FINAL
    col_hora = row["HORA"]
    hora_split = col_hora.split(":")
    tempo = [int(valor) for valor in hora_split]

    data_arbritaria = dt.datetime(2000, 1, 1,tempo[0],tempo[1],tempo[2])
    delta = dt.timedelta(minutes=10)
    tempo_final_arbritario = data_arbritaria + delta

    tempo_inicio = data_arbritaria.time()
    tempo_final = tempo_final_arbritario.time()

    # FORMATAÇÃO DA DATA
    col_data = row["DATA"]
    data_split = col_data.split("/")
    dataf = [int(valor) for valor in data_split]
    data = dt.date(dataf[2], dataf[1], dataf[0])

    print(f'{index}, {nome}, {mat}, {loc}, {tempo_inicio} -> {tempo_final} {data}')


