lista_numeros = [10, 5, 9, 7, 2]
pessoa = {
    'nome': 'Abraaao',
    'idade': 26,
    'altura': 1.68,
    'habilidades': [
        'jogar futebol',
        'programar'
    ]
}

for n in lista_numeros:
    print(n) 

for n in range(10):
    print(n)

for p in pessoa:
    print('A chave é {chave} e o valor é {valor}'.format(chave = p, valor = pessoa.get(p)))