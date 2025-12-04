class TV():
    def __init__(self, titulo, ano_lancamento):
        self.titulo = titulo
        self.ano_lancamento = ano_lancamento
    
    def __str__(self):
        print(f"\n{self.titulo}({self.ano_lancamento})")

class Movie(TV):
    def __init__(self, titulo, ano_lancamento, nota):
        super().__init__(titulo, ano_lancamento)
        self.nota = nota
    
    def __str__(self):
        print(f"\n{self.titulo}({self.ano_lancamento}) - Nota: {self.nota}")
    
class Series(TV):
    def __init__(self, titulo, ano_lancamento, temporadas, episodios):
        super().__init__(titulo, ano_lancamento)
        self.temporadas = temporadas
        self.episodios = episodios
    
    def __str__(self):
        print(f"\n{self.titulo}({self.ano_lancamento}) - Temporadas: {self.temporadas} - Episódios: {self.episodios}")