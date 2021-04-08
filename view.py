class View:
    def introducao(self):
        '''
        teste merge 2
        '''
        
        print('Seja bem vindo a API do Vagalume!'
              '\nAqui você pode encontrar algumas informações do mundo d'
              'a música!!!')
        return self.menu()

    def menu(self):
        """
        * menu = None
        while menu not in ['1', '2', '3']:
            menu = input('Digite o número referente a opção desejada: ')
        """
        print('Neste programa, você poderá procurar por:\n'
              '\n1 - Letras de músicas brasileiras e internacionais'
              '\n2 - Traduções de músicas internacionais'
              '\n3 - Acessar o top 100 de artistas, músicas ou albuns '
              'mais acessados do Vagalume'
              '\nVamos começar?\n')
        menu = ''

        while int(menu) not in range(4):
            menu = str(input('Digite o número referente a opção desejada: '))
        return menu

    def intro_letra(self, parametro):
        print(f'\nPara procurar {parametro} de músicas, precisamos de algumas '
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
        tipo_de_rank = ''
        limite = ''
        while int(menu) not in range(4):
            tipo_de_rank = str(input('\nOpções:'
                                     '\n[1] para rank de artistas '
                                     '\n[2] para rank de músicas'
                                     '\n[3] para rank de álbuns'
                                     '\nDigite a opção escolhida: '))

        while int(menu) not in range(4):
            limite = str(input('\nDigite um número de tamanho máximo '
                               'do ranking Vagalume.'
                               '\nEx: Se eu quero um top 50, '
                               'devo digitar: 50'
                               '\nDigite sua escolha: '))
        return tipo_de_rank, limite

    def parametros_rank_artista_ou_musica(self):
        valor = ''


        while int(menu) not in range(4):

            valor = str(input('\nOpções: '
                              '\n[1] para ranking diário'
                              '\n[2] para ranking semanal'
                              '\n[3] para ranking mensal'
                              '\nDigite sua escolha: '))
        return valor

    def escopo_artista_album(self):
        print('Para este ranking, você pode escolher as '
              'seguintes opções.')
        escopo = ''
        while int(menu) not in range(4):
            escopo = str(input('\nOpções:'
                               '\n[1] para ranking geral, '
                               'incluindo nacionais '
                               'e internacionais'
                               '\n[2] para somente nacionais'
                               '\n[3] para somente internacionais'
                               '\nDigite sua escolha: '))
        return escopo

    def escopo_musica(self):
        musica = ''
        while int(menu) not in range(4):
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
        valor = ''
        while int(menu) not in range(4):
            valor = str(input('\nOpções: '
                              '\n[1] para ranking semanal'
                              '\n[2] para ranking mensal'
                              '\nDigite sua escolha: '))
        return valor

    def mensagem(self):
        continuar = ''
        while continuar != 'S' and continuar != 'N':
            continuar = str(input('\nDeseja continuar? [S/N]: ')).upper()
        if continuar == 'N':
            print('Obrigado por utilizar nosso programa :D!')
        elif continuar == 'S':
            return self.menu()

    def escolha_json_csv(self):
        escolha = ''
        while int(menu) not in range(4):
            escolha = str(input('\nVocê deseja retornar o resultado em'
                                'formato JSON, CSV ou formatado para '
                                'melhor visualização?'
                                '\nAo optar pelo formato JSON ou CSV, '
                                'o programa trará os dados completos que '
                                'a API disponibiliza para consultar.'
                                '\n[1] para JSON'
                                '\n[2] para CSV'
                                '\n[3] para formatado'
                                '\nDigite aqui sua escolha: '))
        return escolha

    def escolher_formato_novamente(self):
        escolha = None
        while escolha != 'S' and escolha != 'N':
            escolha = str(input('\nDeseja retornar em outro formato? [S/N]'))
        return escolha



