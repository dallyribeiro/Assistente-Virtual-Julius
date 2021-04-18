from config import sai_som

def metas():

   sai_som('Quanto deseja investir? ')
   num1 = float(input('Quanto deseja investir?'))

   sai_som('Quanto deseja alcançar? ')
   num2 = float(input('Quanto deseja alcançar?'))

   Vf=  num2 / num1
   print(f'Você vai alcançar R${num2:.2f} em cerca de {Vf:.2f} meses se investir R${num1:.2f} por mês! ')
   sai_som(f'Você vai alcançar R${num2:.2f} em cerca de {Vf:.2f} meses se investir R${num1:.2f} por mês! ')














