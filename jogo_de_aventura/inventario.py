from time import sleep

# FLAG: componentes do inventario

def inventario_ato1():
    print('Você acessou seu inventário.')
    inventario_inicial = ['Vazio']
    print(f'Seu inventário está {inventario_inicial[0]}.')

    escolha = input('Deseja adicionar a Espada flamejante ancestral ao seu inventário?\n')

    if escolha == 'Sim':

        inventario_inicial.pop()
        inventario_inicial.append('Espada flamejante ancestral')
        print('A Espada flamejante ancestral foi adicionada ao seu inventário.')

        sleep(1)
        pergunta = input('Deseja ver seu inventário?\n')

        if pergunta == 'Sim':
            print(f'No seu inventário tem: {inventario_inicial[0]}.')

        else:
            print('Fechando inventário.')

    else:
        print(f'Seu inventário continuara {inventario_inicial[0]}.')

if __name__ == '__main__':
    print(inventario_ato1())