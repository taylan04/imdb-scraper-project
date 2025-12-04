from sqlalchemy import Table, Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TV():
    def __init__(self, titulo, ano_lancamento):
        self.titulo = titulo
        self.ano_lancamento = ano_lancamento
    
    def __str__(self):
        return f"\n{self.titulo}({self.ano_lancamento})"

class Movie(TV):

    def __init__(self, titulo, ano_lancamento, nota):
        super().__init__(titulo, ano_lancamento)
        self.nota = nota
    
    def __str__(self):
        return f"\n{self.titulo}({self.ano_lancamento}) - Nota: {self.nota}"
    
class Series(TV):
    def __init__(self, titulo, ano_lancamento, temporadas, episodios):
        super().__init__(titulo, ano_lancamento)
        self.temporadas = temporadas
        self.episodios = episodios
    
    def __str__(self):
        return f"\n{self.titulo}({self.ano_lancamento}) - Temporadas: {self.temporadas} - Episódios: {self.episodios}"