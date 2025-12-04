from models import *
from db import *
import pandas as pd

df_filmes = pd.DataFrame(f.to_dict() for f in consultar_do_banco(Movie))
df_series = pd.DataFrame(f.to_dict() for f in consultar_do_banco(Series))

print(df_filmes.head())
print(f"\n{df_series.head()}\n")