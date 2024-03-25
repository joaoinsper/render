import os
import requests
from flask import Flask, request, render_template
import bs4
import datetime
import pytz

app = Flask(__name__)
BOT_TOKEN = os.environ['TELEGRAM_BOT_TOKEN']

@app.route("/")
def index():
  return "Olá, <b>tudo bem</b>?"

@app.route('/folha')
def folha():
    cookies = {
    '_cb': 'CTpmbmBXJa33CncFPm',
    '_pcid': '%7B%22browserId%22%3A%22l9hetq8rlb2memoe%22%7D',
    'cX_P': 'l9hetq8rlb2memoe',
    'BTCTL': '72',
    'nvg82721': '117ea28dfb10464c8a9bb5047910|2_337',
    'nav44768': '117ea28dfb067aace18fa5535410|2_337',
    '_hjSessionUser_2239427': 'eyJpZCI6IjFmZTQyMDQyLWMzMTItNTc5YS05ZTg0LWI4ZTgwZGFhOTFlMiIsImNyZWF0ZWQiOjE2NzAwMjMxMjUwNjQsImV4aXN0aW5nIjp0cnVlfQ==',
    '_ga_ED63YQWYC3': 'GS1.1.1670026896.2.0.1670026897.59.0.0',
    '_ga_7NE0W89XE2': 'GS1.1.1670026896.2.0.1670026897.59.0.0',
    '_v__chartbeat3': 'xZXbiBaELojBHVGaj',
    '_hjSessionUser_897662': 'eyJpZCI6IjU4MGE3MjRjLTcxYjQtNTAwMi04NjZjLTJmY2QxMzZjYWZjYSIsImNyZWF0ZWQiOjE2NjYyOTEzMTcyOTIsImV4aXN0aW5nIjp0cnVlfQ==',
    '_hjSessionUser_872296': 'eyJpZCI6Ijc4NzI5Y2ZhLTc2OTctNTIxNS1iY2I2LWQ3YjMwNDZmNDUwZCIsImNyZWF0ZWQiOjE2ODM3Njc0NzQ5NjUsImV4aXN0aW5nIjpmYWxzZX0=',
    '_pcus': 'eyJ1c2VyU2VnbWVudHMiOm51bGx9',
    '_pctx': '%7Bu%7DN4IgrgzgpgThIC5gF8A05owMoBcCGOkiIeAdgPakjoQCWOUAkgCbECMbAzAOwAs3ATgFsADNwBM4tuM4iAbGxDIgA',
    '_hjSessionUser_569021': 'eyJpZCI6IjhhOTQ2OGIwLWQxMzgtNTY5Mi04YWY2LWJkMzZhZTczM2VjNSIsImNyZWF0ZWQiOjE2ODUwNjY4MDc0OTgsImV4aXN0aW5nIjp0cnVlfQ==',
    'mmapi.p.pd': '%22bTV91owfKQEDPelpQ5zHRBCGW-qFK87FRerkHuTdH_Q%3D%7CAgAAAApDH4sIAAAAAAAEAGNh0G6Xtzgk1t3EwJyZmMIoxMDoxGD6n8OaiWHDgm-Fgu23PVwDOA4-uHvLgwEI_kMBA5tLZlFqcgnjTHFGkDgYwCRBNFSI0RUA94LJv2EAAAA%3D%22',
    'mmapi.p.srv': '%22prodiadcgus02%22',
    '_hjSessionUser_1045640': 'eyJpZCI6ImYyNjQ3YWQ4LTA5ODEtNThhNi05NDUwLWVlOTAxMzE1OTJjMiIsImNyZWF0ZWQiOjE2NzEwMjg2NTQ0MzQsImV4aXN0aW5nIjp0cnVlfQ==',
    '_tt_enable_cookie': '1',
    '_ttp': 'uLkpC0yW1Z4hz3Sg13G1VDZJM4f',
    '_ga_S8XGH3WKZH': 'GS1.1.1689631319.2.0.1689631327.52.0.0',
    'cto_bundle': 'h8gfAF94dFVLYiUyRk5aazRnMFA1cU5WVnhxVWJjU25MTWxNMzd3RW9GRm1taCUyQnolMkJsaDJRS1NQMldlbjBGcHpYUVFQc0g3WVp6cXlxOXhtVzVlTmtRSFJ5Y2RKc3Yybkd6UFF1ZHFEOVExbklaQVVLQnJLS2ElMkJKOE9NMVBJd3o1RjBXJTJCdVIyeEdaSER4VyUyRnJqaTh6SXI3TUM3SFIxNHZlOVFLVVRYanR0bGhsT080aSUyQk1KczZRNkVPZTZabWE0N2VTQkNmYw',
    'cto_bidid': 'dv4axF9YWngyaFBtaUZhUVNOSktFQThmY2FuQTE3MGgzemRiYUdoeVV3bmxDUDNGeWdCSmlob3p0dTdyeEFqWFlHaXVLZU5lNG9BOE5PVUZhcnA4UmJRNEl0Z2oycWFvU05uY25vUDNiTjRkODQ1UEttOTdiZ0pyazlIMnhIcFFncVZobXRFdzVhQjBCRE5aNjVTN1BWZDdqTWclM0QlM0Q',
    '_ga': 'GA1.3.584149080.1666291313',
    '_chartbeat2': '.1666291313283.1690411637301.0000100000000001.CevxcV20u1DDDg9E-3ZRz0Cjp8I5.2',
    'FCNEC': '%5B%5B%22AKsRol9mnqpol2qytzFXQR4-HPl-wBkW5XJPlnUT8o1FwpGTNzMMuHTjdoIrw62vvdadhhzG5doJWJZN5YZFGn75SsT-HtMHaYx5F1Z9dH1KMqG5HM25Vf4QHgLOgGL2iahEaGUsLT_aVOPlMWS8Slttq23_z0dtug%3D%3D%22%5D%2Cnull%2C%5B%5B5%2C%22762%22%5D%5D%5D',
    '__gads': 'ID=91d9e74560346bbf:T=1666291313:RT=1690411695:S=ALNI_MY2NVMzeAdYI0YVnu5VbVFsWqvKvg',
    '__gpi': 'UID=00000986060da399:T=1666291313:RT=1690411695:S=ALNI_MbEAgxjQMAYp-hUm_THm50Mn6OikQ',
    '_ga_BS4Q6LCGB1': 'GS1.1.1690411374.9.1.1690411696.59.0.0',
    '__tbc': '%7Bkpex%7D7LqbQz_kKgGwRsKIaHW2YSE4aPBsfrbF9uNv3xEbAGtd6BuAasGqVTonMHIxP8zr',
    'xbc': '%7Bkpex%7Dx2xmlGVXcEY7i4Bm7n1PY6093kktn1LzlF6uGyi7Qq8C4_WNTHy6gl-GaICqOfrW2QNbwp66gg1z1hdBi_hUoSimV02c-1_16rkugz7CBIold0YSxXNglIF4pEvKVl_djrmaThSp37lLxWSwAAIFkqVZm0BA9F_Q734lg6fPTU-YZi9y1H33_PO4Bsql7J2NT_GcFJHiiJo8U1T5f-dMwK85xCY1-nER93ZyxAQsmCe11cjaXNYRCliK_x4PyKePDfuxdhpAxhIJCx6bvBEEAny2K3jlRPSvPdJ6stRZfMkiESXmP-9dsfUMHLTqSY8ariTQrWkAJbWJ-Ww0HrF-a_jEJUYW1KXmC89iKpkUIC6vWIYj8Tb0gykaJsUn39repSQRiA-RcI0tM3vfhnVS11V7LSlpqPnrYvQixZY-8Ow7R6kMJNLNQyEKQkZJLpLOu_C_lFZabZXgXjeD1ZNdfIoJhxa8WWfiBVqXgd0S5VReqDX3Sd439nOmfYmcB98sy_Rn9v_Jbokka6_0IB10yMCE8bPrqJ_Uw4hsxswg7Kl6Y7RSbzuFk7TINEPrI0WVIBQFFull-FLt3XMVi4k5y-ksk0tlrwQEganKDa6Jsk34RXFHIGrSAcWTaYQLKUThxAQ--GP89UyHTcIR1pupcDiiYQLup1z0lxoYlM6cltjZpeiBeJK_MD2nrwdmZBQsvrqbtJV3VXSdPZQ80MZE_6H9tFo_I0W-grYQtuBsdnGbRZUAmuIN4-1qXUIn5Fq-PoElOVWlyM6w320kuwUfuvomlcYzjlD3bKM8YvhTkVjpMp_hBTDx8j5SwCoiWpjyXqV1ZP9UZemhScBn1DstE4ZDDTV8j131OKS8siNgG776GxryMNX1nVQ56gMYMyk3yhAxnqsGZW6eySY08UdaovwA5pM4Umc7Qly_W_aVet8cQU-49mhvCTv0CLBIaGgGzoQsNB-hGNZcYLBQkVHTyeGnTzIZmzu6qKOUkLTW5rjDXopeVsqmmUUEGozXWD-K9St_jkglxIwRa8jBPo7gDaH9kt_YgiKdcmzaFIARwqSdK2adTLxZFXlsv_k6bMGN',
    'folha_ga_userType': 'not_logged',
    'folha_ga_loginType': 'folha',
    'folha_ga_userGroup': 'none',
    'folha_ga_swgt': 'none',
    }

    headers = {
    'authority': 'www1.folha.uol.com.br',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': '_cb=CTpmbmBXJa33CncFPm; _pcid=%7B%22browserId%22%3A%22l9hetq8rlb2memoe%22%7D; cX_P=l9hetq8rlb2memoe; BTCTL=72; nvg82721=117ea28dfb10464c8a9bb5047910|2_337; nav44768=117ea28dfb067aace18fa5535410|2_337; _hjSessionUser_2239427=eyJpZCI6IjFmZTQyMDQyLWMzMTItNTc5YS05ZTg0LWI4ZTgwZGFhOTFlMiIsImNyZWF0ZWQiOjE2NzAwMjMxMjUwNjQsImV4aXN0aW5nIjp0cnVlfQ==; _ga_ED63YQWYC3=GS1.1.1670026896.2.0.1670026897.59.0.0; _ga_7NE0W89XE2=GS1.1.1670026896.2.0.1670026897.59.0.0; _v__chartbeat3=xZXbiBaELojBHVGaj; _hjSessionUser_897662=eyJpZCI6IjU4MGE3MjRjLTcxYjQtNTAwMi04NjZjLTJmY2QxMzZjYWZjYSIsImNyZWF0ZWQiOjE2NjYyOTEzMTcyOTIsImV4aXN0aW5nIjp0cnVlfQ==; _hjSessionUser_872296=eyJpZCI6Ijc4NzI5Y2ZhLTc2OTctNTIxNS1iY2I2LWQ3YjMwNDZmNDUwZCIsImNyZWF0ZWQiOjE2ODM3Njc0NzQ5NjUsImV4aXN0aW5nIjpmYWxzZX0=; _pcus=eyJ1c2VyU2VnbWVudHMiOm51bGx9; _pctx=%7Bu%7DN4IgrgzgpgThIC5gF8A05owMoBcCGOkiIeAdgPakjoQCWOUAkgCbECMbAzAOwAs3ATgFsADNwBM4tuM4iAbGxDIgA; _hjSessionUser_569021=eyJpZCI6IjhhOTQ2OGIwLWQxMzgtNTY5Mi04YWY2LWJkMzZhZTczM2VjNSIsImNyZWF0ZWQiOjE2ODUwNjY4MDc0OTgsImV4aXN0aW5nIjp0cnVlfQ==; mmapi.p.pd=%22bTV91owfKQEDPelpQ5zHRBCGW-qFK87FRerkHuTdH_Q%3D%7CAgAAAApDH4sIAAAAAAAEAGNh0G6Xtzgk1t3EwJyZmMIoxMDoxGD6n8OaiWHDgm-Fgu23PVwDOA4-uHvLgwEI_kMBA5tLZlFqcgnjTHFGkDgYwCRBNFSI0RUA94LJv2EAAAA%3D%22; mmapi.p.srv=%22prodiadcgus02%22; _hjSessionUser_1045640=eyJpZCI6ImYyNjQ3YWQ4LTA5ODEtNThhNi05NDUwLWVlOTAxMzE1OTJjMiIsImNyZWF0ZWQiOjE2NzEwMjg2NTQ0MzQsImV4aXN0aW5nIjp0cnVlfQ==; _tt_enable_cookie=1; _ttp=uLkpC0yW1Z4hz3Sg13G1VDZJM4f; _ga_S8XGH3WKZH=GS1.1.1689631319.2.0.1689631327.52.0.0; cto_bundle=h8gfAF94dFVLYiUyRk5aazRnMFA1cU5WVnhxVWJjU25MTWxNMzd3RW9GRm1taCUyQnolMkJsaDJRS1NQMldlbjBGcHpYUVFQc0g3WVp6cXlxOXhtVzVlTmtRSFJ5Y2RKc3Yybkd6UFF1ZHFEOVExbklaQVVLQnJLS2ElMkJKOE9NMVBJd3o1RjBXJTJCdVIyeEdaSER4VyUyRnJqaTh6SXI3TUM3SFIxNHZlOVFLVVRYanR0bGhsT080aSUyQk1KczZRNkVPZTZabWE0N2VTQkNmYw; cto_bidid=dv4axF9YWngyaFBtaUZhUVNOSktFQThmY2FuQTE3MGgzemRiYUdoeVV3bmxDUDNGeWdCSmlob3p0dTdyeEFqWFlHaXVLZU5lNG9BOE5PVUZhcnA4UmJRNEl0Z2oycWFvU05uY25vUDNiTjRkODQ1UEttOTdiZ0pyazlIMnhIcFFncVZobXRFdzVhQjBCRE5aNjVTN1BWZDdqTWclM0QlM0Q; _ga=GA1.3.584149080.1666291313; _chartbeat2=.1666291313283.1690411637301.0000100000000001.CevxcV20u1DDDg9E-3ZRz0Cjp8I5.2; FCNEC=%5B%5B%22AKsRol9mnqpol2qytzFXQR4-HPl-wBkW5XJPlnUT8o1FwpGTNzMMuHTjdoIrw62vvdadhhzG5doJWJZN5YZFGn75SsT-HtMHaYx5F1Z9dH1KMqG5HM25Vf4QHgLOgGL2iahEaGUsLT_aVOPlMWS8Slttq23_z0dtug%3D%3D%22%5D%2Cnull%2C%5B%5B5%2C%22762%22%5D%5D%5D; __gads=ID=91d9e74560346bbf:T=1666291313:RT=1690411695:S=ALNI_MY2NVMzeAdYI0YVnu5VbVFsWqvKvg; __gpi=UID=00000986060da399:T=1666291313:RT=1690411695:S=ALNI_MbEAgxjQMAYp-hUm_THm50Mn6OikQ; _ga_BS4Q6LCGB1=GS1.1.1690411374.9.1.1690411696.59.0.0; __tbc=%7Bkpex%7D7LqbQz_kKgGwRsKIaHW2YSE4aPBsfrbF9uNv3xEbAGtd6BuAasGqVTonMHIxP8zr; xbc=%7Bkpex%7Dx2xmlGVXcEY7i4Bm7n1PY6093kktn1LzlF6uGyi7Qq8C4_WNTHy6gl-GaICqOfrW2QNbwp66gg1z1hdBi_hUoSimV02c-1_16rkugz7CBIold0YSxXNglIF4pEvKVl_djrmaThSp37lLxWSwAAIFkqVZm0BA9F_Q734lg6fPTU-YZi9y1H33_PO4Bsql7J2NT_GcFJHiiJo8U1T5f-dMwK85xCY1-nER93ZyxAQsmCe11cjaXNYRCliK_x4PyKePDfuxdhpAxhIJCx6bvBEEAny2K3jlRPSvPdJ6stRZfMkiESXmP-9dsfUMHLTqSY8ariTQrWkAJbWJ-Ww0HrF-a_jEJUYW1KXmC89iKpkUIC6vWIYj8Tb0gykaJsUn39repSQRiA-RcI0tM3vfhnVS11V7LSlpqPnrYvQixZY-8Ow7R6kMJNLNQyEKQkZJLpLOu_C_lFZabZXgXjeD1ZNdfIoJhxa8WWfiBVqXgd0S5VReqDX3Sd439nOmfYmcB98sy_Rn9v_Jbokka6_0IB10yMCE8bPrqJ_Uw4hsxswg7Kl6Y7RSbzuFk7TINEPrI0WVIBQFFull-FLt3XMVi4k5y-ksk0tlrwQEganKDa6Jsk34RXFHIGrSAcWTaYQLKUThxAQ--GP89UyHTcIR1pupcDiiYQLup1z0lxoYlM6cltjZpeiBeJK_MD2nrwdmZBQsvrqbtJV3VXSdPZQ80MZE_6H9tFo_I0W-grYQtuBsdnGbRZUAmuIN4-1qXUIn5Fq-PoElOVWlyM6w320kuwUfuvomlcYzjlD3bKM8YvhTkVjpMp_hBTDx8j5SwCoiWpjyXqV1ZP9UZemhScBn1DstE4ZDDTV8j131OKS8siNgG776GxryMNX1nVQ56gMYMyk3yhAxnqsGZW6eySY08UdaovwA5pM4Umc7Qly_W_aVet8cQU-49mhvCTv0CLBIaGgGzoQsNB-hGNZcYLBQkVHTyeGnTzIZmzu6qKOUkLTW5rjDXopeVsqmmUUEGozXWD-K9St_jkglxIwRa8jBPo7gDaH9kt_YgiKdcmzaFIARwqSdK2adTLxZFXlsv_k6bMGN; folha_ga_userType=not_logged; folha_ga_loginType=folha; folha_ga_userGroup=none; folha_ga_swgt=none',
    'dnt': '1',
    'referer': 'https://www1.folha.uol.com.br/maispopulares/',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    }

    params = {
    'qs': '20231082054',
    }

    response = requests.get(
    'https://www1.folha.uol.com.br/virtual/spiffy/mais-lidas/home-1.0.0.json',
    params=params,
    cookies=cookies,
    headers=headers,
    )

    mais_lidas_f = response.json()
    manchetes_folha = []
    for item in mais_lidas_f[0:10]:
        titulo = (item['title'])
        link = (item['url'])
        manchetes_folha.append(f"{titulo}\n{link}")
        manchetes_folha = [line.replace("&apos;", "'") for line in manchetes_folha]
    return render_template('folha.html', resultado = "\n\n".join(manchetes_folha))

@app.route('/uol')
def uol():
    result = requests.get('https://www.uol.com.br/')
    soup_uol = bs4.BeautifulSoup(result.text, 'html.parser')
    raspagem_uol = soup_uol.find_all('li', {'class': 'mostRead__item'})
    manchetes_uol = []

    for li in raspagem_uol:
        azinho = li.find('a')
        link = azinho.get('href')
        titulo = azinho.get('title')
        manchetes_uol.append(f"{titulo}\n{link}")
    return render_template('uol.html', resultado = "\n\n".join(manchetes_uol))

@app.route('/bbc')
def bbc():
    bbc = requests.get('https://www.bbc.com/portuguese/popular/read')
    soup_bbc = bs4.BeautifulSoup(bbc.text, 'html.parser')
    raspagem_bbc = soup_bbc.find_all('div', {'class': 'bbc-14zb6im'})
    manchetes_bbc = []

    for conteudo in raspagem_bbc:
        titulo = conteudo.text
        link = conteudo.find('a').get('href')
        manchetes_bbc.append(f"{titulo}\n{link}")
    return render_template('bbc.html', resultado = "\n\n".join(manchetes_bbc))

@app.route("/telegram", methods=["POST"])
def telegram():
  url_msg = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
  update = request.json
  fname = update["message"]["from"]["first_name"]
  txt = update["message"]["text"]

  mensagem_start = "Eu sou um raspador de notícias e posso te ajudar a verificar quais são as notícias mais lidas em alguns portais neste exato momento.\
\n\nEscolha uma das opções abaixo:\n\n/bbc: Veja as notícias mais lidas da BBC Brasil.\n\
/veja: Veja as notícias mais lidas da revista Veja.\n\
/folha: Veja as notícias mais lidas da Folha de S.Paulo.\n\
/valor: Veja as notícias mais lidas do Valor Econômico.\n\
/uol: Veja as notícias mais lidas do UOL."

  if txt == "/start":
    requests.post(url_msg, data={"chat_id": update["message"]["chat"]["id"], "text": f'Olá, {fname}, bem-vindo! {mensagem_start}'})
    print("Resposta enviada ao start.")

  elif txt == "/bbc":
    requests.post(url_msg, data={"chat_id": update["message"]["chat"]["id"], "text": f'{fname}, essa é a relação das notícias mais lidas da BBC Brasil feito em {horario_raspagem()}. \n\n{raspador_bbc()}'})
    print("Resposta enviada ao bbc.")

  elif txt == "/veja":
    requests.post(url_msg, data={"chat_id": update["message"]["chat"]["id"], "text": f'{fname}, essa é a relação das notícias mais lidas da revista Veja feito em {horario_raspagem()}. \n\n{raspador_veja()}'})
    print("Resposta enviada ao veja.")

  elif txt == "/folha":
    requests.post(url_msg, data={"chat_id": update["message"]["chat"]["id"], "text": f'{fname}, essa é a relação das notícias mais lidas da Folha de S. Paulo feito em {horario_raspagem()}. \n\n{raspador_folha()}'})
    print("Resposta enviada ao folha.")

  elif txt == "/valor":
    requests.post(url_msg, data={"chat_id": update["message"]["chat"]["id"], "text": f'{fname}, essa é a relação das notícias mais lidas do Valor Econômico feito em {horario_raspagem()}. \n\n{raspador_valor()}'})
    print("Resposta enviada ao Valor Econômico.")  

  elif txt == "/uol":
    requests.post(url_msg, data={"chat_id": update["message"]["chat"]["id"], "text": f'{fname}, essa é a relação das notícias mais lidas do UOL feito em {horario_raspagem()}. \n\n{raspador_uol()}'})
    print("Resposta enviada ao UOL.")  

  else:
    requests.post(url_msg, data={"chat_id": update["message"]["chat"]["id"] , "text": 'Desculpe, mas não entendi.'})
    print("Resposta enviada ao else.")
    
  return "ok"


### FOLHA ###

def raspador_folha():
    
    cookies = {
    '_cb': 'CTpmbmBXJa33CncFPm',
    '_pcid': '%7B%22browserId%22%3A%22l9hetq8rlb2memoe%22%7D',
    'cX_P': 'l9hetq8rlb2memoe',
    'BTCTL': '72',
    'nvg82721': '117ea28dfb10464c8a9bb5047910|2_337',
    'nav44768': '117ea28dfb067aace18fa5535410|2_337',
    '_hjSessionUser_2239427': 'eyJpZCI6IjFmZTQyMDQyLWMzMTItNTc5YS05ZTg0LWI4ZTgwZGFhOTFlMiIsImNyZWF0ZWQiOjE2NzAwMjMxMjUwNjQsImV4aXN0aW5nIjp0cnVlfQ==',
    '_ga_ED63YQWYC3': 'GS1.1.1670026896.2.0.1670026897.59.0.0',
    '_ga_7NE0W89XE2': 'GS1.1.1670026896.2.0.1670026897.59.0.0',
    '_v__chartbeat3': 'xZXbiBaELojBHVGaj',
    '_hjSessionUser_897662': 'eyJpZCI6IjU4MGE3MjRjLTcxYjQtNTAwMi04NjZjLTJmY2QxMzZjYWZjYSIsImNyZWF0ZWQiOjE2NjYyOTEzMTcyOTIsImV4aXN0aW5nIjp0cnVlfQ==',
    '_hjSessionUser_872296': 'eyJpZCI6Ijc4NzI5Y2ZhLTc2OTctNTIxNS1iY2I2LWQ3YjMwNDZmNDUwZCIsImNyZWF0ZWQiOjE2ODM3Njc0NzQ5NjUsImV4aXN0aW5nIjpmYWxzZX0=',
    '_pcus': 'eyJ1c2VyU2VnbWVudHMiOm51bGx9',
    '_pctx': '%7Bu%7DN4IgrgzgpgThIC5gF8A05owMoBcCGOkiIeAdgPakjoQCWOUAkgCbECMbAzAOwAs3ATgFsADNwBM4tuM4iAbGxDIgA',
    '_hjSessionUser_569021': 'eyJpZCI6IjhhOTQ2OGIwLWQxMzgtNTY5Mi04YWY2LWJkMzZhZTczM2VjNSIsImNyZWF0ZWQiOjE2ODUwNjY4MDc0OTgsImV4aXN0aW5nIjp0cnVlfQ==',
    'mmapi.p.pd': '%22bTV91owfKQEDPelpQ5zHRBCGW-qFK87FRerkHuTdH_Q%3D%7CAgAAAApDH4sIAAAAAAAEAGNh0G6Xtzgk1t3EwJyZmMIoxMDoxGD6n8OaiWHDgm-Fgu23PVwDOA4-uHvLgwEI_kMBA5tLZlFqcgnjTHFGkDgYwCRBNFSI0RUA94LJv2EAAAA%3D%22',
    'mmapi.p.srv': '%22prodiadcgus02%22',
    '_hjSessionUser_1045640': 'eyJpZCI6ImYyNjQ3YWQ4LTA5ODEtNThhNi05NDUwLWVlOTAxMzE1OTJjMiIsImNyZWF0ZWQiOjE2NzEwMjg2NTQ0MzQsImV4aXN0aW5nIjp0cnVlfQ==',
    '_tt_enable_cookie': '1',
    '_ttp': 'uLkpC0yW1Z4hz3Sg13G1VDZJM4f',
    '_ga_S8XGH3WKZH': 'GS1.1.1689631319.2.0.1689631327.52.0.0',
    'cto_bundle': 'h8gfAF94dFVLYiUyRk5aazRnMFA1cU5WVnhxVWJjU25MTWxNMzd3RW9GRm1taCUyQnolMkJsaDJRS1NQMldlbjBGcHpYUVFQc0g3WVp6cXlxOXhtVzVlTmtRSFJ5Y2RKc3Yybkd6UFF1ZHFEOVExbklaQVVLQnJLS2ElMkJKOE9NMVBJd3o1RjBXJTJCdVIyeEdaSER4VyUyRnJqaTh6SXI3TUM3SFIxNHZlOVFLVVRYanR0bGhsT080aSUyQk1KczZRNkVPZTZabWE0N2VTQkNmYw',
    'cto_bidid': 'dv4axF9YWngyaFBtaUZhUVNOSktFQThmY2FuQTE3MGgzemRiYUdoeVV3bmxDUDNGeWdCSmlob3p0dTdyeEFqWFlHaXVLZU5lNG9BOE5PVUZhcnA4UmJRNEl0Z2oycWFvU05uY25vUDNiTjRkODQ1UEttOTdiZ0pyazlIMnhIcFFncVZobXRFdzVhQjBCRE5aNjVTN1BWZDdqTWclM0QlM0Q',
    '_ga': 'GA1.3.584149080.1666291313',
    '_chartbeat2': '.1666291313283.1690411637301.0000100000000001.CevxcV20u1DDDg9E-3ZRz0Cjp8I5.2',
    'FCNEC': '%5B%5B%22AKsRol9mnqpol2qytzFXQR4-HPl-wBkW5XJPlnUT8o1FwpGTNzMMuHTjdoIrw62vvdadhhzG5doJWJZN5YZFGn75SsT-HtMHaYx5F1Z9dH1KMqG5HM25Vf4QHgLOgGL2iahEaGUsLT_aVOPlMWS8Slttq23_z0dtug%3D%3D%22%5D%2Cnull%2C%5B%5B5%2C%22762%22%5D%5D%5D',
    '__gads': 'ID=91d9e74560346bbf:T=1666291313:RT=1690411695:S=ALNI_MY2NVMzeAdYI0YVnu5VbVFsWqvKvg',
    '__gpi': 'UID=00000986060da399:T=1666291313:RT=1690411695:S=ALNI_MbEAgxjQMAYp-hUm_THm50Mn6OikQ',
    '_ga_BS4Q6LCGB1': 'GS1.1.1690411374.9.1.1690411696.59.0.0',
    '__tbc': '%7Bkpex%7D7LqbQz_kKgGwRsKIaHW2YSE4aPBsfrbF9uNv3xEbAGtd6BuAasGqVTonMHIxP8zr',
    'xbc': '%7Bkpex%7Dx2xmlGVXcEY7i4Bm7n1PY6093kktn1LzlF6uGyi7Qq8C4_WNTHy6gl-GaICqOfrW2QNbwp66gg1z1hdBi_hUoSimV02c-1_16rkugz7CBIold0YSxXNglIF4pEvKVl_djrmaThSp37lLxWSwAAIFkqVZm0BA9F_Q734lg6fPTU-YZi9y1H33_PO4Bsql7J2NT_GcFJHiiJo8U1T5f-dMwK85xCY1-nER93ZyxAQsmCe11cjaXNYRCliK_x4PyKePDfuxdhpAxhIJCx6bvBEEAny2K3jlRPSvPdJ6stRZfMkiESXmP-9dsfUMHLTqSY8ariTQrWkAJbWJ-Ww0HrF-a_jEJUYW1KXmC89iKpkUIC6vWIYj8Tb0gykaJsUn39repSQRiA-RcI0tM3vfhnVS11V7LSlpqPnrYvQixZY-8Ow7R6kMJNLNQyEKQkZJLpLOu_C_lFZabZXgXjeD1ZNdfIoJhxa8WWfiBVqXgd0S5VReqDX3Sd439nOmfYmcB98sy_Rn9v_Jbokka6_0IB10yMCE8bPrqJ_Uw4hsxswg7Kl6Y7RSbzuFk7TINEPrI0WVIBQFFull-FLt3XMVi4k5y-ksk0tlrwQEganKDa6Jsk34RXFHIGrSAcWTaYQLKUThxAQ--GP89UyHTcIR1pupcDiiYQLup1z0lxoYlM6cltjZpeiBeJK_MD2nrwdmZBQsvrqbtJV3VXSdPZQ80MZE_6H9tFo_I0W-grYQtuBsdnGbRZUAmuIN4-1qXUIn5Fq-PoElOVWlyM6w320kuwUfuvomlcYzjlD3bKM8YvhTkVjpMp_hBTDx8j5SwCoiWpjyXqV1ZP9UZemhScBn1DstE4ZDDTV8j131OKS8siNgG776GxryMNX1nVQ56gMYMyk3yhAxnqsGZW6eySY08UdaovwA5pM4Umc7Qly_W_aVet8cQU-49mhvCTv0CLBIaGgGzoQsNB-hGNZcYLBQkVHTyeGnTzIZmzu6qKOUkLTW5rjDXopeVsqmmUUEGozXWD-K9St_jkglxIwRa8jBPo7gDaH9kt_YgiKdcmzaFIARwqSdK2adTLxZFXlsv_k6bMGN',
    'folha_ga_userType': 'not_logged',
    'folha_ga_loginType': 'folha',
    'folha_ga_userGroup': 'none',
    'folha_ga_swgt': 'none',
    }

    headers = {
    'authority': 'www1.folha.uol.com.br',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': '_cb=CTpmbmBXJa33CncFPm; _pcid=%7B%22browserId%22%3A%22l9hetq8rlb2memoe%22%7D; cX_P=l9hetq8rlb2memoe; BTCTL=72; nvg82721=117ea28dfb10464c8a9bb5047910|2_337; nav44768=117ea28dfb067aace18fa5535410|2_337; _hjSessionUser_2239427=eyJpZCI6IjFmZTQyMDQyLWMzMTItNTc5YS05ZTg0LWI4ZTgwZGFhOTFlMiIsImNyZWF0ZWQiOjE2NzAwMjMxMjUwNjQsImV4aXN0aW5nIjp0cnVlfQ==; _ga_ED63YQWYC3=GS1.1.1670026896.2.0.1670026897.59.0.0; _ga_7NE0W89XE2=GS1.1.1670026896.2.0.1670026897.59.0.0; _v__chartbeat3=xZXbiBaELojBHVGaj; _hjSessionUser_897662=eyJpZCI6IjU4MGE3MjRjLTcxYjQtNTAwMi04NjZjLTJmY2QxMzZjYWZjYSIsImNyZWF0ZWQiOjE2NjYyOTEzMTcyOTIsImV4aXN0aW5nIjp0cnVlfQ==; _hjSessionUser_872296=eyJpZCI6Ijc4NzI5Y2ZhLTc2OTctNTIxNS1iY2I2LWQ3YjMwNDZmNDUwZCIsImNyZWF0ZWQiOjE2ODM3Njc0NzQ5NjUsImV4aXN0aW5nIjpmYWxzZX0=; _pcus=eyJ1c2VyU2VnbWVudHMiOm51bGx9; _pctx=%7Bu%7DN4IgrgzgpgThIC5gF8A05owMoBcCGOkiIeAdgPakjoQCWOUAkgCbECMbAzAOwAs3ATgFsADNwBM4tuM4iAbGxDIgA; _hjSessionUser_569021=eyJpZCI6IjhhOTQ2OGIwLWQxMzgtNTY5Mi04YWY2LWJkMzZhZTczM2VjNSIsImNyZWF0ZWQiOjE2ODUwNjY4MDc0OTgsImV4aXN0aW5nIjp0cnVlfQ==; mmapi.p.pd=%22bTV91owfKQEDPelpQ5zHRBCGW-qFK87FRerkHuTdH_Q%3D%7CAgAAAApDH4sIAAAAAAAEAGNh0G6Xtzgk1t3EwJyZmMIoxMDoxGD6n8OaiWHDgm-Fgu23PVwDOA4-uHvLgwEI_kMBA5tLZlFqcgnjTHFGkDgYwCRBNFSI0RUA94LJv2EAAAA%3D%22; mmapi.p.srv=%22prodiadcgus02%22; _hjSessionUser_1045640=eyJpZCI6ImYyNjQ3YWQ4LTA5ODEtNThhNi05NDUwLWVlOTAxMzE1OTJjMiIsImNyZWF0ZWQiOjE2NzEwMjg2NTQ0MzQsImV4aXN0aW5nIjp0cnVlfQ==; _tt_enable_cookie=1; _ttp=uLkpC0yW1Z4hz3Sg13G1VDZJM4f; _ga_S8XGH3WKZH=GS1.1.1689631319.2.0.1689631327.52.0.0; cto_bundle=h8gfAF94dFVLYiUyRk5aazRnMFA1cU5WVnhxVWJjU25MTWxNMzd3RW9GRm1taCUyQnolMkJsaDJRS1NQMldlbjBGcHpYUVFQc0g3WVp6cXlxOXhtVzVlTmtRSFJ5Y2RKc3Yybkd6UFF1ZHFEOVExbklaQVVLQnJLS2ElMkJKOE9NMVBJd3o1RjBXJTJCdVIyeEdaSER4VyUyRnJqaTh6SXI3TUM3SFIxNHZlOVFLVVRYanR0bGhsT080aSUyQk1KczZRNkVPZTZabWE0N2VTQkNmYw; cto_bidid=dv4axF9YWngyaFBtaUZhUVNOSktFQThmY2FuQTE3MGgzemRiYUdoeVV3bmxDUDNGeWdCSmlob3p0dTdyeEFqWFlHaXVLZU5lNG9BOE5PVUZhcnA4UmJRNEl0Z2oycWFvU05uY25vUDNiTjRkODQ1UEttOTdiZ0pyazlIMnhIcFFncVZobXRFdzVhQjBCRE5aNjVTN1BWZDdqTWclM0QlM0Q; _ga=GA1.3.584149080.1666291313; _chartbeat2=.1666291313283.1690411637301.0000100000000001.CevxcV20u1DDDg9E-3ZRz0Cjp8I5.2; FCNEC=%5B%5B%22AKsRol9mnqpol2qytzFXQR4-HPl-wBkW5XJPlnUT8o1FwpGTNzMMuHTjdoIrw62vvdadhhzG5doJWJZN5YZFGn75SsT-HtMHaYx5F1Z9dH1KMqG5HM25Vf4QHgLOgGL2iahEaGUsLT_aVOPlMWS8Slttq23_z0dtug%3D%3D%22%5D%2Cnull%2C%5B%5B5%2C%22762%22%5D%5D%5D; __gads=ID=91d9e74560346bbf:T=1666291313:RT=1690411695:S=ALNI_MY2NVMzeAdYI0YVnu5VbVFsWqvKvg; __gpi=UID=00000986060da399:T=1666291313:RT=1690411695:S=ALNI_MbEAgxjQMAYp-hUm_THm50Mn6OikQ; _ga_BS4Q6LCGB1=GS1.1.1690411374.9.1.1690411696.59.0.0; __tbc=%7Bkpex%7D7LqbQz_kKgGwRsKIaHW2YSE4aPBsfrbF9uNv3xEbAGtd6BuAasGqVTonMHIxP8zr; xbc=%7Bkpex%7Dx2xmlGVXcEY7i4Bm7n1PY6093kktn1LzlF6uGyi7Qq8C4_WNTHy6gl-GaICqOfrW2QNbwp66gg1z1hdBi_hUoSimV02c-1_16rkugz7CBIold0YSxXNglIF4pEvKVl_djrmaThSp37lLxWSwAAIFkqVZm0BA9F_Q734lg6fPTU-YZi9y1H33_PO4Bsql7J2NT_GcFJHiiJo8U1T5f-dMwK85xCY1-nER93ZyxAQsmCe11cjaXNYRCliK_x4PyKePDfuxdhpAxhIJCx6bvBEEAny2K3jlRPSvPdJ6stRZfMkiESXmP-9dsfUMHLTqSY8ariTQrWkAJbWJ-Ww0HrF-a_jEJUYW1KXmC89iKpkUIC6vWIYj8Tb0gykaJsUn39repSQRiA-RcI0tM3vfhnVS11V7LSlpqPnrYvQixZY-8Ow7R6kMJNLNQyEKQkZJLpLOu_C_lFZabZXgXjeD1ZNdfIoJhxa8WWfiBVqXgd0S5VReqDX3Sd439nOmfYmcB98sy_Rn9v_Jbokka6_0IB10yMCE8bPrqJ_Uw4hsxswg7Kl6Y7RSbzuFk7TINEPrI0WVIBQFFull-FLt3XMVi4k5y-ksk0tlrwQEganKDa6Jsk34RXFHIGrSAcWTaYQLKUThxAQ--GP89UyHTcIR1pupcDiiYQLup1z0lxoYlM6cltjZpeiBeJK_MD2nrwdmZBQsvrqbtJV3VXSdPZQ80MZE_6H9tFo_I0W-grYQtuBsdnGbRZUAmuIN4-1qXUIn5Fq-PoElOVWlyM6w320kuwUfuvomlcYzjlD3bKM8YvhTkVjpMp_hBTDx8j5SwCoiWpjyXqV1ZP9UZemhScBn1DstE4ZDDTV8j131OKS8siNgG776GxryMNX1nVQ56gMYMyk3yhAxnqsGZW6eySY08UdaovwA5pM4Umc7Qly_W_aVet8cQU-49mhvCTv0CLBIaGgGzoQsNB-hGNZcYLBQkVHTyeGnTzIZmzu6qKOUkLTW5rjDXopeVsqmmUUEGozXWD-K9St_jkglxIwRa8jBPo7gDaH9kt_YgiKdcmzaFIARwqSdK2adTLxZFXlsv_k6bMGN; folha_ga_userType=not_logged; folha_ga_loginType=folha; folha_ga_userGroup=none; folha_ga_swgt=none',
    'dnt': '1',
    'referer': 'https://www1.folha.uol.com.br/maispopulares/',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    }

    params = {
    'qs': '20231082054',
    }

    response = requests.get(
    'https://www1.folha.uol.com.br/virtual/spiffy/mais-lidas/home-1.0.0.json',
    params=params,
    cookies=cookies,
    headers=headers,
    )

    mais_lidas_f = response.json()
    manchetes_folha = []
    for item in mais_lidas_f[0:10]:
        titulo = (item['title'])
        link = (item['url'])
        manchetes_folha.append(f"{titulo}\n{link}")
        manchetes_folha = [line.replace("&apos;", "'") for line in manchetes_folha]
    return "\n\n".join(manchetes_folha)


### UOL ###

def raspador_uol():
    result = requests.get('https://www.uol.com.br/')
    soup_uol = bs4.BeautifulSoup(result.text, 'html.parser')
    raspagem_uol = soup_uol.find_all('li', {'class': 'mostRead__item'})
    manchetes_uol = []

    for li in raspagem_uol:
        azinho = li.find('a')
        link = azinho.get('href')
        titulo = azinho.get('title')
        manchetes_uol.append(f"{titulo}\n{link}")
    return "\n\n".join(manchetes_uol)


### BBC ###

def raspador_bbc():
    bbc = requests.get('https://www.bbc.com/portuguese/popular/read')
    soup_bbc = bs4.BeautifulSoup(bbc.text, 'html.parser')
    raspagem_bbc = soup_bbc.find_all('div', {'class': 'bbc-14zb6im'})
    manchetes_bbc = []

    for conteudo in raspagem_bbc:
        titulo = conteudo.text
        link = conteudo.find('a').get('href')
        manchetes_bbc.append(f"{titulo}\n{link}")
    return "\n\n".join(manchetes_bbc)


### VALOR ###

def raspador_valor():
    valor = requests.get('https://valor.globo.com/')
    soup_valor = bs4.BeautifulSoup(valor.text, 'html.parser')
    raspagem_valor = soup_valor.find_all('ol', {'class': 'card__highlight__list theme-color-primary-ordered-list'})
    conteudo_valor = raspagem_valor[0].find_all('h2')
    manchetes_valor = []

    for conteudo in conteudo_valor:
        titulo = conteudo.find('a').get('title')
        link = conteudo.find('a').get('href')
        manchetes_valor.append(f"{titulo}\n{link}")
    return "\n\n".join(manchetes_valor)


### VEJA ###

def raspador_veja():
    veja = requests.get('https://veja.abril.com.br/')
    soup_veja = bs4.BeautifulSoup(veja.text, 'html.parser')
    raspagem_veja = soup_veja.find_all('section', {'class': 'block most-read dark'})
    conteudo_veja = raspagem_veja[0].find_all('div', {'class': 'our-carousel-item'})
    manchetes_veja = []

    for conteudo in conteudo_veja:
        titulo = conteudo.find('h2').text
        link = conteudo.find('a').get('href')
        manchetes_veja.append(f"{titulo}\n{link}")
    return "\n\n".join(manchetes_veja)

### HORÁRIO ###

def horario_raspagem():
    agora = datetime.datetime.now()
    timezone_br = pytz.timezone('America/Sao_Paulo')
    horario_br = agora.astimezone(timezone_br)
    hora = horario_br.strftime("%d/%m/%Y, às %H:%M:%S, no horário de Brasília")
    return hora