idade = int(input("""Digite sua idade

"""))

if idade >= 80:
    print('Idoso')
elif idade >= 18 and idade <= 80:
    print('Adulto')
elif idade >= 12 and idade <= 18:
    print('Adolescente')
elif idade >= 0 and idade <= 12:
    print('Crianca')
else:
    print('Benjamin button')

