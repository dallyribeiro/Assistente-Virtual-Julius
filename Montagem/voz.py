import speech_recognition as sr
import pyttsx3
from random import choice
from config import *
from calculadora import *
from Conversor import *
from cotação import *
from noticias import *
from perfil import *
from comparativo_corretoras import *
from metas import *
from codigo import*

reproducao = pyttsx3.init()

def sai_som(resposta):
    reproducao.say(resposta)
    reproducao.runAndWait()


def assistente():
    print('Oi, qual é o seu nome?')
    sai_som('Oi, qual é o seu nome?')
    while True:
            resposta_erro_aleatoria = choice(lista_erros)
            rec = sr.Recognizer()

            with sr.Microphone() as s: #Para usar o microfone
                rec.adjust_for_ambient_noise(s)

                while True: #Enquanto isso for verdadeiro, vai executar o bloco de ações abaixo
                    try:
                        audio = rec.listen(s)
                        user_name = rec.recognize_google(audio, language ='pt') 
                        print(f'Muito prazer {user_name}!')
                        sai_som(f'Muito prazer {user_name}!')
                        break
                    except sr.UnknownValueError: #Se não conseguir, retorne isso (Necessário especificar o erro)
                        sai_som(resposta_erro_aleatoria)
                break
                    

    print('=' * len(user_name))
    print('Ouvindo...') 
    sai_som('Ouvindo...')
    print('=' * len(user_name))
    while True:
            resposta_erro_aleatoria = choice(lista_erros)
            rec = sr.Recognizer()

            with sr.Microphone() as s: #Para usar o microfone
                rec.adjust_for_ambient_noise(s)

                while True: #Enquanto isso for verdadeiro, vai executar o bloco de ações abaixo
                    try:
                        audio = rec.listen(s)
                        entrada = rec.recognize_google(audio, language ='pt')
                        print('{}: {}'.format(user_name, entrada))

                        #Conversor de moedas(Real, Dólar, Euro e Libra) (1)
                        if 'conversor' in entrada:
                            entrada = entrada.replace('Conversor',' ')
                            resposta = Conversor_Moedas()
                            print('Assistente:{}'.format(resposta))
                            sai_som('{}'.format(resposta))       
                            
                        #Calculadora de Juros Compostos (2)
                        if 'calculadora' in entrada:
                            entrada = entrada.replace('Calculadora', ' ')
                            resposta = calculadora()
                            print('Assistente:{}'.format(resposta))
                            sai_som('{}'.format(resposta))
                            
                        #Cotação do dia (3)
                        if 'cotação' in entrada:
                            entrada = entrada.replace('cotação', ' ')
                            resposta = cotacao()
                            print('Assistente:{}'.format(resposta))
                            sai_som('{}'.format(resposta))

                        #Últimas notícias da investing (4)
                        if 'notícias' in entrada:
                            entrada = entrada.replace('noticias', ' ')
                            resposta = informacoes()
                            print('Assistente:{}'.format(resposta))
                            sai_som('{}'.format(resposta))

                        #Traçar perfil do usuário (5)
                        if 'perfil' in entrada:
                            entrada = entrada.replace('perfil', ' ')
                            resposta = perfil()
                            print('Assistente:{}'.format(resposta))
                            sai_som('{}'.format(resposta))

                        #Codigo
                        if 'código' in entrada:
                            entrada = entrada.replace('codigo', ' ')
                            resposta = codigo()
                            print('Assistente:{}'.format(resposta))
                            sai_som('{}'.format(resposta))

                        #Comparativo entre duas corretoras (6)
                        if 'comparativo' in entrada:
                            entrada = entrada.replace('comparativo', ' ')
                            resposta = comparativo()
                            print('Assistente:{}'.format(resposta))
                            sai_som('{}'.format(resposta))
                        
                        #Metas
                        if 'metas' in entrada:
                            entrada = entrada.replace('metas', ' ')
                            resposta = metas()
                            print('Assistente:{}'.format(resposta))
                            sai_som('{}'.format(resposta))
                        else:
                            resposta = conversas[entrada]

                        print('Assistente:{}'.format(resposta))
                        sai_som('{}'.format(resposta))                                               
                    
                    except sr.UnknownValueError: #Se não conseguir, retorne isso (Necessário especificar o erro)
                        sai_som(resposta_erro_aleatoria)
                    
               
if __name__ == '__voz__':
    intro()
    sai_som('Iniciando')
    assistente()
assistente()

               

            

                



    
   
