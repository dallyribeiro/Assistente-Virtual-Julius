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

resposta_erro_aleatoria = choice(lista_erros)
rec = sr.Recognizer()








def calculadora():

    print('Quanto você tem para investir no momento?')
    sai_som('Quanto você tem para investir no momento?')

    while True:
        # resposta_erro_aleatoria = choice(lista_erros)
        # rec = sr.Recognizer()

        with sr.Microphone() as s:  # Para usar o microfone
            rec.adjust_for_ambient_noise(s)

            while True:
                try:
                    audio = rec.listen(s)
                    valor_inicial = rec.recognize_google(audio, language='pt')
                    valor_inicial = float(valor_inicial)
                    print(valor_inicial)
                    break
                except sr.UnknownValueError:
                    sai_som(resposta_erro_aleatoria)


                print('Quanto investirá por mês?')
                sai_som('Quanto investirá por mês?')

                while True:
                    # resposta_erro_aleatoria = choice(lista_erros)
                    # rec = sr.Recognizer()

                    with sr.Microphone() as s: #Para usar o microfone
                       rec.adjust_for_ambient_noise(s)

                       while True:
                           try:
                              audio = rec.listen(s)
                              aporte = rec.recognize_google(audio, language ='pt')
                              aporte = float(aporte)
                              print(aporte)
                              break
                           except sr.UnknownValueError:
                              sai_som(resposta_erro_aleatoria)

                       print('Qual a taxa de rendimento mensal, em porcentagem?')
                       sai_som('Qual a taxa de rendimento mensal, em porcentagem?')
                       while True:
                              # resposta_erro_aleatoria = choice(lista_erros)
                              # rec = sr.Recognizer()

                              with sr.Microphone() as s:  # Para usar o microfone
                                 rec.adjust_for_ambient_noise(s)


                                 while True:
                                    try:
                                        audio = rec.listen(s)
                                        taxa_porc = rec.recognize_google(audio, language='pt')
                                        taxa_porc = float(taxa_porc)
                                        print(taxa_porc)
                                        break
                                    except sr.UnknownValueError:
                                        sai_som(resposta_erro_aleatoria)

                                    print('Em quanto meses pretende resgatar seu investimento?')
                                    sai_som('Em quanto meses pretende resgatar seu investimento?')

                                    while True:
                                        # resposta_erro_aleatoria = choice(lista_erros)
                                        # rec = sr.Recognizer()

                                        with sr.Microphone() as s:  # Para usar o microfone
                                            rec.adjust_for_ambient_noise(s)

                                            while True:
                                                try:
                                                    audio = rec.listen(s)
                                                    mes = rec.recognize_google(audio, language='pt')
                                                    mes = int(mes)
                                                    print(mes)
                                                    break
                                                except sr.UnknownValueError:
                                                    sai_som(resposta_erro_aleatoria)


                                                taxa = (taxa_porc / 100)
                                                ##o calculo a seguir se refere a um aporte mensal de dinheiro
                                                result_aporte = aporte * (((1 + taxa) ** mes) - 1) / taxa
                                                ##já esse cálculo é o de juros compostos, considerando o investimento de um valor inicial e resgate em alguns meses.
                                                result_vinicial = valor_inicial * ((1 + taxa) ** mes)
                                                valor_final = result_aporte + result_vinicial
                                                print(f'O total acumulado será de {valor_final:.2f} reais')
                                                sai_som(f'O total acumulado será de {valor_final:.2f} reais')

                                                # except sr.UnknownValueError:
                                                #     sai_som(resposta_erro_aleatoria)


