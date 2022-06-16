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
funcionario1, funcionario2, funcionario3 = {
    
}


funcionarios = {
    funcionario1: {
        "nome": input(""" Qual o nome do funcionario """""),
        "sexo": input(""" Qual o sexo do funcionario """""),
        "salario": int(input(""" Qual o salario do funcionario """""))
    },

    funcionario2: {
        "nome": input(""" Qual o nome do funcionario """""),
        "sexo": input(""" Qual o sexo do funcionario """""),
        "salario": int(input(""" Qual o salario do funcionario """""))
    },

    funcionario3: {
        "nome": input(""" Qual o nome do funcionario """""),
        "sexo": input(""" Qual o sexo do funcionario """""),
        "salario": int(input(""" Qual o salario do funcionario """""))
    }

}

for f in funcionarios:
    print(f)



# # soma_salarios = 
# soma_salarios = funcionario1["salario"]+funcionario2["salario"]+funcionario3["salario"]

# print(f"A soma dos salarios dos funcionarios é: {soma_salarios}")

