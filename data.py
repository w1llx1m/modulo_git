import requests
from bs4 import BeautifulSoup
import csv

response = requests.get('https://g1.globo.com/')
data = response.content

"""Pegando conteudo de uma pagina com o request e avisando ao BeautifulSoup que 
Esse elemento é do tipo HTML com o 'html.parser' logo abaixo
"""

site = BeautifulSoup(data, 'html.parser')
news = site.findAll('div', attrs={'class': 'feed-post-body'})

"""O comando FindAll() gera um tipo de lista que pode ser iterável
"""


with open('noticias.csv', 'a', newline="") as arquivo:
    """abrindo primeiro em modo escrita
    """
    with open('noticias.csv') as aqr:
        """abrindo em modo leitura
        """
        escrevendo = csv.DictWriter(
            arquivo, fieldnames=['Titulo', 'Subtitulo', 'Link'])
        if len(aqr.read()) == 0:
            """verificando se o arquivo.csv está vazio. Se estiver adicionamos o writeheader() para escrever o cabeçalho
            """
            escrevendo.writeheader()
        for new in news:
            title = new.find(
                'a', attrs={'class': 'feed-post-link gui-color-primary gui-color-hover'})
            subtitle = new.find('a', attrs={
                'class': 'gui-color-primary gui-color-hover feed-post-body-title bstn-relatedtext'})
            if subtitle:
                """
                verifica se o subtitulo da noticia existe
                """
                escrevendo.writerow(
                    {'Titulo': title.text, 'Subtitulo': subtitle.text, 'Link': title['href']})
            else:
                escrevendo.writerow(
                    {'Titulo': title.text, 'Subtitulo': 'Sem subtitulo', 'Link': title['href']})
