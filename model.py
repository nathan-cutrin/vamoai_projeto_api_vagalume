import requests


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
        if info.status_code != 200:
            raise Exception(f"ERRO [{info.status_code}]\nREQUEST [{url}]")
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
        if info.status_code != 200:
            raise Exception(f"ERRO [{info.status_code}]\nREQUEST [{url}]")
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
        if info.status_code != 200:
            raise Exception(f"ERRO [{info.status_code}]\nREQUEST [{url}]")
        info_rank = info.json()
        rank = info_rank[tipo_de_rank][periodo]  # [escopo]
        return rank



