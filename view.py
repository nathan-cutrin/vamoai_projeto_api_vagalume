class View:
    def introducao(self):
        print('Seja bem vindo a API do Vagalume!'
              '\nAqui você pode encontrar algumas informações do mundo da música!!!')
        return self.menu()

    def menu(self):
        print('Neste programa, você poderá procurar por:\n'
              '\n1 - Letras de músicas brasileiras e internacionais'
              '\n2 - Traduções de músicas internacionais'
              '\n3 - Acessar o top 100 de artistas, músicas ou albuns mais acessados '
              'do Vagalume'
              '\n4 - Verificar se seu artista, música ou álbum preferido está no '
              'top 100 de mais acessados'
              '\nVamos começar?\n')

        menu = str(input('Digite o número referente a opção desejada: '))
        return menu

    def intro_letra(self, parametro):
        print(f'Para procurar {parametro} de músicas, precisamos de algumas '
              'informações.')
        return self.parametros_letra()

    def parametros_letra(self):
        nome_do_artista = str(input('Por favor, digite o nome do artista: '))
        nome_da_musica = str(input('Por favor, digite o nome da música: '))
        return nome_do_artista, nome_da_musica

    def intro_rank(self):
        print('Para acessar o top 100 do Vagalume, precisamos de algumas '
              'informações.')
        return self.parametros_gerais_rank()

    def parametros_gerais_rank(self):
        tipo_de_rank = str(input('\nOpções:'
                                 '\n[1] para rank de artistas '
                                 '\n[2] para rank de músicas'
                                 '\n[3] para rank de álbuns'
                                 '\nDigite a opção escolhida: '))

        limite = str(input('\nDigite um número de tamanho máximo '
                           'do ranking Vagalume.'
                           '\nEx: Se eu quero um top 50, '
                           'devo digitar: 50'
                           '\nDigite sua escolha: '))
        return tipo_de_rank, limite

    def parametros_rank_artista_ou_musica(self):
        valor = str(input('\nOpções: '
                          '\n[1] para ranking diário'
                          '\n[2] para ranking semanal'
                          '\n[3] para ranking mensal'
                          '\nDigite sua escolha: '))
        return valor

    def escopo_artista_album(self):
        print('Para este ranking, você pode escolher as '
              'seguintes opções.')
        escopo = str(input('\nOpções:'
                           '\n[1] para ranking geral, '
                           'incluindo nacionais '
                           'e internacionais'
                           '\n[2] para somente nacionais'
                           '\n[3] para somente internacionais'
                           '\nDigite sua escolha: '))
        return escopo

    def escopo_musica(self):
        musica = str(input('\nOpções:'
                           '\n[1] para ranking geral '
                           'de músicas, incluindo todas as músicas '
                           'no Vagalume.'
                           '\n[2] para ranking geral '
                           'de letras de músicas'
                           '\n[3] para traduções de músicas'
                           '\n[4] para cifras de músicas'
                           '\nDigite sua escolha: '))
        return musica

    def periodo_album(self):
        valor = str(input('\nOpções: '
                          '\n[1] para ranking semanal'
                          '\n[2] para ranking mensal'
                          '\nDigite sua escolha: '))
        return valor





