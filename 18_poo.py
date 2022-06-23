from datetime import datetime, date

class Pessoa:
    def __init__(self, nome, nascimento):
        self.nome = nome
        self.nascimento = nascimento

    def __str__(self):
        return f'{self.nome} {self.nascimento}'

    @property
    def idade(self):
        hoje = datetime.now().date()
        diferenca = hoje - self.nascimento
        return int(diferenca.days/365)

joao = Pessoa(nome='Joao Mateus', nascimento=date(2001, 8, 7))

print(joao.idade)
