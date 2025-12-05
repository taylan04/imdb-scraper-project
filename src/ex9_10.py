
def categoria_textual(nota):
    nota = float(nota)
    if nota >= 9.0:
        return "Obra-prima"
    if 8.0 <= nota < 9.0:
        return "Excelente"
    if 7.0 <= nota < 8.0:
        return "Bom"
    if nota < 7:
        return "Mediano"

def adicionar_coluna_categoria(df):
    df['categoria'] = df['nota'].apply(categoria_textual)
    return df

# 10

def retornar_resumo(df):
    return df.groupby(["categoria", "ano"]).size().reset_index(name="quantidade")


