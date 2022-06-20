# #- Dada uma lista de valores inteiros criar um programa para somar os valores pares e valores ímpares
# lista = [1, 22, 43, 45, 56]
# lista_pares = []
# lista_impares = []

# for n in lista:
#     if (n%2 == 0):
#         lista_pares.append(n)
#     else:
#         lista_impares.append(n)

# print(lista_pares)
# print(lista_impares)

# - Dada uma palavra criar uma programa para retornar a quantidade de vogais e quantidade de consoantes

# vogais = ['a', 'e', 'i', 'o', 'u']

# palavra = input("""Digite a palavra que deseja verificar: """"")

# for l in palavra:
#     for v in l:
#         if( v.lower() in vogais):
#             print(f"Vogal: {v}")
#         else:
#             print(f"Consoantes: {v}")



# - Criar um programa para adicionar funcionários. Os funcionários devem ter nome, sexo e salário o programa deve retornar a soma de salários dos homens e soma dos salários das mulheres
# funcionarios = []
funcionarios = []
operador = 1
salario_homens = []
salario_mulheres = []
soma_mulheres = 0
soma_homens = 0
lista_vazia = []

while operador != 0:
    print('[1] - inserir funcionario')
    print('[2] - Mostrar soma salario dos homens')
    print('[3] - Mostrar soma salario das mulheres')
    print('[4] - Mostrar funcionarios')
    print('[0] - encerrar programa')
    operador = int(input('digite uma opcao: '))
    if operador == 1:
        funcionario = {}
        nome = input('digite o nome: ')
        sexo = input('m - masculino ou f - feminino: ')
        salario = float(input('digite o salario: '))

        funcionario['nome'] = nome
        funcionario['sexo'] = sexo
        funcionario['salario'] = salario
        funcionarios.append(funcionario)
    elif operador == 2:
        for f in funcionarios:
            if f["sexo"] == 'm':
                salario_homens.append(f['salario'])
                for v in salario_homens:
                    soma_homens = v+v
        print(f'A soma do salario dos homens é: {soma_homens}')
    elif operador == 3:
        for f in funcionarios:
            if f["sexo"] == "f":
                salario_mulheres.append(f['salario'])
                for v in salario_mulheres:
                    soma_mulheres = v+v
        print(f'A soma do salario das Mulheres é: {soma_mulheres}')
    elif operador == 4:
        if funcionarios == lista_vazia:
            print('A lista esta vazia')
        else:
            print('Segue funcionarios')
            print(funcionarios)
    elif operador == 0:
        print('fim do programa')
        break
    else:
        print('opção inválida!')

print(funcionarios)

