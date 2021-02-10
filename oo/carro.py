


class Motor:

    def __init__(self, velocidade=0):
        self.velocidade = velocidade

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        if self.velocidade > 1:
            self.velocidade -= 2
        elif self.velocidade == 1:
            self.velocidade -= 1


motor1 = Motor()


class Direcao:

    def __init__(self, direcao='Norte'):
        self.direcao = direcao

    def girar_a_direita(self):
        if self.direcao == 'Norte':
            self.direcao = 'Leste'
        elif self.direcao == 'Leste':
            self.direcao = 'Sul'
        elif self.direcao == 'Sul':
            self.direcao = 'Oeste'
        elif self.direcao == 'Oeste':
            self.direcao = 'Norte'

    def girar_a_esquerda(self):
        if self.direcao == 'Norte':
            self.direcao = 'Oeste'
        elif self.direcao == 'Oeste':
            self.direcao = 'Sul'
        elif self.direcao == 'Sul':
            self.direcao = 'Leste'
        elif self.direcao == 'Leste':
            self.direcao = 'Norte'


direcao1 = Direcao()


class Carro:

    def __init__(self, motor=Motor(), direcao=Direcao()):
        self.motor = motor
        self.direcao = direcao

    def calcular_velocidade(self):
        return self.motor.velocidade

    def mostrar_direcao(self):
        return self.direcao.direcao

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()

    def girar_a_direita(self):
        self.direcao.girar_a_direita()


carro = Carro()

print(carro.calcular_velocidade())
print(carro.mostrar_direcao())
carro.acelerar()
carro.acelerar()
print(carro.calcular_velocidade())
carro.frear()
print(carro.calcular_velocidade())
carro.girar_a_esquerda()
carro.girar_a_esquerda()
print(carro.mostrar_direcao())
