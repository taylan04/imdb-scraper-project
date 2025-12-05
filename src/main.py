from ex1_2 import *
from ex5_6 import *
from ex7_8 import *
from ex9_10 import *

# 1 e 2

def exibir_filmes_do_scraping():
    print("\nPrimeira e segunda questões juntas:\n")
    filmes = executar_scraping()
    for filme in filmes[:10]:
        print(f"{filme['filme']}({filme['ano']}) - Nota: {filme['avaliacao']}")

#exibir_filmes_do_scraping()

# 5

def lista_de_objetos():
    print("\nQuinta questão: Lista de objetos a partir do scraping\n")
    filmes = executar_scraping()
    midias = criar_objetos(filmes)
    exibir_objetos_com_str(midias)
    adicionar_no_banco_de_dados(midias)

#lista_de_objetos()

# 7 e 8

def exibir_dataframe_e_salvar():
    df_filmes = retornar_df_filmes()
    df_series = retornar_df_series()
    df_ordenado = retornar_dataframe_ordenado_e_filtrado(df_filmes)

    print(df_filmes.head())
    print(f"\n{df_series.head()}\n")
    print("\ndataframe filtrado: ")
    print(df_ordenado.head()) 

    salvar_em_csv(df_ordenado, "filmes")
    salvar_em_csv(df_series, "series")
    salvar_em_json(df_ordenado, "filmes")
    salvar_em_json(df_series, "series")

#exibir_dataframe_e_salvar()

# 9 e 10

def exibir_nova_coluna_e_resumo():
    df = retornar_df_filmes()
    df_filmes = adicionar_coluna_categoria(df)
    resumo = retornar_resumo(df_filmes)
    print(f"\n{df_filmes[['titulo', 'nota', 'categoria']].head(10)}")
    print(f"\nQuantos filmes existem em cada ano de lançamento?\n\n{resumo}")

#exibir_nova_coluna_e_resumo()