#Pergunta para o cliente

def codigo():
    cod_acao = str(input('De qual empresa deseja saber o código de ação? '))

    #Imprimi o valor e printa o código de ação
    if cod_acao == ('Netflix'):
        print('NFLX34')

    elif cod_acao == ('Itaú'):
        print('O código de ação dessa empresa é: ITUB3F')

    elif cod_acao == ('Vale'):
        print('O código de ação dessa empresa é: VALE5')

    elif cod_acao == ('Petrobras'):
        print('O código de ação dessa empresa é: PETR4F')

    elif cod_acao == ('Facebook'):
        print('O código de ação dessa empresa é: FB')
