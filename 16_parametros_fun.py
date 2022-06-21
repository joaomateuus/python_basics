# # Passando multiplos parametros
# def soma(*args):
#     return sum(args)

# res = soma(10, 3, 6, 7)
# print(res)

# # # Se quiser passar lista
# # def soma(*args):
# #     return sum(args)

# # numeros = [10, 34, 4, 3, 4]
# # print(soma(*numeros))

# def multiplicar(*args) -> float:
#     n = 1
#     for a in args:
#         n *= a
#         return n

# numeros = [2, 3, 4, 5]
# print(multiplicar(*numeros))
# print(multiplicar(3, 4, 5, 6))

# def pessoa(**kwargs):
#     return kwargs
# print(pessoa(nome = 'Joao Mateus', idade=20, altura = 1.68))

numero1 = input('Digite o n1: ')
numero2 = input('Digite o n2: ')
opera = input('Digite a operacao (+,-,*,/):  ')

numeros = {}
numeros["numero1"] = numero1
numeros["numero2"] = numero2
numeros["operacao"] = opera


def aritimetica(**kwargs):
    n1 = kwargs.get('numero1', 0)
    n2 = kwargs.get('numero2', 0)
    op = kwargs.get('operacao', '+')
    
    return eval(f'{n1} {op} {n2}')

print(aritimetica(**numeros))