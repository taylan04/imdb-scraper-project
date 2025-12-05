from ex1 import filmes
from models import *
from db import *

def criar_objetos(filmes):
    catalog = [Movie(filme['filme'],filme['ano'],filme['avaliacao']) for filme in filmes]
    catalog.append(Series("Stranger Things",2016,5,38))
    catalog.append(Series("The Last of Us",2023,2,16))
    return catalog

def exibir_objetos_com_str(midias):
    for midia in midias:
        print(midia)

midias = criar_objetos(filmes)
#exibir_objetos_com_str(midias)

for midia in midias:
    adicionar_no_banco(midia)


