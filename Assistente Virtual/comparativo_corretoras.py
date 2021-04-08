import sqlite3
con = sqlite3.connect('corretoras.db')
cur = con.cursor()

corretora = input('Digite o nome da primeira corretora: ')
corretora2 = input('Digite a segunda corretora que deseja fazer comparação: ')
comparativo = input('Digite qual o quesito que você deseja comparar:  ')

dict_corretora = {
   'xp': 3,
   'itau': 114,
   'ativa': 147,
   'rico': 386,
   'bradesco': 72,
   'icap': 735,
   'easynet': 90,
   'mirae': 262,
   'banco do brasil': 820,
   'santander': 27
}

dict_fator_comparativo = {
     'segurança': 'segurança',
     'experiencia investidor': 'experiencia_investidor',
     'avaliação final': 'avaliação_final',
     'custos mensais 3': 'custos_mensais_3op',
     'custos mensais 5': 'custos_mensais_5op',
     'custos mensais 10': 'custos_mensais_10op'
}

custos_mensais= []

query_parameters = (dict_corretora[corretora.lower()], dict_corretora[corretora2.lower()])

for row in cur.execute(f'SELECT {dict_fator_comparativo[comparativo.lower()]} FROM corretoras WHERE cod_corretora == ? or cod_corretora == ?', query_parameters):
    custos_mensais.append(row[0])

print('Os dados da primeira corretota são de: {} e da segunda corretora são de: {} '.format(custos_mensais[0], custos_mensais[1]))

con.commit()
con.close()