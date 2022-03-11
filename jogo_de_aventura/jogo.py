import random
import componentes
import inventario
from time import sleep


componentes.introducao()

sleep(0.5)
nome_player = input('\nMas antes de começarmos, me diga seu nome jovem héroi: ')
sleep(1)
print(f'Seja bem vindo, {nome_player}! e boa aventura!\n')

sleep(3)
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

acao = input('1) se acalma e pergunta pro mago tudo que quer saber.\n2) decide fugir para a floresta e procurar a aldeia humana mais próxima, afinal você está com medo de ser assombrado.\n\n>> Digite apenas o número 1 ou número 2 para escolher e seguir a história ou o número 3 pra acessar seu arsenal. <<\n\n')

while acao == '3':
    sleep(1)
    inventario.inventario_adicionar_padrao()
    sleep(3)
    acao = input('>> Digite apenas o número 1 ou número 2 para escolher e seguir a história <<')

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
        sleep(2)
        print('E agora, o que você fará?\n')
        sleep(3)

        acao = input('1) sacar sua espada e atacar a criatura sem parar.\n2) Observar enquanto se afasta da criatura sem chamar sua atenção.\n\n')

        if acao == '1':
            sleep(3)
            print('Ao atacar a criatura sem parar você quebra sua espada e fica indefeso.')
            sleep(3)
            print('a criatura se enfurece pelos ataques e usa suas garras para rasgar seu peito desprotegido.')
            sleep(3)
            componentes.final_incompleto(nome_player)

# REDFLAG: Final da primeira rota.

        elif acao == '2':
            sleep(2)
            print('Você se esconde em um arbusto e observa o comportamento do/da...')

            acao = input('')

            if acao == '1':
                sleep()
                print('')
                sleep()

                acao = input('\n')

            elif acao == '2':
                sleep()
                print('')
                sleep()

                acao = input('\n')

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

                    acao = input('\n')

# FLAG: história continua aqui #2

                elif acao == '1':
                    sleep()
                    print('')
                    sleep()

                    acao = input('\n')

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

                    acao = input('\n')

# FLAG: história continua aqui #4

                elif acao == '2':
                    sleep()
                    print('')
                    sleep('')

                    acao = input('\n')

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

            acao = input('\n1) Você percebe que está cercado sua única escolha é fazer o que veio fazer, Caçar\n2) Dentre eles, você nota alguns lobos únicos e diferentes e decide investir nisso')

            if acao == '1':
                sleep(2)
                print('Ao respirar fundo você aguça seus sentidos e prepara seu instinto para batalha e massacre que está por vir.')
                sleep(2)
                print('Você começa a cortar tentaculos e decapitar os lobos escuros como a noite, ')

                acao = input('\n')

# FLAG: história continua aqui #6

            elif acao == '2':
                sleep(2)
                print('Seu investimento deu frutos, no meio "disso" tem lobos, lobos aparentemente normais, que estão sendo enganados por seja lá o que seja isso.')
                sleep(3)
                print('Como são lobos, você pode fazer eles te ajudarem, só precisa convencer esses animais.')
                sleep(3)
                print('Essa é uma situação de vida ou morte, seu decisão será brutal...')

                acao = input('\n1) Faça os lobos se aliarem a você mostrando sua determinação e sacrifício\n2) Para convencer os lobos, teria que pagar um preço alto demais, você téra que sobreviver a isso sozinho')

                if acao == '1':
                    sleep(2)
                    print('A única forma deles se aliarem e oferecendo algo que vai diminuir sua fome.\nVocê não está com nenhuma comida...')
                    sleep(2)
                    print('Você então pega sua espada, respira fundo e serra seus dentes\nEm um único corte limpo você decepa seu braço esquerdo.')
                    sleep(4)
                    print('Você então joga seu braço para os lobos brancos em sinal de confiança, os lobos estranham seu gesto,\nmas aceitam e vão para o seu lado como força de respeito, você usa a boca do maior lobo para estancar o sangramento do seu braço com os dentes.')
                    sleep(2)
                    print('Agora é hora de virar o jogo.')

                    acao = input('\1) Você está ferido, concentre-se na defesa e em aguentar mais um pouco 2) Avance, mesmo ferido só resta lutar agora.')

                    if  acao == '1':
                        sleep(2)
                        print('')
                        sleep()

                        acao = input('\n')

# GOLDFLAG: final de rota previsto
# FLAG: história continua aqui #7

                    elif acao == '1':
                        sleep(2)
                        print('')
                        sleep()

                        acao = input('\n')

# FLAG: história continua aqui #8

                elif acao == '2':
                    sleep(2)
                    print('Preparando-se para matar a todos os lobos, um frio percorre sua espinha, sente que o que está prestes a enfrentar está muito além da força humana.')
                    sleep(3)
                    print('O sol começa a ser por e um festival de sangue é iluminado pela luz alaranjada que vem do horizonte, você cada vez mais se apróxima do centro da criatura bizarra.')
                    sleep(4)
                    print('Proxímo do centro da criatura você não acredita no que seus olhos estão te mostrando... aquilo é... não pode ser, por que tem uma linda mulher ali?\nEla ainda está viva? ou ela apenas é um cadaver no boca da criatura???')
                    sleep(3)
                    print('Não importa, agora sei que ali é o centro, tenho certeza, lá encontrarei o coração da criatura e poderei dar um fim a isso.')
                    sleep(2)
                    print('Ao chegar no centro você percebe que a moça não está morta???\nEla começa a falar alguma coisa...')

                    acao = input('\n1) Você se aproxima para escutar o que ela tem a dizer\n2) Apenas a mata, isso com certeza é uma armadilha!')

                    if acao == '1':
                        sleep(2)
                        print('Ela está sussurando algo...')
                        sleep(3)
                        print('"- Seu destino de agora em diante será coberto de trevas e desespero, em meu último suspiro te amaldiçoo até o fim de sua vida..."')
                        sleep(3)
                        print('Independente do que ela tenha dito, você precisa matar ela, ir até o fim com sua decisão.')

                        acao = input('\n1) Decepar a cabeça da mulher\n2) Antes de mata-lá, tentar conversar')

                        if acao == '1':
                            sleep(2)
                            print('A cabeça da mulher ou será da criatura rola pelo chão e seu sangue deixou seu corpo e sua espada encharcados... ')
                            sleep(3)
                            print('Quando você olha pra sua espada percebe que ela está se dissolvendo, o sangue da criatura era um ácido extremamente letal!')
                            sleep(3)
                            print('Já é tarde demais pra se salvar, o sangue dela queima sua pele, seu maior arrenpedimento vai ser não ter  feito as coisas diferentes, você morrera sem se lembrar de nada.')
                            sleep(3)
                            componentes.final_incompleto(nome_player)

# REDFLAG: Final da terceira rota.

                        elif acao == '2':
                            sleep(2)
                            print('Ela está falando algo muito baixo...')
                            sleep(2)
                            print('Você se aproxima lentamente, com cautela, qualquer movimento errado pode significar sua morte.')
                            sleep(2)
                            print('Finalmente você é capaz de ouvir os lamentos da pobre criatura em seus últimos suspiros')
                            sleep(3)
                            print('\n"- Você tomou a decisão correta, e a partir de agora colherá os frutos de sua coragem, eu te aprovo, meu caro principe".\n')
                            sleep(2)
                            print('\n"- Que as trevas te acompanhem, que os ventos do norte te guiem e que meus irmãos')
                            sleep(1)
                            print('e irmãs de sangue sejam seu súditos fieis e te ajudem a erguer o tão esperado reinado dos monstros."\n')
                            sleep(2)
                            print('Ao terminar de falar, ela cita seu próprio nome... Acylla... uma forma de maldição antiga e aprisionamento de sua alma.')
                            sleep(2)
                            print('Enquanto você viver, de hoje em diante só lhe restará mal em seu caminho.')
                            sleep(1)
                            print('Seu destino então foi selado...')
                            sleep(2)
                            print('Desde então inúmeros monstros juraram lealdade a sua linhagem, com o passar do tempo o número só aumentava.')
                            sleep(2)
                            print('Uma horda de monstros ao seu redor foi dominando os territórios, foram se procriando e aumentando seu reino de destruição.')
                            sleep(3)
                            print('Você nunca quis aquilo, mas não pode fazer nada a respeito, sua própria vontade estava selada na maldiçao feita com a alma e nome de Acylla.')
                            sleep(2)
                            print('Com mais tempo o mundo conheceu sua pior época, o reinado dos monstros pelo continente, liderados por você, o rei dêmonio.')
                            sleep(2)
                            print('Até mesmo após sua morte seu reinado continuaria com sua linhagem, sua vida foi prolongada pelos monstros...')
                            sleep(2)
                            print('Mas finalmente após milhares de anos... ')
                            componentes.final_incompleto(nome_player)

# BLACKFLAG: final da quinta rota

                    elif acao == '2':
                        sleep(3)
                        print('Ao mata-lá você nunca saberá o que ela estava dizendo com certeza.')
                        sleep(2)
                        print('Apenas imagina que seja lá o que fosse, seria cobertor de ódio, desprezo e amargor, com certeza')
                        sleep(2)
                        print('Você aprendeu e sente que fez o certo, que sangue e morte são sua única escolha, você sobriviveu aqui e agora')
                        sleep(2)
                        print('Seu passado e suas mémorias já não importam mais, você vai seguir em frente e trilhar seu próprio caminho.')
                        sleep(2)
                        print('Você abandona o fantasma na floresta e parte para o continente para conquistar terras, saquear e se fazer rei a qualquer custo...')
                        sleep(1)
                        print('Suas escolhas até aqui o tornaram o Rei Tirano...')
                        sleep(2)
                        print('Seu reinado de caos e dor durou sua vida inteira...')
                        sleep(3)
                        print('Final ruim...')
                        print('E depois de dezenas de anos finalmente...')
                        componentes.final_incompleto(nome_player)

# BLACKFLAG: final da quarta rota

elif acao == '2':
    sleep(2)
    print('Enquanto corre pela floresta você tropeça e caí em um ninho de cobras-trovão.')
    sleep(2)
    print('elas são conhecidas pelos apitos na ponta da calda que ao balançar emite o som de um trovão.')
    sleep(2)
    print('você está desprotegido e deixou sua espada lá trás, você é atacado e morre lentamente com o veneno.')
    sleep(2)
    componentes.final_incompleto(nome_player)

# REDFLAG: Final da segunda rota.