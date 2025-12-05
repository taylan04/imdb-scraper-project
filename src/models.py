from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TV():
    def __init__(self, titulo, ano_lancamento):
        self.titulo = titulo
        self.ano_lancamento = ano_lancamento
    
    def __str__(self):
        return f"{self.titulo}({self.ano_lancamento})"

class Movie(Base, TV):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    ano_lancamento = Column(Integer)
    nota = Column(String)

    #pelo visto quando eu modifiquei pra inserir o Base, nao se usa mais super()
    def __init__(self, titulo, ano_lancamento, nota):
        TV.__init__(self, titulo, ano_lancamento)
        self.nota = nota
    
    def to_dict(self):
        return {
            "titulo": self.titulo,
            "ano": self.ano_lancamento,
            "nota": self.nota
        }

    def __str__(self):
        return f"{self.titulo}({self.ano_lancamento}) - Nota: {self.nota}"
    
class Series(Base, TV):
    __tablename__ = "series"

    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    ano_lancamento = Column(Integer)
    temporadas = Column(Integer)
    episodios = Column(Integer)

    def __init__(self, titulo, ano_lancamento, temporadas, episodios):
        TV.__init__(self, titulo, ano_lancamento)
        self.temporadas = temporadas
        self.episodios = episodios
    
    def to_dict(self):
        return {
            "titulo": self.titulo,
            "ano": self.ano_lancamento,
            "temporadas": self.temporadas,
            "episodios": self.episodios
        }

    def __str__(self):
        return f"{self.titulo}({self.ano_lancamento}) - Temporadas: {self.temporadas} - Episódios: {self.episodios}"