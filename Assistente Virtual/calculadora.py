def calculadora():
    valor_inicial = float(input('Qual o valor inicial que você investirá?'))
    aporte = float(input('Quanto investirá por mês?'))
    taxa_porc= float(input('Qual a taxa de rendimento mensal, em %?'))
    mes = int(input('Em quanto meses pretende resgatar seu investimento?'))
    taxa = taxa_porc/100
    ##o calculo a seguir se refere a um aporte mensal de dinheiro
    result_aporte = aporte*(((1+taxa)**mes)-1)/taxa
    ##já esse cálculo é o de juros compostos, considerando o investimento de um valor inicial e resgate em alguns meses.
    result_vinicial = valor_inicial*((1+taxa)**mes)
    valor_final = result_aporte + result_vinicial
    print(f'O total acumulado será de {valor_final:.2f} reais')
calculadora()
