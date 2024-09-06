class Data(object):
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano 

    def setDia(self, dia):
        self.dia = dia
    
    def getDia(self):
        return self.dia
    
    def setMes(self, mes):
        self.mes = mes

    def getMes(self):
        return self.mes
    
    def setAno(self, ano):
        self.ano = ano

    def getAno(self):
        return self.ano

    def __str__(self):
        return(
            '\n Dia:' + str(self.getDia()) +
            '\n Mês:' + str(self.getMes()) +
            '\n Ano:' + str(self.getAno()) 
        )
    
    def checarData(self):
        if self.dia > 31 or self.dia < 1 or self.mes > 12 or self.mes < 1:
            return False
        return True
    