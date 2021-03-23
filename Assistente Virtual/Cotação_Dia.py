import requests
import json

requisição = requests.get('https://economia.awesomeapi.com.br/all')

cotação = requisição.json()

Valor_moeda = input('Qual o valor da moeda?: ')

if Valor_moeda == ('Dolar'):
    print('#### Cotação do Dolar ####')

    print('Moeda: ' + cotação ['USD'] ['name'])
    print('Data: ' + cotação ['USD'] ['create_date'])
    print('Valor Atual R$: ' + cotação ['USD']['bid'])

elif Valor_moeda == ('Euro'):
    print('#### Cotação do Euro ####')

    print('Moeda: ' + cotação ['EUR'] ['name'])
    print('Data: ' + cotação ['EUR'] ['create_date'])
    print('Valor Atual R$: ' + cotação ['EUR'] ['bid'])

elif Valor_moeda == ('Libra'):
    print('#### Cotação do Libra ####')

    print('Moeda: ' + cotação ['GBP'] ['name'])
    print('Data: ' + cotação ['GBP'] ['create_date'])
    print('Valor Atual R$: ' + cotação['GBP'] ['bid'])

elif Valor_moeda == ('Bitcoin'):
    print('#### Cotação do Bitcoin ####')
    
    print('Moeda: ' + cotação ['BTC'] ['name'])
    print('Data: ' + cotação ['BTC'] ['create_date'])
    print('Valor Atual R$: ' + cotação ['BTC'] ['bid'])



