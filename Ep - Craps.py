#Importando bibliotecas necessarias

import random
#Declarando as condições iniciais

dinheiro = 100
i = 0
Lista_Field = [3,4,9,10,11]
lista_AC = [2,3,12]
Lista_perde_PLB = [2,3,12]
Lista_ganha_PLB = [7,11]
Lista_Point = [4,5,6,8,9,10]

#While que declara que so pode apostar se tiver dinheiro

while(dinheiro > 0):
    print('Você tem {0} dinheiros.'.format(dinheiro))
    
# Pergutnando se deseja apostar ou parar de jogar

    escolha1 = str(input('Deseja sair ou apostar?(Digite apostar ou sair) '))
    
#Se escolher apostar, ele entra no if
    
    if escolha1 == 'apostar':
        print('Fase Come Out')
        
# Pergunta no que deseja apostar
        if dinheiro >0:
            Field = str(input('Deseja apostar em Field? (s/n) '))
            if Field == 's':
                aposta1 = int(input('Quanto deseja apostar? '))
                dados1 = random.randint(2,12)
                print('Seus dados foram {0}.'.format(dados1))
                if dados1 in Lista_Field:
                    print('Você ganhou {0}.'.format(aposta1))
                    dinheiro += aposta1
                elif dados1 == 2:
                    print('Você ganhou o dobro do que apostou.')
                    dinheiro += 2 * aposta1
                elif dados1 == 12:
                    print('Você ganhou o triplo do que apostou!')
                    dinheiro += 3 * aposta1
                else:
                    print('Você perdeu {0}.'.format(aposta1))
                    dinheiro = dinheiro - aposta1
            print('Você tem {0} dinheiros.'.format(dinheiro))
        else:
            break
            print("Acabou seu dinheiro, Você perdeu!")
# Pergunta no que deseja apostar
        if dinheiro >0:
            Any_Craps = str(input('Deseja apostar em Any Craps? (s/n) '))
            if Any_Craps == 's':
                aposta2 = int(input('Quanto deseja apostar? '))
                dados2 = random.randint(2,12)
                print('Seus dados foram {0}.'.format(dados2))
                if dados2 in lista_AC:
                    print('Você ganhou 7 vezes o que apostou!')
                    dinheiro += 7 * aposta2
                else:
                    print('Você perdeu {0}.'.format(aposta2))
                    dinheiro = dinheiro - aposta2
            print('Você tem {0} dinheiros.'.format(dinheiro))
        else:
            break
            print("Acabou seu dinheiro, Você perdeu!")
        
# Pergunta no que deseja apostar
        if dinheiro >0:
            Twelve = str(input('Deseja apostar em Twelve? (s/n) '))
            if Twelve == 's':
                aposta3 = int(input('Quanto deseja apostar? '))
                dados3 = random.randint(2,12)
                print('Seus dados foram {0}.'.format(dados3))
                if dados3 == 12:
                    print('Você ganhou 12 vezes o que apostou!')
                    dinheiro += 12 * aposta3
                else:
                    print('Você perdeu {0}.'.format(aposta3))
                    dinheiro -= aposta3
            print('Você tem {0} dinheiros'.format(dinheiro))
        else:
            break
            print("Acabou seu dinheiro, Você perdeu!")
        
# Pergunta no que deseja apostar    
        if dinheiro >0:
            PLB = str(input('Deseja apostar em Pass Line Bet? (s/n) '))
            if PLB == 's':
                aposta4 = int(input('Quanto deseja apostar? '))
                dados4 = random.randint(2,12)
                print('Seus dados foram {0}.'.format(dados4))
                if dados4 in Lista_ganha_PLB:
                    print('Você ganhou {0}.'.format(aposta4))
                    dinheiro += aposta4
                elif dados4 in Lista_perde_PLB:
                    print('Você perdeu {0}.'.format(aposta4))
                    dinheiro = dinheiro - aposta4
                elif dados4 in Lista_Point:
                    print('Como seus dados foram {0} você entrou no Point.'.format(dados4))
                    print('A aposta continua a mesma e você pode apostar em outros tipos de apostas.')
                    dados_point = random.randint(2,12)
                    while(dados4 != dados_point and dados4 != 7):

                    
# Pergunta se deseja apostar ou entrar no point
                    
                        escolha2 = str(input('Quer apostar em Field, Any Crap, twelve ou deseja ir para o Point? digite apostar ou Point:'))
                        if escolha2 == 'apostar':
                            print('Você tem {0} dinheiros, o que foi apostado no Point nao é contabilizado'.format(dinheiro))
                            print('Responda todas as perguntas com s ou n, menos as de aposta')
                            Field = str(input('Deseja apostar em Field? '))
                            if Field == 's':
                                aposta5 = int(input('Quanto quer apostar? '))
                                dados5 = random.randint(2,12)
                                print('Seus dados foram {0}.'.format(dados5))
                                if dados5 in Lista_Field:
                                    print('Você ganhou {0}.'.format(aposta5))
                                    dinheiro += aposta5
                                elif dados5 == 2:
                                    print('Você ganhou o dobro')
                                    dinheiro += 2 * aposta5
                                elif dados5 == 12:
                                    print('Você ganhou o triplo!')
                                    dinheiro += 3 * aposta5
                                else:
                                    print('Você perdeu {0}.'.format(aposta5))
                                    dinheiro = dinheiro - aposta5
                            print('Você tem {0} dinheiros.'.format(dinheiro))
                            Any_Craps = str(input('Deseja apostar em Any Craps? (s/n) '))
                            if Any_Craps == 's':
                                aposta6 = int(input('Quanto deseja apostar? '))
                                dados6 = random.randint(2,12)
                                print('Seus dados foram {0}.'.format(dados6))
                                if dados6 in lista_AC:
                                    print('Você ganhou 7 vezes!')
                                    dinheiro += 7 * aposta6
                                else:
                                    print('Você perdeu {0}.'.format(aposta6))
                                    dinheiro = dinheiro - aposta6
                            print('Você tem {0} dinheiros.'.format(dinheiro))
                            Twelve = str(input('Deseja apostar em Twelve? (s/n) '))
                            if Twelve == 's':
                                aposta7 = int(input('Quanto deseja apostar? '))
                                dados7 = random.randint(2,12)
                                print('Seus dados foram {0}.'.format(dados7))
                                if dados7 == 12:
                                    print('Você ganhou 12 vezes o que apostou!')
                                    dinheiro += 12 * aposta7
                                else:
                                    print('Você perdeu{0}.'.format(aposta7))
                                    dinheiro = dinheiro - aposta7
                                
# Entra no modo de Point
                                
                        else:
                            print('Começa o Point, novos dados serão rodados ate sair {0} (seu número anterior) ou 7.'.format(dados4))
                            dados_point = random.randint(2,12)
                            print('Seus novos dados foram {0}.'.format(dados_point))
                            if dados_point == dados4:
                                print('Os dados foram iguais aos anteriores, você ganhou o Point.')
                                dinheiro += aposta4
                                break
                            elif dados_point == 7:
                                dinheiro = dinheiro - aposta4
                                print('Os dados foram iguais a 7, você perdeu o Point.')
                                break
        else:
            break
            print("Acabou seu dinheiro, Você perdeu!")
#Se desejar sair em vez de apostar o programa fecha.
                
    else:
        break
        print('Você tem {0} dinheiros.'.format(dinheiro))
        
#se o dinheiro for menor ou igual a 0, não é possivel apostar mais.
        
else:
    print ("Você não tem saldo para apostar")
    
