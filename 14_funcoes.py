#Faca 3 funcoes somar, subtrair e multiplicar, respecitvamente funcao normal, funcao com parametros tipados, funcao com parametros tipados retornado tipo especifico

def somar(a, b):
    return a + b

def subtrair(a:int, b:int):
    return a - b
def multiplicar(a:int, b:int) -> float:
    return a * b

print(somar(24, 13))
print(subtrair(42, 16))
print(multiplicar(b=252, a=31))