class Funcionario(object):
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome
    
    def setSalario(self, salario):
        self.saario = salario

    def getSalario(self):
        return self.salario
    
    def __str__(self):
        return(
            '\nNome: ' + str(self.getNome()) +
            f'\nSalário Total: R${self.salario:.2f}'
        )
    
    def calcularINSS(self):
        if self.salario > 5000:
            inss = self.salario * 0.1
            print(f'\nDesconto de INSS: R${inss:.2f}')
            print(f'\nSalário final: R${(self.salario - inss):.2f}')