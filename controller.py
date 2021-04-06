from model import BuscaAPI
from view import View


class CtrlAPI:
    def __init__(self):
        self.model = BuscaAPI(artista=None, musica=None)
        self.view = View()
        self.opcao = ''
        self.rank = ''
        self.limit = ''
        self.periodo = ''
        self.escopo = ''

    def escolha_usuario(self):
        opcao = self.view.introducao()
        self.opcao = opcao
        if opcao == '1':
            return self.escolha_letra()
        if opcao == '2':
            return self.escolha_traducao()
        if opcao == '3':
            return self.escolha_rank()

    def escolha_letra(self):
        nome_artista, nome_musica = self.view.intro_letra('letras')
        self.model.artista, self.model.musica = nome_artista, nome_musica
        letra = self.model.letra_musica()
        print(letra)

    def escolha_traducao(self):
        nome_artista, nome_musica = self.view.intro_letra('traduções')
        self.model.artista, self.model.musica = nome_artista, nome_musica
        letra = self.model.traducao_musica()
        print(letra)

    def escolha_rank(self):
        tipo_rank, limite = self.view.intro_rank()
        self.rank = tipo_rank
        self.limit = limite
        if self.rank == '1':
            return self.retornar_rank_artista()
        if self.rank == '2':
            return self.retornar_rank_musica()
        if self.rank == '3':
            return self.retornar_rank_album()

    def condicoes_artistas_album(self):
        intervalo = self.view.parametros_rank_artista_ou_musica()
        scope = self.view.escopo_artista_album()
        if self.rank == '1':
            self.rank = 'art'
        elif self.rank == '2':
            self.rank = 'mus'
        elif self.rank == '3':
            self.rank = 'alb'
        if intervalo == '1':
            self.periodo = 'day'
        elif intervalo == '2':
            self.periodo = 'week'
        elif intervalo == '3':
            self.periodo = 'month'
        if scope == '1':
            self.escopo = 'all'
        elif scope == '2':
            self.escopo = 'national'
        elif scope == '3':
            self.escopo = 'international'

    def condicoes_musica(self):
        intervalo = self.view.parametros_rank_artista_ou_musica()
        scope = self.view.escopo_musica()
        if self.rank == '1':
            self.rank = 'art'
        elif self.rank == '2':
            self.rank = 'mus'
        elif self.rank == '3':
            self.rank = 'alb'
        if intervalo == '1':
            self.periodo = 'day'
        elif intervalo == '2':
            self.periodo = 'week'
        elif intervalo == '3':
            self.periodo = 'month'

    def condicoes_album(self):
        intervalo = self.view.periodo_album()
        scope = self.view.escopo_artista_album()
        if self.rank == '1':
            self.rank = 'art'
        elif self.rank == '2':
            self.rank = 'mus'
        elif self.rank == '3':
            self.rank = 'alb'
        if intervalo == '1':
            self.periodo = 'week'
        elif intervalo == '2':
            self.periodo = 'month'

    def retornar_rank_artista(self):
        self.condicoes_artistas_album()
        rank = self.model.rank_geral(tipo_de_rank=self.rank,
                                     periodo=self.periodo, escopo=self.escopo,
                                     limite=self.limit)
        print(rank)

    def retornar_rank_musica(self):
        self.condicoes_musica()
        rank = self.model.rank_geral(tipo_de_rank=self.rank,
                                     periodo=self.periodo, escopo=self.escopo,
                                     limite=self.limit)
        print(rank)

    def retornar_rank_album(self):
        self.condicoes_album()
        rank = self.model.rank_geral(tipo_de_rank=self.rank,
                                     periodo=self.periodo, escopo=self.escopo,
                                     limite=self.limit)
        print(rank)






