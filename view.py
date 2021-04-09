class View:
    def introducao(self):
        print('Seja bem vindo a este software de requisição à API do Vagalume!'
              '\nAqui você pode encontrar algumas informações do mundo '
              'da música!!!')
        return self.menu()

    def menu(self):
        print('\nNeste programa, você poderá procurar por:\n'
              '\n1 - Letras de músicas brasileiras e internacionais'
              '\n2 - Traduções de músicas internacionais'
              '\n3 - Acessar o top 100 de artistas, músicas ou albuns '
              'mais acessados do Vagalume'
              '\n4 - Sair do programa'
              '\nVamos começar?\n')

        menu = None
        while menu not in ['1', '2', '3', '4']:
            menu = str(input('Digite o número referente a opção desejada: '))
        if menu != '4':
            return menu
        else:
            print('Obrigado por utilizar nosso programa :D!')


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
        tipo_de_rank = None
        limite = None
        while tipo_de_rank not in ['1', '2', '3']:
            tipo_de_rank = str(input('\nOpções:'
                                     '\n[1] para rank de artistas '
                                     '\n[2] para rank de músicas'
                                     '\n[3] para rank de álbuns'
                                     '\nDigite a opção escolhida: '))

        lista = list(range(1, 101))
        lista_2 = [str(num) for num in lista]
        while limite not in lista_2:
            limite = str(input('\nDigite um número de tamanho máximo '
                               'do ranking Vagalume.'
                               '\nEx: Se eu quero um top 50, '
                               'devo digitar: 50'
                               '\nDigite sua escolha: '))
        return tipo_de_rank, limite

    def parametros_rank_artista_ou_musica(self):
        valor = None
        while valor not in ['1', '2', '3']:
            valor = str(input('\nOpções: '
                              '\n[1] para ranking diário'
                              '\n[2] para ranking semanal'
                              '\n[3] para ranking mensal'
                              '\nDigite sua escolha: '))
        return valor

    def escopo_artista_album(self):
        print('Para este ranking, você pode escolher as '
              'seguintes opções.')
        escopo = None
        while escopo not in ['1', '2', '3']:
            escopo = str(input('\nOpções:'
                               '\n[1] para ranking geral, '
                               'incluindo nacionais '
                               'e internacionais'
                               '\n[2] para somente nacionais'
                               '\n[3] para somente internacionais'
                               '\nDigite sua escolha: '))
        return escopo

    def escopo_musica(self):
        musica = None
        while musica not in ['1', '2', '3', '4']:
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
        valor = None
        while valor not in ['1', '2']:
            valor = str(input('\nOpções: '
                              '\n[1] para ranking semanal'
                              '\n[2] para ranking mensal'
                              '\nDigite sua escolha: '))
        return valor

    def mensagem(self):
        continuar = None
        while continuar not in ['S', 'N']:
            continuar = str(input('\nVoltar ao menu? [S/N]: ')).upper()
        if continuar == 'N':
            print('Obrigado por utilizar nosso programa :D!')
        elif continuar == 'S':
            return self.menu()

    def escolha_formato(self):
        escolha = None
        while escolha not in ['1', '2', '3']:
            escolha = str(input('\nVocê deseja retornar o resultado em '
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

    def mostrando_codigo_404(self):
        escolha = None
        while escolha not in ['S', 'N']:
            escolha = str(input('\nAntes de terminarmos, '
                                'gostaria de ver o código HTTP 404?'
                                '\nEste erro ocorre quando a nossa '
                                'requisição não encontrou nenhum resultado.'
                                '\nDigite [S] para ver o erro e continuar'
                                'no programa ou [N] para sair do programa'
                                ': ')).upper()
        return escolha

