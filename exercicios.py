# #- Dada uma lista de valores inteiros criar um programa para somar os valores pares e valores ímpares
# import random
# numeros = []
# sum_par = 0
# sum_impar = 0

# for i in range(20):
#     numeros.append(random.randint(0, 100))

# for numero in numeros:
#     if(numero % 2 == 0):
#         sum_par += numero
#     else:
#         sum_impar += numero

# print(sum_par)
# print(sum_impar)

# # - Dada uma palavra criar uma programa para retornar a quantidade de vogais e quantidade de consoantes
# vogais = 'AEIOU'
# consoantes = 'BCDFGKLMNPQRSTVWXYZ'
# lista_vogais = []
# lista_consoantes = []

# texto = input('Digite alguma palavra:  ')

# for t in texto.upper():
#     if t in vogais:
#         lista_vogais.append(t)
#     elif t in consoantes:
#         lista_consoantes.append(t)

# print('As vogais sao {} e o total é {}'.format(lista_vogais, len(lista_vogais)))
# print('As consoantes sao {} e o total é {}'.format(lista_consoantes, len(lista_consoantes)))


# # - Criar um programa para adicionar funcionários. Os funcionários devem ter nome, sexo e salário o programa deve retornar a soma de salários dos homens e soma dos salários das mulheres
funcionarios = [
    {
        'nome': 'Abraao',
        'sexo': 'm',
        'salario': 1200.33
    },
    {
        'nome': 'Joao Mateus',
        'sexo': 'm',
        'salario': 500.33
    }
]

while True:
    print('0 - Sair do Programa')
    print('1 - Adicionar funcionario')
    print('2 - Mostrar soma dos salarios ')

    op = int(input('Digite a opcao que deseja:  '))

    if op == 0:
        print('Tchau')
        break
    elif op == 1:
        funcionario = {}
        nome = input('Digite o nome do funcionario:  ')
        sexo = input('Digite o sexo (m/f):  ')
        salario = float(input('Digite o salario desse funcionario:  '))

        funcionario['nome'] = nome
        funcionario['sexo'] = sexo
        funcionario['salario'] = salario

        funcionarios.append(funcionario)
        print(f'Atualmente esses sao nossos funcionarios {funcionarios}')
    elif op == 2:
        salario_home = 0
        salario_mulhe = 0

    for funcionario in funcionarios:
        if funcionario['sexo'] == 'm':
            salario_home += funcionario.get('salario')
        elif funcionario['sexo'] == 'f':
            salario_mulhe += funcionario.get('salario')
    print(f'A soma dos salarios dos homens é R${salario_home}') 
    print(f'A soma dos salarios das mulheres é R${salario_mulhe}')