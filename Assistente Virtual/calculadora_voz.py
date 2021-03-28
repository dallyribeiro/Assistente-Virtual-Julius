import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
def ouvir_microfone():
    # Habilita o microfone do usuário
    microfone = sr.Recognizer()

    with sr.Microphone() as source:

        # Chama um algoritmo de reducao de ruidos no som
        microfone.adjust_for_ambient_noise(source)

        # # Frase para o usuario dizer algo
        # print("Diga alguma coisa: ")

        # Armazena o que foi dito numa variavel
        audio = microfone.listen(source)

    try:

        # Passa a variável para o algoritmo reconhecedor de padroes
        frase = microfone.recognize_google(audio, language='pt-BR')

        # Retorna a frase pronunciada
        print("Você disse: " + frase)

    # Se nao reconheceu o padrao de fala, exibe a mensagem
    except sr.UnkownValueError:
        print("Não entendi")

    return (frase)

def calculadora_():
    print('Qual valor inicial que você investirá')
    valor_inicial = float(ouvir_microfone())
    print(valor_inicial)
    print('Quanto investirá por mês')
    aporte = float(ouvir_microfone())
    print(aporte)
    print('Qual a taxa de rendimento mensal, em %?')
    taxa_porc = float(ouvir_microfone())
    print(taxa_porc)
    print('Em quanto meses pretende resgatar seu investimento?')
    mes = int(ouvir_microfone())
    print(mes)
    taxa = taxa_porc/100
    ##o calculo a seguir se refere a um aporte mensal de dinheiro
    result_aporte = aporte*(((1+taxa)**mes)-1)/taxa
    ##já esse cálculo é o de juros compostos, considerando o investimento de um valor inicial e resgate em alguns meses.
    result_vinicial = valor_inicial*((1+taxa)**mes)
    valor_final = result_aporte + result_vinicial
    print(f'O total acumulado será de {valor_final:.2f} reais')