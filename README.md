# Trabalho final - Algoritmos de Automação - Master em Jornalismo de Dados, Automação e Data Storytelling

Este repositório contém o trabalho desenvolvido pelo jornalista João Barbosa para a disciplina Algoritmos de Automação, do 3º trimestre do Master em Jornalismo de Dados, Automação e Data Storytelling do Insper.

O trabalho consiste em uma webpage desenvolvida em Flask para suportar raspadores dos portais de notícias Folha de S. Paulo, UOL, Veja, Valor Econômico e BBC, além de um robô no telegram que disponibiliza em tempo real as notícias mais lidas desses portais.

## Instalação das bibliotecas necessárias para o funcionamento do código

No requirements.txt:

```
Flask
gunicorn
python-dotenv
bs4
requests
pytz
```

No app.py:

```
import os
import requests
from flask import Flask, request, render_template, redirect
import bs4
import datetime
import pytz
```

## Exemplo de uso de um dos raspadores no site

Ao acessar o site do trabalho (https://render-5wce.onrender.com/), o usuário poderá escolher um dos raspadores. A função que chama o raspador da Veja, por exemplo, é a seguinte:

```
@app.route('/veja')
def veja():
    veja = requests.get('https://veja.abril.com.br/') 
    soup_veja = bs4.BeautifulSoup(veja.text, 'html.parser')
    raspagem_veja = soup_veja.find_all('section', {'class': 'block most-read dark'})
    conteudo_veja = raspagem_veja[0].find_all('div', {'class': 'our-carousel-item'})
    manchetes_veja = []

    for conteudo in conteudo_veja:
        titulo = conteudo.find('h2').text
        link = conteudo.find('a').get('href')
        manchetes_veja.append(f"{titulo}\n{link}")
    return render_template('veja.html', resultado = "\n\n".join(manchetes_veja))
  ```

Cada raspador tem sua própria lógica para conseguir extrair o título e o link das matérias da seção Mais Lidas de cada site.

## Funcionamento do robô do Telegram

Após a configuração do robô do Telegram, que pode ser vista aqui (https://encurtador.com.br/dxCX6), fiz um comando para configurar o Webhook.

```
token = "..." # substitua pelo seu token
url = "..." # substitua pela URL do seu site no Render que vai servir como um 'servidor'
dados = {"url": url}
resposta = requests.post(f"https://api.telegram.org/bot{token}/setWebhook", data=dados)
```
Feito esse processo, tudo deve estar funcionando.

## Pasta Templates

Na pasta Templates, estão todos os arquivos HTML que são renderizados com a função render template do Flask. Houve uma estilização básica com elementos CSS.
