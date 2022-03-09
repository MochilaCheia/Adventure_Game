from time import sleep

# FLAG: componentes de estrutura de história

def nome_jogador():
    sleep(0.5)
    nome_player = input('\nMas antes de começarmos, me diga seu nome jovem héroi: ')
    sleep(1)
    print(f'Seja bem vindo, {nome_player}! e boa aventura!\n')

def introducao():
    sleep(3)
    print('Olá, esse é o Adventure Game!\nUm jogo criado para ser como uma hitória em que suas escolhas vão te levar até em diversas aventuras e finais diferentes.')
    sleep(3)
    print('explore a história e veja os mais diversos finais se surpreendendo com suas diferenças e revelações.\nNão desista e divirta-se! bom jogo!')

def final_incompleto():
    sleep(4)
    print('Você morreu.')
    sleep(3)
    print('Não desânime caro herói, continue tentando e tenho certeza que chegara a um final glorioso, surpresas te aguardam!')
    sleep(3)
    print('Vejo você logo!')

def final_conclusao():
    print('Parabéns, herói! Você finalizou o jogo, chegando em um dos finais da história, você passou por inúmeros desafios e ganhei muita experiência e só precisou de N.horas.\n')
    print('Você tomou N.decisões até chegar aqui.')

def final_encerramento():
    print('Uma realização de Paulo Vieira\nEm parceria com Silmara\n Com o apoio, ensino e paciência de Matheus')
    print('Agradecimentos especiais a: ... ')

# FLAG: componentes do inventario

def inventario():
    inventario_inicial = ['Vazio']
    print(inventario_inicial)

if __name__ == '__main__':
    pass