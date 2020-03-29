import random
dinheiro = 100
i = 0
whilhe(dinheiro > 0):
    print('Você tem {0}'.format(dinheiro))
    escolha = input('quer sair ou apostar?')
    if escolha == 'apostar':
        print('Fase de Come Out')
        print('responda com s ou n')
        Field = input('deseja apostar em Field?)
        if Field == 's':
            aposta1 = input('Quanto quer apostar?')
            dados1 = random.randint(2,12)
            if dados1 == 3:
                print('Ganhou')
                dinheiro += aposta1
            elif dados1 == 4:
                print('Ganhou')
                dinheiro += aposta1
            elif dados1 == 9:
                print('Ganhou')
                dinheiro += aposta1
            elif dados1 == 10:
                print('Ganhou')
                dinheiro += aposta1
            elif dados1 == 11:
                print('Ganhou')
                dinheiro += aposta1
            elif dados1 == 2:
                print('Ganhou o dobro')
                dinheiro += 2 * aposta1
            elif dados1 == 12:
                print('Ganhou o triplo')
                dinheiro += 3 * aposta1
            else:
                print('Perdeu')
                dinheiro = dinheiro - aposta1
        Any_Craps = input('deseja apostar em Any Craps?)
        if Any_Craps == 's':
            aposta2 = input('Quanto quer apostar?')
            dados2 = random.randint(2,12)
            if dados2 == 2:
                print('Ganhou 7 vezes')
                dinheiro += 7 * aposta2
            elif dados2 == 3:
                print('Ganhou 7 vezes')
                dinheiro += 7 * aposta2
            elif dados2 == 12:
                print('Ganhou 7 vezes')
                dinheiro += 7 * aposta2
            else:
                print('Perdeu')
                dinheiro = dinheiro - aposta
        Twelve = input('deseja apostar em Twelve?)
        if Twelve == 's':
            aposta3 = input('Quanto quer apostar?')
            dados3 = random.randint(2,12)
            if dados3 == 12:
                print('ganhou 12 vezes!')
                dinheiro += 12 * aposta3
        PLB = input('deseja apostar em Pass Line Bet?)
        if PLB == 's':
            aposta4 = input('Quanto quer apostar?')
            dados4 = random.randint(2,12)
            if dados4 == 7:
                print('Ganhou')
                dinheiro += aposta4
            elif dados4 == 11:
                print('Ganhou')
                dinheiro += aposta4
            elif dados4 == 2:
                print('Perdeu')
                dinheiro = dinheiro - aposta4
            elif dados4 == 3:
                print('Perdeu')
                dinheiro = dinheiro - aposta4
            elif dados4 == 12:
                print('Perdeu')
                dinheiro = dinheiro - aposta4
            elif dados4 == 4:
                print('Entrou no Point, a aposta continua a mesma')
                dados_point = random.randint(2,12)
                if dados_point == dados4:
                    print('Os dados foram iguais, ganhou o mesmo tanto que apostou')
                    dinheiro += aposta4
                elif dados_point == 7:
                    print('Perdeu")
                    dinheiro = dinheiro - aposta4
    else:
        break
        
        