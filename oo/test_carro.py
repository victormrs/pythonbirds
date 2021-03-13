from unittest import TestCase

from oo.carro import Motor

class CarroTestCase(TestCase):
    def test_motor_carro(self):
        motor = Motor()
        self.assertEqual(0, motor.velocidade)

    def test_aceleracao_carro(self):
        motor = Motor()
        motor.acelerar()
        self.assertEqual(1, motor.velocidade)
