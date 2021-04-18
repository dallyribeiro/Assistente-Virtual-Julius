from forex_python.converter import CurrencyRates
from config import sai_som

def Conversor_Moedas():

    c = CurrencyRates()

    print('''
        =====================================================
        Para realizar a conversão, use os seguintes códigos:

        'EUR' - para Euros;
        'CAD' - para dólar Canadense;
        'USD' - para dólar americano;
        'BRL' - para real brasileiro;
        'GBP' - para libra;
        =====================================================
    ''')
    sai_som('''
        Para realizar a conversão, use os seguintes códigos:

        'EUR' - para Euros;
        'CAD' - para dólar Canadense;
        'USD' - para dólar americano;
        'BRL' - para real brasileiro;
        'GBP' - para libra;
    
    ''')

    actually = str(input('Qual é a moeda do seu valor? '))
    sai_som('Qual é a moeda do seu valor? ')

    valor = float(input('Qual é o seu valor? '))
    sai_som('Qual é o seu valor? ')

    final = str(input('Qual é a sua moeda final? '))
    sai_som('Qual é a sua moeda final? ')

    convert = c.convert(actually, final, valor)

    print(f'{valor} {actually} são {convert:.2f} {final}. ')
    sai_som(f'{valor} {actually} são {convert:.2f} {final}. ')
