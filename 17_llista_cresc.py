import random

lista = []
lista_menores = []
lista_maiores = []

for i in range(10):
    lista.append(random.randint(1,200))

# for l in lista:
#     if l < 100:
#         lista_menores.append(l)
#     else:
#         lista_maiores.append(l)


#Criar lista com operacoes
numero = [n for n in lista if n%2 == 0]

# print(f'Os numeros menores que cem sao  {lista_menores}')
# print(f'Os maiores numeros sao  {lista_maiores}')

print(numero)

