from time import sleep
# FLAG: componentes de estrutura de história


def introducao(tempo):
    sleep(tempo)
    print('Olá, esse é o Adventure Game!')
    sleep(tempo)
    print('Um jogo criado para ser como uma hitória em que suas escolhas '
          'vão te levar até em diversas aventuras e finais diferentes.')
    sleep(tempo)
    print('explore a história e veja os mais diversos finais se surpreendendo com suas diferenças e revelações.')
    sleep(tempo)
    print('Não desista e divirta-se! bom jogo!')


def continuara(nome_player, tempo):
    sleep(tempo)
    print(' Sua jornada ainda não acabou! teste as outras rotas e veja as outras possibilidades dessa história.')
    sleep(tempo)
    print(' Você tomou ótimas decicões até aqui!')
    sleep(tempo)
    print(' Você já é um grande héroi {}!!!'.format(nome_player))


def final_incompleto(nome_player, tempo):
    sleep(tempo)
    print('Você morreu.')
    sleep(tempo)
    print(f'Mas não desânime meu caro herói {nome_player}! '
          f'continue tentando e tenho certeza que chegará a um final glorioso!')
    sleep(tempo)
    print('Surpresas te aguardam e muitas aventuras precisam ser vividas, '
          'todas as histórias tem algo de único pra você!.')
    sleep(tempo)
    print('Continue sua jornada gloriosa!!!')
    sleep(tempo)
    print('Vejo você logo!')


def final_conclusao(nome_player, tempo):
    sleep(tempo)
    print(f'Parabéns herói {nome_player}! Você finalizou o jogo, chegando em um dos finais gloriosos da história,')
    sleep(tempo)
    print('você passou por inúmeros desafios e ganhou muita experiência e só precisou de N.horas.')
    sleep(tempo)
    print('Você tomou N.decisões até chegar aqui.')


def final_encerramento(tempo):
    sleep(tempo)
    print('Uma realização de Paulo Vinicius\n')
    print('Em parceria com Silmara Silva, uma colega extraordinaria')
    print('Com o apoio, ensino e paciência de Matheus Bortoletto, '
          'que tem toda minha gratidão e admiração, meu grande mestre.')
    print('Agradecimentos especiais a: \n')
    print('Minha familia e amigos')
    print('Minha mãe, por absolutamente tudo!')
    print('Danilo, meu grande amigo que sempre me apoiou.')
    print('Stephanie, por todo amor e nunca me deixar desistir.')
    print('um agradecimento a namorada do Matheus, por ceder ele e ser legal.')


if __name__ == '__main__':
    pass
