class Estudante(object):
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome
    
    def setNota(self, notas):
        self.notas = notas

    def getNotas(self):
        return self.notas
    
    def __str__(self):
        return(
            '\nNome: ' + str(self.getNome()) +
            f'\nNotas: {", ".join(f"{notas:.2f}" for notas in self.notas)}'
        )
    
    def calcularMedia(self):
        media = sum(self.notas) / 4
        print(f"Média: {media:.2f}")    