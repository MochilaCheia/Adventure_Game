def luta_troll():
    golpes = ['3', '5', '7']
    ponto_critico = '7'
    print('Um troll de diamante selvagem apareceu! e você precisa atacar!')
    escolha = input('Quantos golpes você vai dar?\nOpções: '+','.join(golpes))
    if escolha == '3':
        print('Não foi o bastante pra derrotar o troll de diamante selvagem.')
    elif escolha == '5':
        print('Faltou pouco pra derrotar ele')
    elif escolha == ponto_critico:
        print('Você acertou no ponto fraco da armadura de cristais e finalmente derretou ele.\nParabéns jovem espachim! você se saiu vitorioso! ')
    else:
        print('Essa não é uma opção jovem guerreiro.')

def confront_medusa():
    corpo_medusa = ['Cabeça', 'Pescoço', 'Torso', 'Barriga', 'Braços', 'Pernas']
    pass

if __name__ == '__main__':
    print(luta_troll())