import requests

# Bloco de endpoints e token
token = '3bdfe52c5b254680abe6c4a9c93ec3df'
url = f'https://api.vagalume.com.br/search.php?apikey={token}'
url_artista = f'https://www.vagalume.com.br/'
url_rank_art = f'https://api.vagalume.com.br/rankArtist.php?apikey={token}'
url_rank_geral = f'https://api.vagalume.com.br/rank.php?'


# Bloco informações do artista
artista = 'iza'  # str(input('Digite o nome do artista: ')).lower()
url_artista_final = f'{url_artista}{artista}/index.js?{token}'  # em nomes conjuntos tem que ter um traço

# Bloco informações do artista + rank artistas
response = requests.get(url=url_artista_final)
artistas_info = response.json()
artista_id = artistas_info['artist']['id']
response_rank = requests.get(url=url_rank_art, params={'period': 'monthly', 'artID': artista_id})

# Bloco de informações do rank geral
response_rank_geral = requests.get(url=url_rank_geral, params={'type': 'art', 'apikey': token})
variavel = response_rank_geral.json()
variavel2 = variavel['art']['month']['all']

print(variavel)

for elemento in variavel2:
    print(f"Nome: {elemento['name']}, visualizações únicas: {elemento['uniques']}, "
          f"total de visualizações: {elemento['views']}\n")



