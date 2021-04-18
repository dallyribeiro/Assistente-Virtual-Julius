from config import sai_som, lista_erros
from random import choice

def calculadora():
    resposta_erro_aleatoria = choice(lista_erros)
    try:

        sai_som('Qual o valor inicial que você investirá?')
        valor_inicial = float(input('Qual o valor inicial que você investirá?'))

        sai_som('Quanto investirá por mês?')
        aporte = float(input('Quanto investirá por mês?'))

        sai_som('Qual a taxa de rendimento mensal, em %?')
        taxa_porc = float(input('Qual a taxa de rendimento mensal, em %?'))

        sai_som('Em quanto meses pretende resgatar seu investimento?')
        mes = int(input('Em quanto meses pretende resgatar seu investimento?'))

        taxa = taxa_porc/100
        ##o calculo a seguir se refere a um aporte mensal de dinheiro
        result_aporte = aporte*(((1+taxa)**mes)-1)/taxa
        ##já esse cálculo é o de juros compostos, considerando o investimento de um valor inicial e resgate em alguns meses.
        result_vinicial = valor_inicial*((1+taxa)**mes)
        valor_final = result_aporte + result_vinicial
        print(f'O total acumulado será de {valor_final:.2f} reais')
        sai_som(f'O total acumulado será de {valor_final:.2f} reais')
                        

    except: 
        sai_som(resposta_erro_aleatoria)
