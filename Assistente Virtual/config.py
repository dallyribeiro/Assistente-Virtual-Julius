from random import choice
import speech_recognition as sr
import pyttsx3

version = '1.0'

def intro():
    msg = 'Assistente - version {} / by'.format(version)
    print('-' * len(msg) + '\n{}\n'.format(msg) + '-' * len(msg) )


lista_erros = [
        'Não entendi nada, repita',
        'Esse erro me custou R$0,97 centavos',
        'Sempre que você errar a fala\n EU VOU ESTAR LÁ\n'

]

conversas = {
    'Olá' : 'Oi, tudo bem?',
    'Tudo, e você?' : 'Estou bem, obrigado'

}

comandos = {
    'Desligar' : 'Desligando',
    'Reiniciar' : 'Reiniciando'

}
reproducao = pyttsx3.init()

def sai_som(resposta):
    reproducao.say(resposta)
    reproducao.runAndWait()

def Conversor_Moedas(entrada):

    print('Qual a moeda do seu valor?')
    sai_som('Qual a moeda do seu valor?')
    
    while True:
            resposta_erro_aleatoria = choice(lista_erros)
            rec = sr.Recognizer()

            with sr.Microphone() as s: #Para usar o microfone
                rec.adjust_for_ambient_noise(s)

                while True:
                    try:
                        audio = rec.listen(s)
                        entrada = rec.recognize_google(audio, language ='pt')
                        #REAIS PARA:
                        if 'Real' or 'Reais' in entrada:
                            real = float(input('Qual o valor que quer converter?'))
                            sai_som('Qual o valor que quer converter?')
                            audio = rec.listen(s)
                            real = rec.recognize_google(audio, language='pt')
                            print('Qual é a moeda para qual quer converter?')
                            sai_som('Qual é a moeda para qual quer converter:?')
                            audio = rec.listen(s)
                            entrada = rec.recognize_google(audio, language='pt')
                            
                            #REAIS PARA DOLAR
                            if 'Dólar' or 'Dólares' in entrada:
                                dolar = real / 5.56
                                print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
                                sai_som('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))

                            #REAL PARA EURO
                            if 'Euro' or 'Euros' in entrada:
                                euro = real / 6.62
                                print('Com R${:.2f} você pode comprar €{:.2f}'.format(real, euro))
                                sai_som('Com R${:.2f} você pode comprar €{:.2f}'.format(real, euro))
                            #REAIS PARA LIBRA
                            if 'Libra' or 'Libras' in entrada:            
                                libra = real / 7.73
                                print('Com R${:.2f} você pode comprar £{:.2f}'.format(real, libra))
                                sai_som('Com R${:.2f} você pode comprar £{:.2f}'.format(real, libra))

                        #DÓLAR PARA:
                        if 'Dólar' or 'Dólares' in entrada:
                            dolar = float(input('Qual o valor que quer converter?'))
                            sai_som('Qual o valor que quer converter?')                         
                            print('Qual é a moeda para qual quer converter?')
                            sai_som('Qual é a moeda para qual quer converter:?')
                            
                            if 'Real' or 'Reais' in entrada:
                                real = dolar / 0.18
                                print('Com U${:.2f} você pode comprar R${:.2f}'.format(dolar, real))
                                sai_som('Com U${:.2f} você pode comprar R${:.2f}'.format(dolar, real))
                            
                            if 'Euro' or 'Euros' in entrada:
                                euro = dolar / 0.84
                                print('Com US${:.2f} você pode comprar €{:.2f}'.format(dolar, euro))
                                sai_som('Com US${:.2f} você pode comprar €{:.2f}'.format(dolar, euro))

                            if 'Libra' or 'Libras' in entrada:  
                                libra = dolar / 0.72
                                print('Com US${:.2f} você pode comprar £{:.2f}'.format(dolar, libra))
                                sai_som('Com US${:.2f} você pode comprar £{:.2f}'.format(dolar, libra))
                        
                        #EURO PARA:
                        if 'Euro' or 'Euros' in entrada:
                            euro = float(input('Qual o valor que quer converter?'))
                            sai_som('Qual o valor que quer converter?')                         
                            print('Qual é a moeda para qual quer converter?')
                            sai_som('Qual é a moeda para qual quer converter:?')

                            if 'Real' or 'Reais' in entrada:
                                real = euro / 0.15
                                print('Com €{:.2f} você pode comprar R${:.2f}'.format(euro, real))
                                sai_som('Com €{:.2f} você pode comprar R${:.2f}'.format(euro, real))

                            if 'Libra' or 'Libras' in entrada:  
                                libra = euro / 0.86
                                print('Com €{:.2f} você pode comprar £{:.2f}'.format(euro, libra))
                                sai_som('Com €{:.2f} você pode comprar £{:.2f}'.format(euro, libra))

                            if 'Dólar' or 'Dólares' in entrada:
                                dolar = euro / 1.19
                                print('Com €{:.2f} você pode comprar US${:.2f}'.format(euro, dolar))
                                sai_som('Com €{:.2f} você pode comprar US${:.2f}'.format(euro, dolar))

                        #LIBRA PARA:    
                        if 'Libra' or 'Libras' in entrada:
                            libra = float(input('Qual o valor que quer converter?'))
                            sai_som('Qual o valor que quer converter?')                           
                            print('Qual é a moeda para qual quer converter?')
                            sai_som('Qual é a moeda para qual quer converter:?')

                            if 'Real' or 'Reais' in entrada:
                                real = libra / 0.13
                                print('Com £{:.2f} você pode comprar R${:.2f}'.format(libra, real))
                                sai_som('Com £{:.2f} você pode comprar R${:.2f}'.format(libra, real))

                            if 'Dólar' or 'Dólares' in entrada:
                                dolar = libra / 1.39
                                print('Com £{:.2f} você pode comprar US${:.2f}'.format(libra, dolar))
                                sai_som('Com £{:.2f} você pode comprar US${:.2f}'.format(libra, dolar))

                            if 'Euro' or 'Euros' in entrada:
                                euro = libra / 1.17
                                print('Com €{:.2f} você pode comprar US${:.2f}'.format(libra, euro))
                                sai_som('Com €{:.2f} você pode comprar US${:.2f}'.format(libra, euro))
                        else:
                            sai_som(resposta_erro_aleatoria)

                    except sr.UnknownValueError: 
                        sai_som(resposta_erro_aleatoria)

def Calculadora(entrada):

    print('Qual a moeda do seu valor?')
    sai_som('Qual a moeda do seu valor?')
    
    while True:
            resposta_erro_aleatoria = choice(lista_erros)
            rec = sr.Recognizer()

            with sr.Microphone() as s: #Para usar o microfone
                rec.adjust_for_ambient_noise(s)

                while True:
                    try:
                        audio = rec.listen(s)
                        entrada = rec.recognize_google(audio, language ='pt')

                        valor_inicial = float(input('Qual o valor inicial que você investirá?'))
                        sai_som('Qual o valor inicial que você investirá?')
                        aporte = float(input('Quanto investirá por mês?'))
                        sai_som('Quanto investirá por mês?')
                        taxa_porc= float(input('Qual a taxa de rendimento mensal, em %?'))
                        sai_som('Qual a taxa de rendimento mensal, em %?')
                        mes = int(input('Em quanto meses pretende resgatar seu investimento?'))
                        sai_som('Em quanto meses pretende resgatar seu investimento?')
                        taxa = taxa_porc/100
                        ##o calculo a seguir se refere a um aporte mensal de dinheiro
                        result_aporte = aporte*(((1+taxa)**mes)-1)/taxa
                        ##já esse cálculo é o de juros compostos, considerando o investimento de um valor inicial e resgate em alguns meses.
                        result_vinicial = valor_inicial*((1+taxa)**mes)
                        valor_final = result_aporte + result_vinicial
                        print(f'O total acumulado será de {valor_final:.2f} reais')
                        sai_som(f'O total acumulado será de {valor_final:.2f} reais')
                        

                    except sr.UnknownValueError: 
                        sai_som(resposta_erro_aleatoria)