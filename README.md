# Projeto IMDb Scraping e Análise de Dados

### Descrição

Este projeto realiza **web scraping**, **modelagem de classes em Python**, **persistência em banco de dados com SQLAlchemy**, **análises com Pandas** e **exportação de dados** a partir da página *IMDb Top 250*.  
O objetivo é demonstrar conceitos fundamentais de scraping, POO, banco de dados e análise de dados em um fluxo completo — da coleta ao processamento.

### Funcionalidades

- **Scraping do IMDb Top 250**
  - Extração dos títulos dos filmes
  - Coleta de título, ano e nota (rating)
- **POO**
  - Classe base `TV`
  - Classes `Movie` e `Series` com sobrescrita de `__str__`
- **Banco de Dados (imdb.db)**
  - Tabelas `movies` e `series`
  - Inserção com tratamento de duplicatas
- **Análises com Pandas**
  - Leitura das tabelas do banco
  - Ordenação, filtragem e criação de categorias textuais
  - Resumo de filmes por categoria e ano
- **Exportação**
  - CSV e JSON para filmes e séries

### Tecnologias Utilizadas

- **Python 3.x**
- **SQLAlchemy**
- **SQLite**
- **Pandas**
- **BeautifulSoup4**
- **Requests**

---

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/taylan04/imdb-scraper-project.git
cd imdb-scraper-project
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

---

## Como Usar

### 1. Executar o programa:
```bash
python main.py
```

---

## Conceitos Demonstrados

- **Scraping com BeautifulSoup**
- **Extração e manipulação de HTML**
- **POO – herança, classes, método `__str__`**
- **Modelagem e persistência de dados**
- **SQLAlchemy ORM**
- **Tratamento de exceções**
- **Análises com DataFrames**
- **Classificação por categorias**
- **Agrupamento e sumarização (groupby)**
- **Exportação CSV e JSON**


