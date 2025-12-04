from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

URL = "https://www.imdb.com/pt/chart/top/"

def acessar_url(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        req = Request(url, headers=headers)
        html = urlopen(req)
        return html
    except Exception as ex:
        print(f"{ex}")
        exit()

    return html

def obter_dados_filmes(soup):
    filmes = []
    tags = soup.find_all("div", class_="sc-b4f120f6-0 bQhtuJ cli-children")
    for tag in tags:
        nome = tag.find("h3", class_="ipc-title__text").text.strip()
        ano = tag.find("span", class_="sc-b4f120f6-7 hoOxkw cli-title-metadata-item").text.strip()
        avaliacao = tag.find("span", class_="ipc-rating-star--rating").text.strip()
        filmes.append({"filme":nome, "ano":ano, "avaliacao":avaliacao})

    return filmes

def executar_scraping():
    html = acessar_url(URL)
    soup = BeautifulSoup(html, "html.parser")
    filmes = obter_dados_filmes(soup)
    return filmes

filmes = executar_scraping()

'''for filme in filmes[:10]:
    print(f"\n{filme['filme']}({filme['ano']}) - Nota: {filme['avaliacao']}")'''





    
    
