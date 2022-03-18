from time import sleep

# FLAG: componentes do inventario

def inventario_adicionar_padrao():
    print('Você acessou seu inventário.')
    inventario_inicial = ['Vazio']
    print(f'Seu inventário está {inventario_inicial[0]}.')

    escolha = input('Deseja adicionar a Espada flamejante ancestral ao seu inventário?\n')
    escolha_tratada = escolha.lower().strip()

    if escolha_tratada == 'sim':

        inventario_inicial.pop()
        inventario_inicial.append('Espada flamejante ancestral')
        print('A Espada flamejante ancestral foi adicionada ao seu inventário.')

        sleep(1)
        pergunta = input('Deseja ver seu inventário?\n')
        pergunta_tratada = pergunta.lower().strip()

        if pergunta_tratada == 'sim':
            print(f'No seu inventário tem: {inventario_inicial[0]}.')

        else:
            print('Fechando inventário.')

    else:
        print(f'Seu inventário continuara {inventario_inicial[0]}.')

def inventario_adicionar():
    sleep(1)
    print('Você acessou seu inventário.')
    inventario_adicionar = ['Vazio']
    sleep(1)
    print(f'Seu inventário está {inventario_adicionar[0]}.')

    sleep(1)
    escolha = input('Deseja adicionar um item ao seu inventário?\n')
    escolha_tratada = escolha.lower().strip()

    if escolha_tratada == 'sim':

        inventario_adicionar.pop()
        sleep(1)
        adicao = input('Digite o item que deseja adicionar ao seu inventario:\n')
        inventario_adicionar.append(adicao)
        adicao_limpa = adicao.strip()
        sleep(1)
        print(f'A {adicao_limpa} foi adicionado ao seu inventário.')
        sleep(1)
        pergunta = input('Deseja ver seu inventário?\n')
        pergunta_tratada = pergunta.lower().strip()

        if pergunta_tratada == 'sim':
            print(f'No seu inventário tem: {inventario_adicionar[0]}.')

        else:
            print('Fechando inventário.')

    else:
        print(f'Seu inventário continuara {inventario_adicionar[0]}.')

def diario():
    pass

if __name__ == '__main__':
    pass