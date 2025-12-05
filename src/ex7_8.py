from models import *
from db import *
import pandas as pd

df_filmes = pd.DataFrame(f.to_dict() for f in consultar_do_banco(Movie))
df_series = pd.DataFrame(f.to_dict() for f in consultar_do_banco(Series))

#print(df_filmes.head())
#print(f"\n{df_series.head()}\n")

# 8

df_filmes_filtrados = df_filmes.sort_values(by="nota", ascending=False).loc[df_filmes['nota'] > "9"]

#print(df_filmes_filtrados.head())

def salvar_em_csv(df, nome):
    try:
        df.to_csv(f'data/{nome}.csv', header=False, index=False) 
    except Exception as ex:
        print(f"Erro: {ex}")

def salvar_em_json(df, nome):
    try:
        df.to_json(f"data/{nome}.json", orient="records", indent=4, force_ascii=False)
    except Exception as ex:
        print(f"Erro: {ex}")

def salvar_dataframes_em_arquivos():
    salvar_em_csv(df_filmes_filtrados, "filmes")
    salvar_em_csv(df_series, "series")
    salvar_em_json(df_filmes_filtrados, "filmes")
    salvar_em_json(df_series, "series")

salvar_dataframes_em_arquivos()