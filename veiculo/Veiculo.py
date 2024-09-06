#Classe de teste para veículo 
class Veiculo(object):
    def __init__(self, marca, modelo, cor, velocidade):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.velocidade = velocidade

    def setMarca(self, marca):
        self.marca = marca

    def getMarca(self):
        return self.marca

    def setModelo(self, modelo):
        self.modelo = modelo
    
    def getModelo(self):
        return self.modelo

    def setCor(self, cor):
        self.cor = cor

    def getCor(self):
        return self.cor
    
    def setVelocidade(self, velocidade):
        self.velocidade = velocidade

    def getVelocidade(self):
        return self.velocidade
    
    def __str__(self):
        return(
            '\n Marca: ' + str(self.getMarca()) +
            '\n Modelo: ' + str(self.getModelo()) +
            '\n Cor: ' + str(self.getCor()) +
            '\n Velocidade: ' + str(self.getVelocidade())   
        )
    
    def acelerar(self):
        if self.velocidade < 120:
            self.velocidade+=1


    def frear(self):
        if self.velocidade > 0:
            self.velocidade-=1
