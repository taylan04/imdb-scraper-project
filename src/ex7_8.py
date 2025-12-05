from models import *
from db import *
import pandas as pd

def retornar_df_filmes():
    df = pd.DataFrame(f.to_dict() for f in consultar_do_banco(Movie))
    return df

def retornar_df_series():
    df = pd.DataFrame(f.to_dict() for f in consultar_do_banco(Series))
    return df

# 8

def retornar_dataframe_ordenado_e_filtrado(df):
    return df.sort_values(by="nota", ascending=False).loc[df['nota'] > "9"]

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


