# Desenvolva um programa que receba a idade e retorne uma condicao
# 80+= idoso 18+= adulto 13+=adolescente 0+=crianca

idade = int(input('Digite a idade que deseja:  '))

if idade >= 0 and idade <= 12:
    print('Crianca')
elif(idade >= 13 and idade <= 17):
    print('Adolescente')
elif(idade >= 18 and idade <= 80):
    print('Adulto')
elif(idade > 81):
    print('Adulto')
else:
    print('Benjamin button')
