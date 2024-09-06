import random

from Funcionario import Funcionario

func1 = Funcionario('Fulano da Silva', random.random() * 10000)

print(func1)
func1.calcularINSS()
