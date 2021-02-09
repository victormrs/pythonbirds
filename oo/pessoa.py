class Pessoa:
    olhos = 2

    def __init__(self, *pais, nome=None, idade=1):
        self.nome = nome
        self.idade = idade
        self.pais = list(pais)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 40

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls}, -olhos {cls.olhos}'

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
    victor.sobrenome = 'Morais'
    del victor.sobrenome
    print(aldo.__dict__)
    print(victor.__dict__)
    print(Pessoa.olhos)
    print(aldo.olhos)
    print(victor.olhos)
    print(id(Pessoa.olhos), id(aldo.olhos), id(victor.olhos))
    print(Pessoa.metodo_estatico(), victor.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), victor.nome_e_atributos_de_classe())
