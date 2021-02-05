class Pessoa:
    def __init__(self, nome=None, idade=1):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    p = Pessoa('Victor', 21)
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.nome)
    print(p.idade)
    print(p.cumprimentar())
    print(f'{p.nome}, {p.idade}')

