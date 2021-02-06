class Pessoa:
    def __init__(self, *pais, nome=None, idade=1):
        self.nome = nome
        self.idade = idade
        self.pais = list(pais)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    aldo = Pessoa(nome='Aldo', idade=48)
    karla = Pessoa(nome='Karla', idade=45)
    victor = Pessoa(aldo, karla, nome='Victor', idade=21)
    print(Pessoa.cumprimentar(victor))
    print(id(victor))
    print(victor.nome)
    print(victor.idade)
    print(victor.cumprimentar())
    print(f'{victor.nome}, {victor.idade}')
    print(victor.pais)
    for pai in victor.pais:
        print(pai)

