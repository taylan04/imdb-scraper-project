from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *

banco = "data/imdb.db"

def conectar():
    try:
        engine = create_engine("sqlite:///"+banco)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind = engine)
        session = Session()
        return session
    except Exception as ex:
        print("Erro ao conectar ao banco:", ex)
        return None

session = conectar()