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
    print('O que ele quis dizer com isso? - você se pergunta.')
    sleep(2)
    print('bate uma brisa de vento e você nota que está com fome.\n')
    sleep(4)

    acao = input('Você:\n1) Levanta e vai a procura de comida, abrigo e roupas para se vestir.\n2) Se irrita com o mago e tenta bater nele com alguma coisa perto de você.\n\n')

# FlAG: parte em construção e desenvolvimento

    if acao == '1':
        monstros = [('** Troll de diamante **'), '', '']
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

# REDFLAG: Final da primeira rota.

        elif acao == '2':
            sleep(2)
            print('Você se esconde em um arbusto e observa o comportamento do/da...')

            acao = input('')

            if acao == '1':
                sleep()
                print('')
                sleep()

                acao = input('')

            elif acao == '2':
                sleep()
                print('')
                sleep()

                acao = input('')

# FLAG: função de luta entra nessa rota da história #1
# FLAG: história continua aqui #1

    elif acao == '2':
        sleep(3)
        print('Você joga pedras e galhos nele mas todas simplesmente atravessam seu corpo, você então pega um galho grande ao seu lado e mesmo assim tenta bater nele.\nO fantasma para o bastão com a mão e diz:')
        sleep(3)
        print('\n"- Deixe meu cajado mágico em paz". o cajado então fica translúcido.\n')
        sleep(4)
        print('Você fica admirado e então pergunta novamente:\n\n"- Quem sou eu e o que eu estou fazendo aqui?"\n')
        sleep(5)

        acao = input('\nVocê:\n1) se desculpa por tentar acertar ele mais cedo.\n2) se levanta irritado, pega sua espada e vai caçar alguma coisa, procurar dentro de uma caverna.\n')

        if acao == '1':
            sleep(2)
            print('O Mago te lança um olhar frio e então suspira e diz:\n')
            sleep(3)
            print('\n"- Você sempre foi assim, desde de pequeno, não me surpreende que tenha puxado tanto ele com seu jeito impulsivo".')
            sleep(2)
            print('\n"- DE QUEM VOCÊ TÁ FALANDO SEU VELHO SENIL?"- você grita confuso e com dores de cabeça.\n')
            sleep(2)
            print('\n"- Hora de quem mais? não me diga que não se lembra"')
            sleep(2)
            print('\n"- NÃO, EU NÃO CONSIGO ME LEMBRAR DE NADA! "')
            sleep(2)
            print('\n"- Estou falando do seu pai, Arthur..."')
            sleep(4)
            print('Nesse momento um flash de memória passa pela sua mente, imagens aparentemente desconexas se juntam, não formam uma imagem muito clara\nMas é possível ver um homem alto, segurando algo... uma bainha? NÃO! É SEM DÚVIDA NENHUMA UMA ESPADA!\n')
            sleep(3)
            print('Voltando a sí, você respira fundo e olha pro velho fantasma, ele está te olhando estranho,então você toma coragem e...')
            sleep(5)

            acao = input('\n1)Diz: "- Eu quero saber quem eu sou e farei o necessário para descobrir, não importando o preço." \n2)Pergunta: "- Me diga o que fazer, como faço para reaver minhas memórias?"')


            if acao == '1':
                sleep(2)
                print('\n"- Seu pai não aprovaria seu comportamento, Arthur. ele te deixou essa espada pra proteger os fracos e inocentes."')
                sleep(3)
                print('\n"- Ela está em minha posse agora e farei dela o começo do meu império, independente dos motivos de meu pai, essa espada será usada pra conquistar."')
                sleep(3)
                print('\n"- Vamos começar com essa floresta mago, me diga como torna-lá minha, ela será meu primeiro passo. Depois de conquistar o mundo, tenho certeza que minhas memórias retornarão"')

                acao = input('1) "- Se deseja conquistar essas terras, subjulgue todas as criaturas que vivem aqui." 2) "- O começo do mal está na ganância, tem certeza que deseja desviar do seu caminho?"')

                if acao == '1':
                    sleep()
                    print('')
                    sleep()

                    acao = input('')

# FLAG: história continua aqui #2

                elif acao == '1':
                    sleep()
                    print('')
                    sleep()

                    acao = input('')

# FLAG: história continua aqui #3

            elif acao == '2':
                sleep(2)
                print('\n"- Eu não sei a causa que te fez perder suas mémorias, menino Arthur.\nPórem temo que só vá consegui-las novamente após achar a causa por de trás disso."')
                sleep(3)
                print('\n"- Por onde eu deveria começar se não me lembro de nada?"')
                sleep(3)
                print('\n"- Pelo mesmo motivo que nos trouxe aqui, a caverna de cristais espirais. Nós viemos atrás de suas riquezas e poderes."')
                sleep(4)
                print('\n"- Me mostre o caminho então, velho razinza."')
                sleep(3)
                print('O mago aponta por de dentro da floresta, segundo ele: a caverna está no coração da floresta de caldas,\ne quanto mais próxima dela mais criaturas poderosas e versáteis habitam.')
                sleep(3)

                acao = input('Você deve decidir:\n1) Seguir direto até a caverna, o mais rápido que puder e se preparar para enfrentar todo tipo de criatura existente 2) Planejar e mapear a floresta, perder dias estudando o local e anotar tudo para os próximos que vierem até aqui.')

                if acao == '1':
                    sleep()
                    print('')
                    sleep()

                    acao = input('')

# FLAG: história continua aqui #4

                elif acao == '2':
                    sleep()
                    print('')
                    sleep('')

                    acao = input('')

# FLAG: história continua aqui #5

        elif acao == '2':
            sleep(2)
            print('Você acaba em um ambiente atípico e hostil, seus instintos te dizem pra correr o mais rápido e pra mais longe que puder,\nmas antes que tenha tempo pra virar e fugir, você é cercado por uma criatura... uma só? ou várias?\n')
            sleep(4)
            print('Você não acredita no que seus olhos estão te mostrando, ao mesmo tempo que são várias criaturas parecem ser... uma só?')
            sleep(5)
            print('Um monstro bizarro e nojento ou uma alcatéia de grandes lobos selvagens\ncom pêlos escuros como a noite e no meio deles, tem tentáculos de um polvo gigante saindo, mas nem estamos perto do mar???')
            sleep(4)
            print('Independentemente de quão bizarra seja essa situação, você precisa se mover,\nprecisa tomar uma atitude e logo, antes que seja tarde')
            sleep(4)

            acao = input('\n1) Você percebe que está cercado sua única escolha é fazer o que veio fazer, Caçar\n2) Dentre eles, você nota alguns lobos únicos e diferentes e investe nisso')

            if acao == '1':
                sleep()
                print('')
                sleep()

                acao = input('')

# FLAG: história continua aqui #6

            elif acao == '2':
                sleep()
                print('')
                sleep()

                acao = input('')

# FLAG: história continua aqui #7

elif acao == '2':
    sleep(2)
    print('Enquanto corre pela floresta você tropeça e caí em um ninho de cobras-trovão.\n(elas são conhecidas pelos apitos na ponta da calda que ao balançar emite o som de um trovão.')
    sleep(5)
    print('você está desprotegido e deixou sua espada lá trás, você é atacado e morre lentamente com o veneno.')
    sleep(5)
    print('Você morreu.')

# REDFLAG: Final da segunda rota.