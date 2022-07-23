import random
from time import sleep


def luta_troll():
    golpes = ['3', '5', '7']
    ponto_critico = '7'

    sleep(2)
    print('Um troll de diamante selvagem apareceu! e você precisa atacar!')
    sleep(3)
    escolha = input('Quantos golpes você vai dar?\nOpções: '+','.join(golpes))

    if escolha == '3':
        print('Não foi o bastante pra derrotar o troll de diamante selvagem.')
    elif escolha == '5':
        print('Faltou tão pouco pra derrotar ele.')
    elif escolha == ponto_critico:
        print('Você acertou no ponto fraco da armadura de cristais e finalmente derrotou ele.'
              '\nParabéns jovem espachim! você se saiu vitorioso!')
    else:
        print('Essa não é uma opção, jovem guerreiro.')


def confronto_medusa():
    corpo_medusa = ['Cabeça', 'Pescoço', 'Torso', 'Barriga', 'Braços', 'Pernas']
    golpe_final = 'Pescoço'

    sleep(2)
    print('Você só tem uma única chance de matar a Medusa, '
          'acertando seu ponto fraco, escolha com sabedoria aonde vai atacar.')
    sleep(3)
    ataque = input('Só poderá atacar nesses lugares, escolha um e digite para atacar: '+','.join(corpo_medusa))

    if ataque == 'Cabeça':
        print('A cabeça da Medusa está cheia de cobras que defendem seu ataque, '
              'te picam e o veneno te transforma em pedra.')
    elif ataque == 'Torso':
        print('O torso dela é duro demais, sua espada não consegue atravessar.')
    elif ataque == 'Barriga':
        print('Sua barriga é coberta de escamas, mas você morrerá como um valente guerreiro.')
    elif ataque == 'Braços':
        print('Seus braços podem se regenerar em instantes.')
    elif ataque == 'Pernas':
        print('Suas pernas decepatadas viram uma longa calda de cobra')
    elif ataque == golpe_final:
        print('Você venceu, ímbátivel guerreiro e ganhou o título de matador de maldiçôes.\n'
              'Acertou seu ponto fraco e com seu pescoço cortado você ainda '
              'pode transformas sua cabeça em um escudo.\n')
    else:
        print('Essa não uma opção, jovem espachim.')


def azetris():
    golpe_fatal = 10
    ataques_eu_aguento = 3

    while ataques_eu_aguento != 0:
        tentativa = int(
            input('Quantos golpes você acha necessário para derrotar o monstro azetris:\n~~Digite o número~~\n')
        )
        golpes = range(1, tentativa)

        for golpe in golpes:
            sleep(0.5)
            print(f'Você deu o {golpe} golpe!')

        if tentativa < golpe_fatal:
            print('Você não o matou, e o Azetris deu um golpe em você!')
            ataques_eu_aguento = ataques_eu_aguento - 1
            if ataques_eu_aguento == 0:
                print('Você não aguenta mais e morre!!!')
        else:
            print('Parabéns você conseguiu derrotar o Azetris!!!!')
            break


def confronto_hydra():
    ataque = ['Pela esquerda', 'Pela direita', 'Pelo meio', 'Por cima', 'Por baixo']
    print(' Suas opções são: {}' .format(ataque))
    dano = 0

    while dano < 5:
        desvio = input(' De onde você acha que está vindo o ataque? \n')
        direcao = random.choice(ataque)

        if desvio == direcao:
            print(' A Hydra atacou {}'.format(direcao))
            print(' E você conseguiu escapar!!!')
            print(' Parabéns!')
            dano += 6

        elif desvio != direcao and desvio in ataque:
            print(' Infelizmente o ataque não veio {}'.format(desvio))
            print(' Mas você ainda consegue aguentar mais golpes')
            dano += 1

        else:
            print(' Essa não é uma opção válida!')

    if dano > 5:
        print(' Parabéns!')

    else:
        print(' Você morreu')


def ultima_luta():
    protagonista = 100
    antagonista = 100
    golpe_espada = -5
    golpe_machado = -15
    soco = -5
    chute = -10
    cabecada = -3
    print(protagonista, antagonista, golpe_machado, golpe_espada, soco, cabecada, chute)
    # if, while ou for?


if __name__ == '__main__':
    print(confronto_hydra())
