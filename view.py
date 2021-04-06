class View:
    def introducao(self):
        print('Seja bem vindo a API do Vagalume!'
              '\nAqui você pode encontrar algumas informações do mundo da música!!!')

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
        if menu == '1':
            print('Para procurar letras de músicas, precisamos de algumas '
                  'informações.')
            nome_do_artista = str(input('Por favor, digite o nome do artista: '))
            nome_da_musica = str(input('Por favor, digite o nome da música: '))
        elif menu == '2':
            print('Para procurar traduções de músicas, precisamos de algumas'
                  'informações.')
            nome_do_artista = str(input('Por favor, digite o nome do artista: '))
            nome_da_musica = str(input('Por favor, digite o nome da música: '))
        elif menu == '3':
            print('Para acessar o top 100 do Vagalume, precisamos de algumas '
                  'informações.')
            tipo_de_rank = str(input('\nDigite [1] para rank de artistas '
                                     '\nDigite [2] para rank de músicas'
                                     '\nDigite [3] para rank de álbuns'))

a = View()
a.menu()