class BuscaAPI:
    import requests

    def __init__(self, artista=None, musica=None, tipo_de_rank=None):
        self.artista = artista
        self.musica = musica
        self.tipo_de_rank = tipo_de_rank

    def procura(self):
        """
        a funçao procura é usada para retornar a url da api para buscar artista e musica
        """
        # formatar entrada de parametros para nao dar bug, noa pode ter espaços
        # obs: aceita trecho do nome
        art = f'art={self.artista}'
        mus = f'mus={self.musica}'
        tipo_de_rank = f'type={self.tipo_de_rank}'
        url_base = f'https://api.vagalume.com.br/'
        if self.artista is None and self.musica is None:
            url = f'https://api.vagalume.com.br/rank.php?{tipo_de_rank}'
        else:
            url = f'{url_base}search.php?{art}&{mus}'
        return url

    def letra_musica(self):
        """
        busca a letra no idioma original da musica dentro da API do vagalume
        """
        info = self.requests.get(self.procura())
        info_j = info.json()
        letra_musica = info_j['mus'][0]['text']
        return letra_musica

    def traducao_musica(self):
        """
        busca a tradução da música original dentro da API do vagalume
        """
        info = self.requests.get(url=self.procura())
        info_j = info.json()
        traducao_musica = info_j['mus'][0]['translate'][0]['text']
        return traducao_musica

    def rank_geral(self):
        """
        busca a posição dos artistas no ranking do Vagalume
        """
        info = self.requests.get(url=self.procura())
        info_rank = info.json()
        rank = info_rank['art']['month']['all']
        return rank



