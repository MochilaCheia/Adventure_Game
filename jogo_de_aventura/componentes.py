from time import sleep

# FLAG: componentes de estrutura de história

def introducao(tempo):
    sleep(tempo)
    print('Olá, esse é o Adventure Game!')
    sleep(tempo)
    print('Um jogo criado para ser como uma hitória em que suas escolhas vão te levar até em diversas aventuras e finais diferentes.')
    sleep(tempo)
    print('explore a história e veja os mais diversos finais se surpreendendo com suas diferenças e revelações.')
    sleep(tempo)
    print('Não desista e divirta-se! bom jogo!')

def final_incompleto(nome_player,tempo):
    sleep(tempo)
    print('Você morreu.')
    sleep(tempo)
    print(f'Mas não desânime herói {nome_player}! continue tentando e tenho certeza que chegara a um final glorioso!')
    sleep(tempo)
    print('Surpresas te aguardam e muitas aventuras precisam ser vividas.')
    sleep(tempo)
    print('Continue sua jornada gloriosa!!!')
    sleep(tempo)
    print('Vejo você logo!')

def final_conclusao(nome_player,tempo):
    sleep(tempo)
    print(f'Parabéns herói {nome_player}! Você finalizou o jogo, chegando em um dos finais da história,')
    sleep(tempo)
    print('você passou por inúmeros desafios e ganhou muita experiência e só precisou de N.horas.')
    sleep(tempo)
    print('Você tomou N.decisões até chegar aqui.')

def final_encerramento(tempo):
    sleep(tempo)
    print('Uma realização de Paulo Vieira\nEm parceria com Silmara Silva\n Com o apoio, ensino e paciência de Matheus Bortoletto.')
    print('Agradecimentos especiais a: ... ')

if __name__ == '__main__':
    pass