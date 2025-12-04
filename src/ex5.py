from ex1 import filmes
from models import *

def criar_objetos(filmes):
    catalog = [Movie(filme['filme'],filme['ano'],filme['avaliacao']) for filme in filmes]
    catalog.append(Series("Stranger Things",2016,5,38))
    catalog.append(Series("The Last of Us",2023,2,16))
    return catalog

midias = criar_objetos(filmes)

for midia in midias:
    print(midia)