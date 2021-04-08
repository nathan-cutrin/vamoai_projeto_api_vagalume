from model import BuscaAPI
from view import View
import json
import pandas as pd


class CtrlAPI:
    def __init__(self):
        self.model = BuscaAPI(artista=None, musica=None)
        self.view = View()
        self.opcao = None
        self.rank = None
        self.limit = None
        self.periodo = None
        self.escopo = None
        self.formato = None

    def escolha_usuario(self):
        opcao = self.view.introducao()
        self.opcao = opcao
        if opcao == '1':
            return self.retorna_letra()
        if opcao == '2':
            return self.retorna_traducao()
        if opcao == '3':
            return self.escolha_rank()

    def escolha_usuario_final(self):
        opcao = self.view.mensagem()
        if opcao == '1':
            return self.retorna_letra()
        if opcao == '2':
            return self.retorna_traducao()
        if opcao == '3':
            return self.escolha_rank()

    def definir_formato(self):
        if self.formato == '1':
            self.formato = 'json'
        elif self.formato == '2':
            self.formato = 'csv'
        elif self.formato == '3':
            self.formato = 'formatado'

    def retornar_formato(self, request):
        resultado = ''
        if self.formato == 'json':
            resultado = json.dumps(request, indent=2)
        elif self.formato == 'csv':
            resultado = pd.DataFrame.from_dict(data=request, orient='index')
            resultado.reset_index(inplace=True)
            resultado.to_csv(header=False)
        return resultado

    def retornar_status_request(self):
        if self.model.resultado_request == 200:
            print('Requisição bem sucedida.')
        elif self.model.resultado_request == 400:
            print('Requisição mal sucedida.')
        elif self.model.resultado_request == 401:
            print('Requisição não autorizada.')
        elif self.model.resultado_request == 404:
            print('Requisição não encontrada :(')
        print(self.model.resultado_request)

    def retorna_letra(self):
        nome_artista, nome_musica = self.view.intro_letra('letras')
        self.model.artista, self.model.musica = nome_artista, nome_musica
        self.formato = self.view.escolha_formato()
        self.definir_formato()
        letra = self.model.letra_musica()
        self.retornar_status_request()
        if self.formato != 'formatado':
            letra_formatada = self.retornar_formato(letra)
            print(letra_formatada)
        else:
            letra_completa = letra['mus'][0]['text']
            print(letra_completa)
        self.escolha_usuario_final()

    def retorna_traducao(self):
        nome_artista, nome_musica = self.view.intro_letra('traduções')
        self.model.artista, self.model.musica = nome_artista, nome_musica
        self.formato = self.view.escolha_formato()
        self.definir_formato()
        traducao = self.model.traducao_musica()
        if self.formato != 'formatado':
            traducao_formatada = self.retornar_formato(traducao)
            print(traducao_formatada)
        else:
            traducao_completa = traducao['mus'][0]['translate'][0]['text']
            print(traducao_completa)
        self.escolha_usuario_final()

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
            self.escopo = 'nacional'
        elif scope == '3':
            self.escopo = 'internacional'

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
        if scope == '1':
            self.escopo = 'all'
        elif scope == '2':
            self.escopo = 'nacional'
        elif scope == '3':
            self.escopo = 'internacional'

    def retornar_rank_artista(self):
        self.condicoes_artistas_album()
        self.formato = self.view.escolha_formato()
        self.definir_formato()
        rank = self.model.rank_geral(tipo_de_rank=self.rank,
                                     periodo=self.periodo, escopo=self.escopo,
                                     limite=self.limit)
        if self.formato != 'formatado':
            rank_formatado = self.retornar_formato(rank)
            print(rank_formatado)
        else:
            rank_formatado = rank[self.rank][self.periodo][self.escopo]
            print(rank)
            print(rank_formatado)
            for elemento in rank_formatado:
                print(f'Nome:{elemento["name"]} -'
                      f'Visualizações únicas: {rank_formatado["uniques"]} -'
                      f'Visualizações totais: {rank_formatado["views"]}')
        self.escolha_usuario_final()

    def retornar_rank_musica(self):
        self.condicoes_musica()
        self.formato = self.view.escolha_formato()
        self.definir_formato()
        rank = self.model.rank_geral(tipo_de_rank=self.rank,
                                     periodo=self.periodo, escopo=self.escopo,
                                     limite=self.limit)
        rank_formatado = self.retornar_formato(rank)
        print(rank_formatado)
        self.escolha_usuario_final()

    def retornar_rank_album(self):
        self.condicoes_album()
        self.formato = self.view.escolha_formato()
        self.definir_formato()
        rank = self.model.rank_geral(tipo_de_rank=self.rank,
                                     periodo=self.periodo, escopo=self.escopo,
                                     limite=self.limit)
        rank_formatado = self.retornar_formato(rank)
        print(rank_formatado)
        self.escolha_usuario_final()






