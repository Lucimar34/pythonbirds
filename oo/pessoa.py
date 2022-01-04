class Pessoa:
    def __init__(self, *filhos, nome=None, idade=37):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    maxwell = Pessoa(nome='Maxwell')
    lucimar = Pessoa(maxwell, nome='Lucimar')
    print(Pessoa.cumprimentar(lucimar))
    print(id(lucimar))
    print(lucimar.cumprimentar())
    print(lucimar.nome)
    print(lucimar.idade)
    for filho in lucimar.filhos:
        print(filho.nome)




