from time import sleep

# FLAG: componentes de estrutura de história

def introducao():
    sleep(1)
    print('Olá, esse é o Adventure Game!')
    sleep(2)
    print('Um jogo criado para ser como uma hitória em que suas escolhas vão te levar até em diversas aventuras e finais diferentes.')
    sleep(2)
    print('explore a história e veja os mais diversos finais se surpreendendo com suas diferenças e revelações.')
    sleep(1)
    print('Não desista e divirta-se! bom jogo!')

def final_incompleto(nome_player):
    sleep(3)
    print('Você morreu.')
    sleep(2)
    print(f'Não desânime herói {nome_player}! continue tentando e tenho certeza que chegara a um final glorioso!') \
    sleep(1)
    print('Surpresas te aguardam e muitas aventuras precisam ser vividas.')
    sleep(2)
    print('Continue sua jornada gloriosa!!!')
    sleep(2)
    print('Vejo você logo!')

def final_conclusao(nome_player):
    sleep(2)
    print(f'Parabéns herói {nome_player}! Você finalizou o jogo, chegando em um dos finais da história,')
    sleep(2)
    print('você passou por inúmeros desafios e ganhou muita experiência e só precisou de N.horas.')
    sleep(1)
    print('Você tomou N.decisões até chegar aqui.')

def final_encerramento():
    sleep(1)
    print('Uma realização de Paulo Vieira\nEm parceria com Silmara Silva\n Com o apoio, ensino e paciência de Matheus Bortoletto.')
    print('Agradecimentos especiais a: ... ')

if __name__ == '__main__':
    pass