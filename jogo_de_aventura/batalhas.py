import random
from time import sleep

def luta_troll():
    golpes = ['3', '5', '7']
    ponto_critico = '7'
    sleep(2)
    print('Um troll de diamante selvagem apareceu! e você precisa atacar!')
    sleep(3)
    #while
    escolha = input('Quantos golpes você vai dar?\nOpções: '+','.join(golpes))
    if escolha == '3':
        print('Não foi o bastante pra derrotar o troll de diamante selvagem.')
    elif escolha == '5':
        print('Faltou tão pouco pra derrotar ele.')
    elif escolha == ponto_critico:
        print('Você acertou no ponto fraco da armadura de cristais e finalmente derrotou ele.\nParabéns jovem espachim! você se saiu vitorioso!')
    else:
        print('Essa não é uma opção, jovem guerreiro.')

def confronto_medusa():
    corpo_medusa = ['Cabeça', 'Pescoço', 'Torso', 'Barriga', 'Braços', 'Pernas']
    golpe_final = 'Pescoço'
    sleep(2)
    print('Você só tem uma única chance de matar a Medusa, acertando seu ponto fraco, escolha com sabedoria aonde vai atacar.')
    sleep(3)
    ataque = input('Só poderá atacar nesses lugares, escolha um e digite para atacar: '+','.join(corpo_medusa))
    if ataque == 'Cabeça':
        print('A cabeça da Medusa está cheia de cobras que defendem seu ataque, te picam e o veneno te transforma em pedra.')
    elif ataque == 'Torso':
        print('O torso dela é duro demais, sua espada não consegue atravessar.')
    elif ataque == 'Barriga':
        print('Sua barriga é coberta de escamas, mas você morrerá como um valente guerreiro.')
    elif ataque == 'Braços':
        print('Seus braços podem se regenerar em instantes.')
    elif ataque == 'Pernas':
        print('Suas pernas decepatadas viram uma longa calda de cobra')
    elif ataque == golpe_final:
        print('Você venceu, ímbátivel guerreiro e ganhou o título de matador de maldiçôes.\nAcertou seu ponto fraco e com seu pescoço cortado você ainda pode transformas sua cabeça em um escudo.\n')
    else:
        print('Essa não uma opção, jovem espachim.')

def luta_azetris():
    tentativa = int(input('Quantos golpes você acha necessário para derrotar o monstro azetris:\n~~Digite o número~~\n'))
    golpes_necessarios = [2, 3, 4, 5, 6, 8, 9, 10 , 11, 12, 13, 14, 15, 16, 17, 18]
    for busca in golpes_necessarios:
        if tentativa >= 18:
            print('Você acertou ele: {} vezes' .format(busca))
            break

def batalha_acylla():
    pass

def confronto_hydra():
    desvios = ['Esquerda', 'Direita', 'Meio', 'Cima', 'Baixo']
    ataque = input('Adivinha:')
    while ataque != 'Desisto':
        regenerando_direcao = random.choice(desvios)
        if ataque == regenerando_direcao:
            print(regenerando_direcao)
            print('Você acertou!')
            nova_chance = input('continuar?')

def ultima_luta():
    protagonista = 100
    antagonista = 100
    golpe_espada = -5
    golpe_machado = -15
    soco = -5
    chute = -10
    cabeçada = -3
    #if, while ou for?


if __name__ == '__main__':
    #print(luta_azetris())
    #print(confronto_medusa())
    #print(luta_troll())
    #print(batalha_acylla())
    #print(confronto_hydra())
    #print(ultima_luta())
    pass