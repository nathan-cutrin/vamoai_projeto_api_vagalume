class View:
    def introducao(self):
        print('Seja bem vindo a API do Vagalume!'
              '\nAqui você pode encontrar algumas informações do mundo d'
              'a música!!!')
        return self.menu()

    def menu(self):
        print('Neste programa, você poderá procurar por:\n'
              '\n1 - Letras de músicas brasileiras e internacionais'
              '\n2 - Traduções de músicas internacionais'
              '\n3 - Acessar o top 100 de artistas, músicas ou albuns '
              'mais acessados do Vagalume'
              '\n4 - Verificar se seu artista, música ou álbum preferido está no '
              'top 100 de mais acessados'
              '\nVamos começar?\n')
        menu = ''
        while menu != '1' and menu != '2' and menu != '3' and menu != '3':
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
        while tipo_de_rank != '1' and tipo_de_rank != '2' and tipo_de_rank != '3':
            tipo_de_rank = str(input('\nOpções:'
                                     '\n[1] para rank de artistas '
                                     '\n[2] para rank de músicas'
                                     '\n[3] para rank de álbuns'
                                     '\nDigite a opção escolhida: '))

        while limite != '1' and limite != '2' and limite != '3':
            limite = str(input('\nDigite um número de tamanho máximo '
                               'do ranking Vagalume.'
                               '\nEx: Se eu quero um top 50, '
                               'devo digitar: 50'
                               '\nDigite sua escolha: '))
        return tipo_de_rank, limite

    def parametros_rank_artista_ou_musica(self):
        valor = ''
        while valor != != '1' and valor != '2' and valor != '3':
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
        while escopo != '1' and escopo != '2' and escopo != '3':
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
        while musica != '1' and musica != '2' and musica != '3':
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
        while valor != '1' and valor != '2' and valor != '3':
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
        while escolha != '1' and escolha != '2' and escolha != '3':
            escolha = str(input('\nVocê deseja retornar o resultado em'
                                'formato JSON, CSV ou formatado para '
                                'melhor visualização?'))
        return escolha




