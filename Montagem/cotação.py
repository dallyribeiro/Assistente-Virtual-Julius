from config import sai_som 
import requests
import json

requisição = requests.get('https://economia.awesomeapi.com.br/all')

cotação = requisição.json()
def cotacao():
    print('''
        =====================================================
        Bem-vindo(a) a cotação do dia!
        Atualmente temos o valor atual das seguintes moedas:
        Dólar (Comércial americano) - Euro - Libra e Bitcoin!
        =====================================================
    ''')
    sai_som('''
        Bem-vindo(a) a cotação do dia!
        Atualmente temos o valor atual das seguintes moedas:
        Dólar (Comércial americano) - Euro - Libra e Bitcoin!
    ''')
    Valor_moeda = str(input('Qual a moeda que deseja cotação?: ')).strip().upper()

    if Valor_moeda == 'DOLAR':
        print('#### Cotação do Dolar ####')
        
        print('Moeda: ' + cotação ['USD'] ['name'])

        print('Data: ' + cotação ['USD'] ['create_date'])

        print('Valor Atual R$: ' + cotação ['USD']['bid'])
        #####################################################
        sai_som('Cotação do Dolar')
        
        sai_som('Moeda: ' + cotação ['USD'] ['name'])

        sai_som('Data: ' + cotação ['USD'] ['create_date'])

        sai_som('Valor Atual R$: ' + cotação ['USD']['bid'])

        
    if Valor_moeda == 'EURO':
        print('#### Cotação do Euro ####')

        print('Moeda: ' + cotação ['EUR'] ['name'])

        print('Data: ' + cotação ['EUR'] ['create_date'])

        print('Valor Atual R$: ' + cotação ['EUR'] ['bid'])
        #####################################################
        sai_som('Cotação do Euro')

        sai_som('Moeda: ' + cotação ['EUR'] ['name'])

        sai_som('Data: ' + cotação ['EUR'] ['create_date'])
        
        sai_som('Valor Atual R$: ' + cotação ['EUR'] ['bid'])
        
    if Valor_moeda == 'LIBRA':
        print('#### Cotação do Libra ####')

        print('Moeda: ' + cotação ['GBP'] ['name'])

        print('Data: ' + cotação ['GBP'] ['create_date'])

        print('Valor Atual R$: ' + cotação['GBP'] ['bid'])
        #####################################################
        sai_som('Cotação do Libra')

        sai_som('Moeda: ' + cotação ['GBP'] ['name'])

        sai_som('Data: ' + cotação ['GBP'] ['create_date'])
        
        sai_som('Valor Atual R$: ' + cotação['GBP'] ['bid'])

        
    if Valor_moeda == 'BITCOIN':
        print('#### Cotação do Bitcoin ####')
        
        print('Moeda: ' + cotação ['BTC'] ['name'])

        print('Data: ' + cotação ['BTC'] ['create_date'])

        print('Valor Atual R$: ' + cotação ['BTC'] ['bid'])
        #####################################################
        sai_som('Cotação do Bitcoin')
        
        sai_som('Moeda: ' + cotação ['BTC'] ['name'])

        sai_som('Data: ' + cotação ['BTC'] ['create_date'])

        sai_som('Valor Atual R$: ' + cotação ['BTC'] ['bid'])

        
    else:
        print('Moeda não cadastrada!')
        sai_som('Moeda não cadastrada!')
