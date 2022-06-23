funcionarios = []

f1 = {'nome':'Joao Mateus', 'sexo': 'm', 'salario': 1200}
f2 = {'nome':'Abraao', 'sexo': 'm', 'salario': 1500}
f3 = {'nome':'Lucia', 'sexo': 'f', 'salario': 1500}
f4 = {'nome':'Julia ', 'sexo': 'f', 'salario': 1700}

funcionarios.append(f1)
funcionarios.append(f2)
funcionarios.append(f3)
funcionarios.append(f4)

soma_homens = sum([sh['salario'] for sh in funcionarios if sh['sexo']=='m'])
soma_mulheres = sum([sh['salario'] for sh in funcionarios if sh['sexo']=='f'])

print(f'A soma do salario do salario dos homens é: {soma_homens} ')
print(f'A soma do salario das mulhres é: {soma_mulheres} ')





