import requests


class BuscaAPI:
    def __init__(self, artista=None, musica=None):
        self.artista = artista
        self.musica = musica
        self.url = 'https://api.vagalume.com.br/'
        self.resultado_request = None

    def letra_musica(self):
        """
        busca a letra no idioma original da musica dentro da API do vagalume
        """
        art = f'art={self.artista}'
        mus = f'mus={self.musica}'
        url = self.url + f'search.php?{art}&{mus}'
        info = requests.get(url=url)
        self.resultado_request = info.status_code
        info_j = info.json()
        return info_j

    def traducao_musica(self):
        """
        busca a tradução da música original dentro da API do vagalume
        """
        art = f'art={self.artista}'
        mus = f'mus={self.musica}'
        url = self.url + f'search.php?{art}&{mus}'
        info = requests.get(url=url)
        self.resultado_request = info.status_code
        info_j = info.json()
        return info_j

    def rank_geral(self, tipo_de_rank, periodo, escopo, limite):
        """
        busca o ranking do Vagalume
        """
        url = self.url + f'rank.php?type={tipo_de_rank}&period={periodo}' \
                         f'&scope={escopo}&limit={limite}'
        info = requests.get(url=url)
        self.resultado_request = info.status_code
        info_rank = info.json()
        return info_rank

    def request_erro_404(self):
        url = 'https://www.vagalume.com.br/u2/discografia/index.js'
        info = requests.get(url=url)
        self.resultado_request = info.status_code
        print(f'\nVamos lá...'
              f'\nAcho que vou pesquisar sobre a discografia do U2!'
              f'\nProcurando pela URL {url}...'
              f'\nNão encontrei nada :(')
        return f'               --Erro: {self.resultado_request}, ' \
               f'requisição não encontrada.--'








