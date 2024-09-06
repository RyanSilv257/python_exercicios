import random

from Estudante import Estudante

estudante = Estudante('João Almeida', [random.random()*10 for i in range(0, 4)])

print(estudante)

estudante.calcularMedia()