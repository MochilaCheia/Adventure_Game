import random
import componentes
import inventario
from time import sleep

tempo = int(input('Quantos segundos você gostaria até cada frase aparecer?\n'
                  'Digite apenas o número e lembre-se, as frases não são muito longas\n'))

sleep(tempo)
print('Vamos começar então!\n')

componentes.introducao(tempo)

sleep(tempo)
nome_player = input('\nMas antes de começarmos, me diga seu nome jovem héroi: ')
sleep(tempo)
print(f'Seja bem vindo, {nome_player}! e boa aventura!\n')

sleep(tempo)
print('Durante a Era do Rei Arthur e seus doze Cavaleiros, monstros e criaturas ainda eram comuns no mundo,')
sleep(tempo)
print('seres fantásticos que hoje apenas existem no imaginário das pessoas.')
sleep(tempo)
print('E essa é história das suas aventuras, conquistas e perdas na última era dos monstros e magia.')
sleep(tempo)
print('A sua história se inicia não exatamente no começo, mas nesse momento estranhamente diferente,')
sleep(tempo)
print('em uma aldeia onde os ataques ocasiões de monstros'
      ' costumam frequentes mas mesmo assim costuma ser um lugar calmo e pacato,')
sleep(tempo)
print('exceto pelo cavaleiro pelado na floresta falando sozinho, e esse é você:')
sleep(tempo)
print('Um estranho desacordado na floresta, pelado e sem se lembrar de nada,')
sleep(tempo)
print('apenas com sua espada e um fantasma de um mago resmungão, é assim que começa a sua história.')
sleep(tempo)
print('Ao abrir seus olhos e observar seu entorno encontra')
sleep(tempo)
print('um cenário nada familiar, mas você nem mesmo lembra de algo...')
sleep(tempo)
print('Enquanto continua procurando alguma coisa que te lembre algo'
      ' você apenas vê uma espada ao seu lado e se questiona')
sleep(tempo)
print('porque está sem roupas e com fome, quando de repente...')
sleep(tempo)
print('BOOM, UM FANTASMA DE UM MAGO VELHO APARECE NA SUA FRENTE FALANDO TANTA COISA QUE TE DEIXA ATORDOADO.')
sleep(tempo)
print('Você está assustado, mas precisa tomar uma decisão:\n')
sleep(tempo)

acao = input('1) se acalma e pergunta pro mago tudo que quer saber.\n'
             '2) decide fugir para a floresta e procurar a aldeia humana mais próxima,'
             ' afinal você está com medo de ser assombrado.\n\n'
             '>> Digite apenas o número 1 ou número 2 para escolher '
             'e seguir a história ou o número 3 pra acessar seu arsenal. <<\n\n')

while acao == '3':
    sleep(tempo)
    inventario.inventario_adicionar_padrao()
    sleep(tempo)
    acao = input('>> Digite apenas o número 1 ou número 2 para escolher e seguir a história <<')

if acao == '1':
    sleep(tempo)
    print('Você pergunta ao mago tudo que quer saber, mas ele briga com você e fala '
          'um monte de asneira sobre você ser irresponsável e nunca escutar ele.')
    sleep(tempo)
    print('Ele tem um sotaque forte e fala algo que te chama a atenção:')
    sleep(tempo)
    print('\n" - Essa sua idéia de explorar as cavernas de relíquias não poderia ser pior".')
    sleep(tempo)
    print('O que ele quis dizer com isso? - você se pergunta.')
    sleep(tempo)
    print('bate uma brisa de vento e você nota que está com fome.\n')
    sleep(tempo)

    acao = input('Você:\n1) Levanta e vai a procura de comida, abrigo e roupas para se vestir.\n'
                 '2) Se irrita com o mago e tenta bater nele com alguma coisa perto de você.\n\n')

# FlAG: parte em construção e desenvolvimento

    if acao == '1':
        monstros = ['Troll de diamante', 'Porco voador roxo', 'Arvore de seiva maligna']
        criatura, luta = random.choice(monstros)
        sleep(tempo)
        print('Ao procurar comida na floresta, você se depara nada mais nada menos do que um... {}\n'.format(criatura))
        sleep(tempo)
        print('E agora, o que você fará?\n')
        sleep(tempo)

        acao = input('1) sacar sua espada e atacar a criatura sem parar.\n'
                     '2) Observar enquanto se afasta da criatura sem chamar sua atenção.\n\n')

        if acao == '1':
            sleep(tempo)
            print('Ao atacar a criatura sem parar você quebra sua espada e fica indefeso.')
            sleep(tempo)
            print('a criatura se enfurece pelos ataques e usa suas garras para rasgar seu peito desprotegido.')
            sleep(tempo)
            componentes.final_incompleto(nome_player, tempo)

# REDFLAG: final da primeira rota.

        elif acao == '2':
            sleep(tempo)
            print('Você se esconde em um arbusto e observa o comportamento do/da...')

            acao = input('')

            if acao == '1':
                sleep(tempo)
                print('')
                sleep(tempo)
                pass

                acao = input('\n')

            elif acao == '2':
                sleep(tempo)
                print('')
                sleep(tempo)

                acao = input('\n')

# FLAG: função de luta entra nessa rota da história #1
# FLAG: história continua aqui #1

    elif acao == '2':
        sleep(tempo)
        print('Você joga pedras e galhos nele mas todas simplesmente atravessam seu corpo, '
              'você então pega um galho grande ao seu lado e mesmo assim tenta bater nele.')
        print('O fantasma para o bastão com a mão e diz:')
        sleep(tempo)
        print('\n"- Deixe meu cajado mágico em paz". o cajado então fica translúcido.\n')
        sleep(tempo)
        print('Você fica admirado e então pergunta novamente:\n')
        sleep(tempo)
        print('"- Quem sou eu e o que eu estou fazendo aqui?"\n')
        sleep(tempo)

        acao = input('\nVocê:\n1) se desculpa por tentar acertar ele mais cedo.\n'
                     '2) se levanta irritado, pega sua espada e vai caçar alguma coisa, '
                     'procurar dentro de uma caverna.\n')

        if acao == '1':
            sleep(tempo)
            print('O Mago te lança um olhar frio e então suspira e diz:\n')
            sleep(tempo)
            print('\n"- Você sempre foi assim, desde de pequeno, '
                  'não me surpreende que tenha puxado tanto ele com seu jeito impulsivo".')
            sleep(tempo)
            print('\n"- DE QUEM VOCÊ TÁ FALANDO SEU VELHO SENIL?"- você grita confuso e com dores de cabeça.\n')
            sleep(tempo)
            print('\n"- Hora de quem mais? não me diga que não se lembra"')
            sleep(tempo)
            print('\n"- NÃO, EU NÃO CONSIGO ME LEMBRAR DE NADA! "')
            sleep(tempo)
            print('\n"- Estou falando do seu pai, Arthur..."')
            sleep(tempo)
            print('Nesse momento um flash de memória passa pela sua mente, '
                  'imagens aparentemente desconexas se juntam, não formam uma imagem muito clara')
            sleep(tempo)
            print('Mas é possível ver um homem alto, segurando algo... '
                  'uma bainha? NÃO! É SEM DÚVIDA NENHUMA UMA ESPADA!\n')
            sleep(tempo)
            print('Voltando a sí, você respira fundo e olha pro velho fantasma, '
                  'ele está te olhando estranho,então você toma coragem e...')
            sleep(tempo)

            acao = input('\n1)Diz: "- Eu quero saber quem eu sou e farei o necessário para descobrir, '
                         'não importando o preço." \n2)Pergunta: "- Me diga o que fazer, '
                         'como faço para reaver minhas memórias?"')

            if acao == '1':
                sleep(tempo)
                print('\n"- Seu pai não aprovaria seu comportamento, Arthur. '
                      'ele te deixou essa espada pra proteger os fracos e inocentes."')
                sleep(tempo)
                print('\n"- Ela está em minha posse agora e farei dela o começo do meu império, '
                      'independente dos motivos de meu pai, essa espada será usada pra conquistar."')
                sleep(tempo)
                print('\n"- Vamos começar com essa floresta mago, me diga como torna-lá minha, '
                      'ela será meu primeiro passo. Depois de conquistar o mundo, '
                      'tenho certeza que minhas memórias retornarão"')

                acao = input('1) "- Se deseja conquistar essas terras, subjulgue todas as criaturas que vivem aqui."\n'
                             '2) "- O começo do mal está na ganância, '
                             'tem certeza que deseja desviar do seu caminho?"\n\n')

                if acao == '1':
                    sleep(tempo)
                    print('')
                    sleep(tempo)

                    acao = input('\n')

# FLAG: história continua aqui #2

                elif acao == '2':
                    sleep(tempo)
                    print('')
                    sleep(tempo)

                    acao = input('\n')

# FLAG: história continua aqui #3

            elif acao == '2':
                sleep(tempo)
                print('\n"- Eu não sei a causa que te fez perder suas mémorias, menino Arthur.')
                sleep(tempo)
                print('Pórem temo que só vá consegui-las novamente após achar a causa por de trás disso."')
                sleep(tempo)
                print('\n"- Por onde eu deveria começar se não me lembro de nada?"')
                sleep(tempo)
                print('\n"- Pelo mesmo motivo que nos trouxe aqui, '
                      'a caverna de cristais espirais. Nós viemos atrás de suas riquezas e poderes."')
                sleep(tempo)
                print('\n"- Me mostre o caminho então, velho razinza."')
                sleep(tempo)
                print('O mago aponta por de dentro da floresta, segundo ele: '
                      'a caverna está no coração da floresta de caldas,')
                sleep(tempo)
                print('e quanto mais próxima dela mais criaturas poderosas e versáteis habitam.')
                sleep(tempo)

                acao = input('Você deve decidir:\n1) Seguir direto até a caverna, '
                             'o mais rápido que puder e se preparar para enfrentar todo tipo de criatura existente\n'
                             '2) Planejar e mapear a floresta, perder dias estudando o local '
                             'e anotar tudo para os próximos que vierem até aqui.')

                if acao == '1':
                    sleep(tempo)
                    print('')
                    sleep(tempo)

                    acao = input('\n')

# FLAG: história continua aqui #4

                elif acao == '2':
                    sleep(tempo)
                    print('Então você deverá escrever e anotar seus pensamentos e observações em um diário, '
                          'sinta-se livre pra criar da melhor forma que achar.')
                    sleep(tempo)
                    inventario.diario()

                    acao = input('\n')

# FLAG: história continua aqui #5

        elif acao == '2':
            sleep(tempo)
            print('Você acaba em um ambiente atípico e hostil, '
                  'seus instintos te dizem pra correr o mais rápido e pra mais longe que puder,')
            sleep(tempo)
            print('mas antes que tenha tempo pra virar e fugir, '
                  'você é cercado por uma criatura... uma só? ou várias?\n')
            sleep(tempo)
            print('Você não acredita no que seus olhos estão te mostrando, '
                  'ao mesmo tempo que são várias criaturas parecem ser... uma só?')
            sleep(tempo)
            print('Um monstro bizarro e nojento ou uma alcatéia de grandes lobos selvagens')
            sleep(tempo)
            print('com pêlos escuros como a noite e no meio deles, '
                  'tem tentáculos de um polvo gigante saindo, mas nem estamos perto do mar???')
            sleep(tempo)
            print('Independentemente de quão bizarra seja essa situação, você precisa se mover,')
            sleep(tempo)
            print('precisa tomar uma atitude e logo, antes que seja tarde')
            sleep(tempo)

            acao = input('\n1) Você percebe que está cercado sua única escolha é fazer o que veio fazer, Caçar\n'
                         '2) Dentre eles, você nota alguns lobos únicos e diferentes e decide investir nisso.\n')

            if acao == '1':
                sleep(tempo)
                print('Ao respirar fundo você aguça seus sentidos e '
                      'prepara seu instinto para batalha e massacre que está por vir.')
                sleep(tempo)
                print('Você começa a cortar tentáculos e decapitar os lobos que são engolidos pela noite escura, '
                      'sua espada coberta de sangue se afia nos ossos da criatura.')
                sleep(tempo)
                print('"- QUEM É VOCÊ, CRIATURA NEFASTA! O QUE QUER COMIGO AFINAL!", você grita.')
                sleep(tempo)
                print('Zero respostas, você não obtém nada além de silêncio e ataques.')
                sleep(tempo)
                print('(Isso não te deixa com raiva?)')
                sleep(tempo)

                acao = input('1) Transforme sua raiva em força e ataque!\n2) Você busca respostas e deve obte-lás\n')

                if acao == '1':
                    sleep(tempo)
                    print('Sua raiva não se justifica, ela te queima por dentro e'
                          ' te cega, ela te dará o resultado que busca...')
                    sleep(tempo)
                    print('A qualquer preço...')
                    sleep(tempo)
                    print('O ódio faz seu sangue ferver, sua única vontade é'
                          ' matar aquilo que te ataca e se mostrar superior')
                    sleep(tempo)
                    print('--VOCÊ VIRA UM GUERREIRO BERSERKER--')
                    sleep(tempo)
                    print('Seus ossos estralam, seus músculos contraem e seus urros te dão presença')
                    sleep(tempo)
                    print('Animais que escutam tremem de pavor com o som de algo '
                          'que está preparado pra morrer atacando')
                    sleep(tempo)
                    print('Incansavelmente você luta, você corta com sua espada, você dilacera com suas mãos e dentes')
                    sleep(tempo)
                    print('Você não liga pra sua vida, apenas para a morte daquilo, você alcança seu objetivo...')
                    sleep(tempo)
                    componentes.final_incompleto(nome_player, tempo)

# REDFLAG: final da sétima rota

                elif acao == '2':
                    sleep(tempo)
                    print('')
                    sleep(tempo)

                    acao = input('\n')

# FLAG: história continua aqui #7

            elif acao == '2':
                sleep(tempo)
                print('Seu investimento deu frutos, no meio "disso" tem lobos, '
                      'lobos aparentemente normais, que estão sendo enganados por seja lá o que seja isso.')
                sleep(tempo)
                print('Como são lobos, você pode fazer eles te ajudarem, só precisa convencer esses animais.')
                sleep(tempo)
                print('Essa é uma situação de vida ou morte, seu decisão será brutal...')

                acao = input('\n1) Faça os lobos se aliarem a você mostrando sua determinação e sacrifício.\n'
                             '2) Para convencer os lobos, teria que pagar um preço alto demais, '
                             'você téra que sobreviver a isso sozinho.\n')

                if acao == '1':
                    sleep(tempo)
                    print('A única forma deles se aliarem e oferecendo algo que vai diminuir sua fome.')
                    sleep(tempo)
                    print('Você não está com nenhuma comida...')
                    sleep(tempo)
                    print('Você então pega sua espada, respira fundo e serra seus dentes.')
                    sleep(tempo)
                    print('Em um único corte limpo você decepa seu braço esquerdo.')
                    sleep(tempo)
                    print('Você então joga seu braço para os lobos brancos em sinal de confiança, '
                          'os lobos estranham seu gesto,')
                    sleep(tempo)
                    print('mas aceitam e vão para o seu lado como forma de respeito, você usa a boca do maior lobo'
                          ' para estancar o sangramento do seu braço com os dentes.')
                    sleep(tempo)
                    print('Agora é hora de virar o jogo.')

                    acao = input('\1) Você está ferido, concentre-se na defesa e em aguentar mais um pouco.\n'
                                 '2) Avance, mesmo ferido só resta lutar agora.\n')

                    if acao == '1':
                        sleep(tempo)
                        print('')
                        sleep(tempo)

                        acao = input('\n')

# GOLDFLAG: final de rota previsto
# FLAG: história continua aqui #8

                    elif acao == '1':
                        sleep(tempo)
                        print('Talvez seja pela perda de sangue, talvez seja '
                              'pela adrenalina ou talvez apenas seja por medo de morrer.')
                        sleep(tempo)
                        print('Você monta em um lobo branco, seu sangramento parou mas continua internamente.')
                        sleep(tempo)
                        print('O lobo alfa branco se tinge de carmesim com seu sangue.')
                        sleep(tempo)
                        print('Sua visão está ficando embaçada... você estar perdendo a consciência.')
                        sleep(tempo)
                        print('Com suas últimas forças, você avança, uge de '
                              'dor e fúria e com a alcatéia de lobos brancos,')
                        sleep(tempo)
                        print('Você vai em direção a morte!')
                        sleep(tempo)
                        print('Tentáculos, sangue, presas e garras voam pra todo lado, só tem morte ao redor.')
                        sleep(tempo)
                        print('Os lobos não se afugentam, não existe medo alí, '
                              'o fim se aproxima, você deve escolher como prefere morrer.')

                        acao = input('1) Continue sem parar, lute! mate a criatura e morra em glória.\n'
                                     '2) Mate a criatura e tente salvar o maior número de lobos que puder.')

                        if acao == '1':
                            sleep(tempo)
                            print('Resta pouco da criatura agora, apenas a parte mulher '
                                  'com alguns tentáculos em pedaços e lobos pretos morrendo.')
                            sleep(tempo)
                            print('Ela está sem forças, então você usa um cadáver de lobo como escudo enquanto avança.')
                            sleep(tempo)
                            print('Você finalmente chega no centro da criatura, '
                                  'dá de encontro com a morte certa dela e sua e por fim...')
                            sleep(tempo)
                            print('Você apunha-lá seu coração verde e gosmento, '
                                  'sua espada e suas mãos começam a derreter.')
                            sleep(tempo)
                            print('O sangue corrosivo da criatura está te queimando, '
                                  'mas você não se importa, você a matou, finalmente a matou.')
                            sleep(tempo)
                            print('Em seus últimos momentos, valquírias vem do céu pra'
                                  ' proclamar sua vitória e receber sua alma em vahala.')
                            sleep(tempo)
                            print('Sua te deu o direito, agora você poderá passar a '
                                  'eternidade lutando e conquistando em nome de Odin.')
                            sleep(tempo)
                            print('por fim, você dá seu último suspiro e se vai sorrindo.')
                            sleep(tempo)
                            componentes.final_incompleto(nome_player, tempo)

# REDFLAG: final da sexta rota

                        elif acao == '2':
                            sleep(tempo)
                            print('Que decisão louvável! você não irá se arrepender dessa decisão!')
                            sleep(tempo)
                            print('Você grita para os lobos retrocederem e avança sozinho contra a criatura.')
                            sleep(tempo)
                            print('Não lhe resta muita força, mas você ainda tem o suficiente para mata-lá.')
                            sleep(tempo)
                            print('Você não teme a morte, com toda a força e determinação que tem empunha '
                                  'sua espada e decapita a criatura em forma de mulher.')
                            sleep(tempo)
                            print('Você conseguiu! a matou!')
                            sleep(tempo)
                            print('Sem arrenpedimentos, você cai no chão de costas e olha '
                                  'pro céu, os lobos comovidos te carregam pra cima da colina.')
                            sleep(tempo)
                            print('Seus uivos de dor e tristeza quebram o silêncio da noite.')
                            sleep(tempo)
                            print('Os deuses se emocionam com sua luta e antes de morrer te concedem o título máximo'
                                  ' de matador de monstros! sua história nuca será esquecida, sua lenda será eterna.')
                            sleep(tempo)
                            componentes.final_incompleto(nome_player, tempo)

# REDFLAG: final da sétima rota

                elif acao == '2':
                    sleep(tempo)
                    print('Preparando-se para matar a todos os lobos, um frio percorre sua espinha, sente '
                          'que o que está prestes a enfrentar está muito além da força humana.')
                    sleep(tempo)
                    print('O sol começa a ser por e um festival de sangue é iluminado pela luz alaranjada '
                          ''
                          'que vem do horizonte, você cada vez mais se apróxima do centro da criatura bizarra.')
                    sleep(tempo)
                    print('Proxímo do centro da criatura você não acredita no que seus olhos estão te '
                          'mostrando... aquilo é... não pode ser, por que tem uma linda mulher ali?')
                    sleep(tempo)
                    print('Ela ainda está viva? ou ela apenas é um cadaver no boca da criatura???')
                    sleep(tempo)
                    print('Não importa, agora sei que ali é o centro, tenho certeza, lá encontrarei o '
                          'coração da criatura e poderei dar um fim a isso.')
                    sleep(tempo)
                    print('Ao chegar no centro você percebe que a moça não está morta???')
                    sleep(tempo)
                    print('Ela começa a falar alguma coisa...')

                    acao = input('\n1) Você se aproxima para escutar o que ela tem a dizer.\n'
                                 '2) Apenas a mata, isso com certeza é uma armadilha!\n')

                    if acao == '1':
                        sleep(tempo)
                        print('Ela está sussurando algo...')
                        sleep(tempo)
                        print('"- Seu destino de agora em diante será coberto de trevas e desespero, '
                              'em meu último suspiro te amaldiçoo até o fim de sua vida..."')
                        sleep(tempo)
                        print('Independente do que ela tenha dito, você precisa matar ela, '
                              'ir até o fim com sua decisão.')

                        acao = input('\n1) Decepar a cabeça da mulher.\n2) Antes de mata-lá, tentar conversar.\n')

                        if acao == '1':
                            sleep(tempo)
                            print('A cabeça da mulher ou será da criatura rola pelo chão e '
                                  'seu sangue deixou seu corpo e sua espada encharcados... ')
                            sleep(tempo)
                            print('Quando você olha pra sua espada percebe que ela está se '
                                  'dissolvendo, o sangue da criatura era um ácido extremamente letal!')
                            sleep(tempo)
                            print('Já é tarde demais pra se salvar, o sangue dela queima sua pele, '
                                  'seu maior arrenpedimento vai ser não ter  feito as coisas diferentes, '
                                  'você morrera sem se lembrar de nada.')
                            sleep(tempo)
                            componentes.final_incompleto(nome_player, tempo)

# REDFLAG: final da terceira rota.

                        elif acao == '2':
                            sleep(tempo)
                            print('Ela está falando algo muito baixo...')
                            sleep(tempo)
                            print('Você se aproxima lentamente, com cautela, '
                                  'qualquer movimento errado pode significar sua morte.')
                            sleep(tempo)
                            print('Finalmente você é capaz de ouvir os lamentos'
                                  ' da pobre criatura em seus últimos suspiros')
                            sleep(tempo)
                            print('\n"- Você tomou a decisão correta, e a partir de agora colherá '
                                  'os frutos de sua coragem, eu te aprovo, meu caro principe".')
                            sleep(tempo)
                            print('\n"- Que as trevas te acompanhem, que os ventos do norte te guiem e que meus irmãos')
                            sleep(tempo)
                            print('e irmãs de sangue sejam seu súditos fieis e te ajudem a '
                                  'erguer o tão esperado reinado dos monstros."\n')
                            sleep(tempo)
                            print('Ao terminar de falar, ela cita seu próprio nome... Acylla... '
                                  'uma forma de maldição antiga e aprisionamento de sua alma.')
                            sleep(tempo)
                            print('Enquanto você viver, de hoje em diante só lhe restará mal em seu caminho.')
                            sleep(tempo)
                            print('Seu destino então foi selado...')
                            sleep(tempo)
                            print('Desde então inúmeros monstros juraram lealdade a sua linhagem, '
                                  'com o passar do tempo o número só aumentava.')
                            sleep(tempo)
                            print('Uma horda de monstros ao seu redor foi dominando os territórios, '
                                  'foram se procriando e aumentando seu reino de destruição.')
                            sleep(tempo)
                            print('Você nunca quis aquilo, mas não pode fazer nada a respeito, '
                                  'sua própria vontade estava selada na maldiçao feita com a alma e nome de Acylla.')
                            sleep(tempo)
                            print('Com mais tempo o mundo conheceu sua pior época, o reinado dos '
                                  'monstros pelo continente, liderados por você, o rei dêmonio.')
                            sleep(tempo)
                            print('Até mesmo após sua morte seu reinado continuaria '
                                  'com sua linhagem, sua vida foi prolongada pelos monstros...')
                            sleep(tempo)
                            print('Mas finalmente após milhares de anos... ')
                            componentes.final_incompleto(nome_player, tempo)

# BLACKFLAG: final da quinta rota

                    elif acao == '2':
                        sleep(tempo)
                        print('Ao mata-lá você nunca saberá o que ela estava dizendo com certeza.')
                        sleep(tempo)
                        print('Apenas imagina que seja lá o que fosse, '
                              'seria cobertor de ódio, desprezo e amargor, com certeza')
                        sleep(tempo)
                        print('Você aprendeu e sente que fez o certo, '
                              'que sangue e morte são sua única escolha, você sobriviveu aqui e agora')
                        sleep(tempo)
                        print('Seu passado e suas mémorias já não importam mais, '
                              'você vai seguir em frente e trilhar seu próprio caminho.')
                        sleep(tempo)
                        print('Você abandona o fantasma na floresta e parte para o continente para conquistar terras, '
                              'saquear e se fazer rei a qualquer custo...')
                        sleep(tempo)
                        print('Suas escolhas até aqui o tornaram o Rei Tirano...')
                        sleep(tempo)
                        print('Seu reinado de caos e dor durou sua vida inteira...')
                        sleep(tempo)
                        print('Final ruim...')
                        print('E depois de dezenas de anos finalmente...')
                        componentes.final_incompleto(nome_player, tempo)

# BLACKFLAG: final da quarta rota

elif acao == '2':
    sleep(tempo)
    print('Enquanto corre pela floresta você tropeça e caí em um ninho de cobras-trovão.')
    sleep(tempo)
    print('elas são conhecidas pelos apitos na ponta da calda que ao balançar emite o som de um trovão.')
    sleep(tempo)
    print('você está desprotegido e deixou sua espada lá trás, você é atacado e morre lentamente com o veneno.')
    sleep(tempo)
    componentes.final_incompleto(nome_player, tempo)

# REDFLAG: final da segunda rota.
