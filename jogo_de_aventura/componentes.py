from time import sleep

# FLAG: componentes de estrutura de história

def introducao():
    sleep(3)
    print('Olá, esse é o Adventure Game!\nUm jogo criado para ser como uma hitória em que suas escolhas vão te levar até em diversas aventuras e finais diferentes.')
    sleep(3)
    print('explore a história e veja os mais diversos finais se surpreendendo com suas diferenças e revelações.\nNão desista e divirta-se! bom jogo!')

def final_incompleto(nome_player):
    sleep(4)
    print('Você morreu.')
    sleep(3)
    print(f'Não desânime herói {nome_player}! continue tentando e tenho certeza que chegara a um final glorioso, surpresas te aguardam e muitas aventuras precisam ser vividas.')
    sleep(2)
    print('Continue sua jornada gloriosa!!!')
    sleep(3)
    print('Vejo você logo!')

def final_conclusao(nome_player):
    print(f'Parabéns herói {nome_player}! Você finalizou o jogo, chegando em um dos finais da história, você passou por inúmeros desafios e ganhou muita experiência e só precisou de N.horas.\n')
    print('Você tomou N.decisões até chegar aqui.')

def final_encerramento():
    print('Uma realização de Paulo Vieira\nEm parceria com Silmara Silva\n Com o apoio, ensino e paciência de Matheus Bortoletto.')
    print('Agradecimentos especiais a: ... ')

if __name__ == '__main__':
    pass