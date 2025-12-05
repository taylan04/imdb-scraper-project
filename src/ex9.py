from ex7_8 import df_filmes

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

df_filmes['categoria'] = df_filmes['nota'].apply(categoria_textual)
print(df_filmes[['titulo', 'nota', 'categoria']].head(10))