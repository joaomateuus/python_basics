from datetime import datetime, date

class Pessoa:
    def __init__(self, nome, nascimento):
        self.nome = nome
        self.nascimento = nascimento

    def __str__(self):
        return f'{self.nome} {self.nascimento}'

    #Property retorna um valor
    @property
    def idade(self):
        hoje = datetime.now().date()
        diferenca = hoje - self.nascimento
        return int(diferenca.days/365)

#HERANCA
class PessoaFisica(Pessoa):
    def __init__(self, nome, cpf, nascimento):
        super().__init__(nome=nome, nascimento=nascimento)
        self.cpf = cpf
    
    def __str__(self):
        return f'{self.nome} {self.cpf}'

pessoaf1 = PessoaFisica(nome='Joao Mateus', cpf='02758621274', nascimento=date(2001,8,7))
print(pessoaf1)

class PessoaJuridica(Pessoa):
    def __init__(self, nome, cnpj ,nascimento):
        super().__init__(nome=nome, nascimento=nascimento)
        self.cnpj = cnpj
    
    def __str__(self):
        return f'{self.nome} {self.cnpj} {self.nascimento}'
pessoaj1 = PessoaJuridica(nome='Joao', cnpj='27348273', nascimento=date(2001, 7, 16))
print(pessoaj1)

class PessoaIdosa(Pessoa):
    def __init__(self, nome, nascimento, remedios, filhos):
        super().__init__(nome=nome, nascimento=nascimento)
        self.remedios = remedios
        self.filhos = filhos
    def __str__(self):
        return f'{self.nome} {self.nascimento} {self.remedios} {self.filhos}'
idoso1 = PessoaIdosa(nome='Terezinha', nascimento=date(1966, 8, 18), remedios='rivotril' ,filhos='Nao')
print(idoso1)

class PessoaAtleta(Pessoa):
    def __init__(self, nome, nascimento, altura, fisico):
        super().__init__(nome=nome, nascimento=nascimento)
        self.altura = altura
        self.fisico = fisico
    def __str__(self):
        return f'{self.nome} {self.nascimento} {self.altura} {self.fisico}'

atleta = PessoaAtleta(nome='Carlins', nascimento=date(1999, 6, 17), altura='1.65', fisico='Atleta' )
print(atleta)
# joao = Pessoa(nome='Joao Mateus', nascimento=date(2001, 8, 7))

# print(joao.idade)
