import random
dinheiro = 100
i = 0
Lista_Field = [3,4,9,10,11]
lista_AC = [2,3,12]
Lista_perde_PLB = [2,3,12]
Lista_ganha_PLB = [7,11]
Lista_Point = [4,5,6,8,9,10]

while(dinheiro > 0):
    print('Você tem {0} dinheiros'.format(dinheiro))
    escolha1 = input('Deseja sair ou apostar?')
    if escolha1 == 'apostar':
        print('Fase Come Out')
        print('Responda todas as perguntas com s ou n, menos as de aposta')
        Field = input('Deseja apostar em Field?')
        if Field == 's':
            aposta1 = int(input('Quanto deseja apostar?'))
            dados1 = random.randint(2,12)
            print('Seus dados foram {0}'.format(dados1))
            if dados1 in Lista_Field:
                print('Você ganhou {0}'.format(aposta1))
                dinheiro += aposta1
            elif dados1 == 2:
                print('Você ganhou o dobro do que apostou')
                dinheiro += 2 * aposta1
            elif dados1 == 12:
                print('Você ganhou o triplo do que apostou!')
                dinheiro += 3 * aposta1
            else:
                print('Você perdeu')
                dinheiro = dinheiro - aposta1
        print('Você tem {0} dinheiros'.format(dinheiro))
        Any_Craps = input('Deseja apostar em Any Craps?')
        if Any_Craps == 's':
            aposta2 = int(input('Quanto deseja apostar?'))
            dados2 = random.randint(2,12)
            print('Seus dados foram {0}'.format(dados2))
            if dados2 in lista_AC:
                print('Você ganhou 7 vezes o que apostou!')
                dinheiro += 7 * aposta2
            else:
                print('Você perdeu')
                dinheiro = dinheiro - aposta2
        print('Você tem {0} dinheiros'.format(dinheiro))
        Twelve = input('Deseja apostar em Twelve?')
        if Twelve == 's':
            aposta3 = int(input('Quanto deseja apostar?'))
            dados3 = random.randint(2,12)
            print('Seus dados foram {0}'.format(dados3))
            if dados3 == 12:
                print('Você ganhou 12 vezes o que apostou!')
                dinheiro += 12 * aposta3
            else:
                print('Você perdeu')
                dinheiro -= aposta3
        print('Você tem {0} dinheiros'.format(dinheiro))
        PLB = input('Deseja apostar em Pass Line Bet?')
        if PLB == 's':
            aposta4 = int(input('Quanto deseja apostar?'))
            dados4 = random.randint(2,12)
            print('Seus dados foram {0}'.format(dados4))
            if dados4 in Lista_ganha_PLB:
                print('Você ganhou')
                dinheiro += aposta4
            elif dados4 in Lista_perde_PLB:
                print('Você perdeu')
                dinheiro = dinheiro - aposta4
            elif dados4 in Lista_Point:
                print('Como seus dados foram 4 você entrou no Point.')
                print('a aposta continua a mesma e você pode apostar em outros tipos de apostas.')
                escolha2 = input('Quer apostar em Field, Any Crap, twelve ou deseja ir para o Point? digite apostar ou Point')
                if escolha2 == 'apostar':
                    dinheiro2 = dinheiro - aposta4
                    print('Você tem {0} dinheiros, o que foi apostado no Point nao é contabilizado'.format(dinheiro2))
                    print('Responda todas as perguntas com s ou n, menos as de aposta')
                    Field = input('Deseja apostar em Field?')
                    if Field == 's':
                        aposta5 = int(input('Quanto quer apostar?'))
                        dados5 = random.randint(2,12)
                        print('Seus dados foram {0}'.format(dados5))
                        if dados5 in Lista_Field:
                            print('Você ganhou')
                            dinheiro += aposta5
                        elif dados5 == 2:
                            print('Você ganhou o dobro')
                            dinheiro += 2 * aposta5
                        elif dados5 == 12:
                            print('Você ganhou o triplo!')
                            dinheiro += 3 * aposta5
                        else:
                            print('Você perdeu')
                            dinheiro = dinheiro - aposta5
                    print('Você tem {0} dinheiros'.format(dinheiro2))
                    Any_Craps = input('Deseja apostar em Any Craps?')
                    if Any_Craps == 's':
                        aposta6 = int(input('Quanto deseja apostar?'))
                        dados6 = random.randint(2,12)
                        print('Seus dados foram {0}'.format(dados6))
                        if dados6 in lista_AC:
                            print('Você ganhou 7 vezes!')
                            dinheiro += 7 * aposta6
                        else:
                            print('Você perdeu')
                            dinheiro = dinheiro - aposta6
                    print('Você tem {0} dinheiros'.format(dinheiro2))
                    Twelve = input('Deseja apostar em Twelve?')
                    if Twelve == 's':
                        aposta7 = int(input('Quanto deseja apostar?'))
                        dados7 = random.randint(2,12)
                        print('Seus dados foram {0}'.format(dados7))
                        if dados7 == 12:
                            print('Você ganhou 12 vezes o que apostou!')
                            dinheiro += 12 * aposta7
                        else:
                            print('Você perdeu')
                            dinheiro = dinheiro - aposta7
                else:
                    print('Começa o Point, novos dados serão rodados ate sair {0} (seu número anterior) ou 7'.format(dados4))
                    dados_point = random.randint(2,12)
                    while(dados4 != dados_point and dados4 != 7):
                        print('Seus novos dados foram {0}'.format(dados_point))
                        if dados_point == dados4:
                            print('Os dados foram iguais aos anteriores, você ganhou o Point')
                            dinheiro += aposta4
                        elif dados_point == 7:
                            print('Os dados foram iguais a 7, você perdeu o Point')
                            dinheiro = dinheiro - aposta4
                        else:
                            print('Rolaremos seus dados novamente')
                            dados_point = random.randint(2,12)
    else:
        break
        
        