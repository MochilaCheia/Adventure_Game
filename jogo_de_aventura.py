import random
from time import sleep

def player():
    nome_player = input('Vamos começar! Qual seu nome?')

print('Durante a Era do Rei Arthur e seus doze Cavaleiros, monstros e criaturas ainda eram comuns no mundo,\nseres fantásticos que hoje apenas existem no imaginário das pessoas. \nE essa é história das suas aventuras, conquistas e perdas na última era dos monstros e magia.')
sleep(6)
print('A sua história se inicia não exatamente no começo, mas nesse momento estranhamente diferente,\nem uma aldeia onde os ataques ocasiões de monstros  costumam frequentes mas mesmo assim costuma ser um lugar calmo e pacato,\nexceto pelo cavaleiro pelado na floresta falando sozinho, e esse é você:')
sleep(6)
print('Um estranho desacordado na floresta, pelado e sem se lembrar de nada,\napenas com sua espada e um fantasma de um mago resmungão,\né assim que começa a sua história.')
sleep(6)
print('Ao abrir seus olhos e observar seu entorno encontra\num cenário nada familiar, mas você nem mesmo lembra de algo...')
sleep(6)
print('Enquanto continua procurando alguma coisa que te lembre algo você apenas vê uma espada ao seu lado e se questiona\nporque está sem roupas e com fome, quando de repente...\nBOOM, UM FANTASMA DE UM MAGO VELHO APARECE NA SUA FRENTE FALANDO TANTA COISA QUE TE DEIXA ATORDOADO.')
sleep(6)
print('Você está assustado, mas precisa tomar uma decisão:\n')

acao = input('1) se acalma e pergunta pro mago tudo que quer saber.\n2) decide fugir para a floresta e procurar a aldeia humana mais próxima, afinal você está com medo de ser assombrado.\n\n>> Digite apenas o número 1 ou número 2 para escolher. <<\n\n')

if acao == '1':
    sleep(2)
    print('Você pergunta ao mago tudo que quer saber, mas ele briga com você e fala um monte de asneira sobre você ser irresponsável e nunca escutar ele.')
    sleep(3)
    print('Ele tem um sotaque forte e fala algo que te chama a atenção:')
    sleep(3)
    print('\n" - Essa sua idéia de explorar as cavernas de relíquias não poderia ser pior".')
    sleep(3)
    print('\nO que ele quis dizer com isso? - você se pergunta.')
    sleep(2)
    print('\nbate uma brisa de vento e você nota que está com fome.\n')

    acao = input('Você:\n1) Levanta e vai a procura de comida, abrigo e roupas para se vestir.\n2) Se irrita com o mago e tenta bater nele com alguma coisa perto de você.\n\n')

    if acao == '1':
        monstros = [('** Troll de diamante **', Lutas.luta_troll), 'Matheus', 'Sil']
        criatura, luta = random.choice(monstros)
        sleep(2)
        print('Ao procurar comida na floresta, você se depara nada mais nada menos do que um... {}\n' .format(criatura))
        sleep(3)
        print('E agora, o que você fará?\n')
        sleep(3)
        acao = input('1) sacar sua espada e atacar a criatura sem parar.\n2) Observar enquanto se afasta da criatura sem chamar sua atenção.\n\n')

        if acao == '1':
            sleep(3)
            print('Ao atacar a criatura sem parar você quebra sua espada e fica indefeso.')
            sleep(4)
            print('a criatura se enfurece pelos ataques e usa suas garras para rasgar seu peito desprotegido.')
            sleep(4)
            print('Você morreu.')

# Final da primeira rota.

        elif acao == '2':
            print('Você se esconde em um arbusto e observa o comportamento do/da...')
            acao = input('')
            pass

    elif acao == '2':
        print('Você joga pedras e galhos nele mas todas simplesmente atravessam seu corpo, você então pega um galho grande ao seu lado e mesmo assim tenta bater nele.\nO fantasma para o bastão com a mão e diz:')
        print('\n"- Deixe meu cajado mágico em paz". o cajado então fica translúcido.\n')
        print('\n\nVocê fica admirado e então pergunta novamente:\n\n"- Quem sou eu e o que eu estou fazendo aqui?"\n')
        acao = input('\nVocê:\n1) se desculpa por tentar acertar ele mais cedo.\n2) se levanta irritado, pega sua espada e vai caçar alguma coisa, procurar dentro de uma caverna.\n')

        if acao == '1':
            print('')
            input('')
            pass

        elif acao == '2':
            print('')
            input('')
            pass

elif acao == '2':
    sleep(2)
    print('Enquanto corre pela floresta você tropeça e caí em um ninho de cobras-trovão.\n(elas são conhecidas pelos apitos na ponta da calda que ao balançar emite o som de um trovão.')
    sleep(5)
    print('você está desprotegido e deixou sua espada lá trás, você é atacado e morre lentamente com o veneno.')
    sleep(5)
    print('Você morreu.')

# Final da segunda rota.