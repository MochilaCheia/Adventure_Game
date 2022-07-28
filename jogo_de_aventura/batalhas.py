import random
from time import sleep


def luta_troll(tempo):
    golpes = ['3', '5', '7']
    ponto_critico = '7'

    sleep(tempo)
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

# Utilizado


def confronto_hydra(nome_player, tempo):
    sleep(tempo)
    print('A hydra então ataca e você precisa desviar!')
    ataque = ['Pela esquerda', 'Pela direita', 'Pelo meio', 'Por cima', 'Por baixo']
    print('Suas opções são: {}' .format(ataque))
    dano = 0

    while dano < 5:
        desvio = input('De onde você acha que está vindo o ataque? \n')
        direcao = random.choice(ataque)

        if desvio == direcao:
            print('A Hydra atacou {}'.format(direcao))
            print('E você conseguiu escapar!!!')
            print('Você se saiu vitorioso afinal, {}!'.format(nome_player))
            dano += 6

        elif desvio != direcao and desvio in ataque:
            print('O ataque dela não veio {}'.format(desvio))
            print('Mas você ainda consegue aguentar mais golpes, seja resiliente e continue! tente mais uma vez!')
            dano += 1

        else:
            print('Essa não é uma opção válida, meu guerreiro!')

    if dano > 5:
        print('Você conseguiu escapar de seus ataques! e sair vivo dessa batalha sangrenta!')
        sleep(tempo)
        print('Você venceu, mas infezlimente a hydra conseguiu escapar com vida')
        sleep(tempo)
        print('Desse dia em diante, você decidiu que seu maior objetivo seria procurar por ela')
        sleep(tempo)
        print('E mata-lá"!')

    else:
        print('Você se feriu além do limite, perdendo sangue demais')
        sleep(tempo)
        print('Essa foi sua última batalha em vida')
        sleep(tempo)
        print('Você morreu.')


if __name__ == '__main__':
    pass
