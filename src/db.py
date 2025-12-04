from conexao import *

def consultar_do_banco(classe):
    try:
        dados = session.query(classe).all()
        return dados
    except Exception as ex:
        print(f"\nErro: {ex}")

def adicionar_no_banco(obj):
    try:
        with session:
            session.add(obj)
            session.commit()
    except Exception as ex:
        print(f"\nErro: {ex}")