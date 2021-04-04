class BuscaAPI:
    import requests

    def __init__(self, artista = None, musica= None):
        self.artista = artista
        self.musica = musica

    def procura(self):
        '''
        a funçao procura é usada para retornar a url da api para buscar artista e musica
        '''
        #formatar entrada de parametros para nao dar bug, noa pode ter espaços
        #obs: aceita trecho do nome
        art= f'art={self.artista}'
        mus = f'mus={self.musica}'
        url = f'https://api.vagalume.com.br/search.php?{art}&{mus}' 
        return url

    def letra_musica(self):
        '''
        busca a letra no idioma original da musica dentro da API do vagalume
        
        '''
        info = self.requests.get(self.procura())
        info_j = info.json()
        letra_musica = info_j['mus'][0]['text']
        return letra_musica



