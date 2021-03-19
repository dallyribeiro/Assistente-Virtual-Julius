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


def verifica_nome(user_name):
    if user_name.startswish('Meu nome é'):
        user_name = user_name.replace('Meu nome é','')

    if user_name.startswish('Eu me chamo'):
        user_name = user_name.replace('Eu me chamo','')

    if user_name.startswish('Eu sou o'):
        user_name = user_name.replace('Eu sou o','')

    if user_name.startswish('Eu sou a'):
        user_name = user_name.replace('Eu sou a','')
    
    return user_name

def verifica_nome_exist(nome):
    dados = open('dados/nome.txt', 'r')
    nome_list = dados.readlines()

    if not nome_list:
        vazio = open('dados/nome.txt', 'r')
        conteudo = vazio.readlines()
        conteudo.append('{}'.format(nome))
        vazio = open('dados/nome.txt', 'w')
        vazio.writelines(conteudo)
        vazio.close()
        return 'Olá, {}, prazer em te conhecer! Vamos economizar?'.format(nome)

    for linha in nome_list:
        if linha == nome:
            return f'Olá {nome}, acho que já nos conhecemos'

    vazio = open('dados/nome.txt', 'r')
    conteudo = vazio.readlines()
    conteudo.append('\n{}'.format(nome))
    vazio = open('dados/nome.txt', 'w')
    vazio.writelines(conteudo)
    vazio.close()

    return f'Oi {nome}, é a primeira vez que nos falamos!'

def name_list():
    try:
        nomes = open('dados/nome.txt', 'r')
        nomes.close()
    except FileNotFoundError:
        nomes = open('dados/nome.txt', 'w')
        nomes.close()

def Conversor_Moedas(entrada):
    print('Qual a moeda do seu valor?')
    sai_som('Qual a moeda do seu valor?')
    
    if 'Real' or 'Reais' in entrada:
        print('Qual o valor que quer converter?')
        sai_som('Qual o valor que quer converter?')
        
    