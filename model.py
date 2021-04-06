import requests
import json

class BuscaAPI:
    def __init__(self, artista=None, musica=None):
        self.artista = artista
        self.musica = musica
        self.url = 'https://api.vagalume.com.br/'

    def letra_musica(self):
        """
        busca a letra no idioma original da musica dentro da API do vagalume
        """
        art = f'art={self.artista}'
        mus = f'mus={self.musica}'
        url = self.url + f'search.php?{art}&{mus}'
        info = requests.get(url=url)
        info_j = info.json()
        letra_musica = info_j['mus'][0]['text']
        return letra_musica

    def traducao_musica(self):
        """
        busca a tradução da música original dentro da API do vagalume
        """
        art = f'art={self.artista}'
        mus = f'mus={self.musica}'
        url = self.url + f'search.php?{art}&{mus}'
        info = requests.get(url=url)
        info_j = info.json()
        traducao_musica = info_j['mus'][0]['translate'][0]['text']
        return traducao_musica

    def rank_geral(self, tipo_de_rank, periodo, escopo, limite):
        """
        busca o ranking do Vagalume
        """
        url = self.url + f'rank.php?type={tipo_de_rank}&period={periodo}' \
                         f'&scope={escopo}&limit={limite}'
        info = requests.get(url=url)
        info_rank = info.json()
        rank = info_rank[tipo_de_rank][periodo]  # [escopo]
        return rank

    def procurar_artista_no_rank(self, tipo_de_rank, periodo, escopo, limite):
        if self.musica is None:
            print('Você não procurou por nenhum artista :(')
        else:
            """
                  busca o ranking do Vagalume
                  """
            url = self.url + f'rank.php?type={tipo_de_rank}&period={periodo}' \
                             f'&scope={escopo}&limit={limite}'
            info = requests.get(url=url)
            info_rank = info.json()
            rank = info_rank[tipo_de_rank][periodo]  # [escopo]
            #print(rank)
            if self.artista in rank:
                print('Ele está')
            else:
                print('flopou')

    def procurar_musica_no_rank(self):
        if self.musica is None:
            print('Você não procurou por nenhuma música :(')


#a = BuscaAPI(artista='ariana grande', musica='thank u next',)
#print(a.rank_geral(periodo='week', limite=100, escopo='nacional', tipo_de_rank='art'))
#a.procurar_artista_no_rank(periodo='week', limite=100, escopo='nacional', tipo_de_rank='art')

