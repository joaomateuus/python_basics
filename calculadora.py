# # Digitar um monte de coisa na calculadora e e fazer o calculo ex:23423+23423-4534534/4
# def calc_expressao(args: str) -> float:
#     return eval(args)

# input_usuario = input('Digite a operacao que deseja fazer:  ')
# resul = calc_expressao(input_usuario)
# print(calc_expressao(input_usuario))

# while True:
#     def calc_expressao(args:str) -> float:
#         return eval(args)

#     numero = input('Digite a expressao que deseja calcular:  ')
#     print(calc_expressao(numero))
#     print('Digite 1 para sair ou qualuer tecla para continuar')

#     condicao = int(input('Deseja continuar ?  '))
#     if condicao == 1:
#         break
#     else:
#         pass


#calculadora que para zera tem q limpar
def calculadora(args: str) -> float:
    return eval(args)
    
def main():
    while True:
        text = input('Digite a operacao:  ')

        if text == 'exit':
            break
        else:
            resul = calculadora(text)
            print(resul)

main()

#Armazenar o valor do primeiro input
#atribuir a variavel somando