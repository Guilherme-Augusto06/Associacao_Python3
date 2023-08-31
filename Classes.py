class Motor:
    def __init__(self, potencia, cilindrada, combustivel):
        self.potencia = potencia
        self.cilindrada = cilindrada
        self.combustivel = combustivel

    def getPotencia(self):
        return self.potencia

    def getCilindrada(self):
        return self.cilindrada
    
    def getCombustivel(self):
        return self.combustivel
    
    def setPotencia(self, potencia):
        self.potencia = potencia

    def setCilindrada(self, cilindrada):
        self.cilindrada = cilindrada
    
    def setCombustivel(self, combustivel):
        self.combustivel = combustivel

class Roda:
    def __init__(self, aro, marca):
        self.aro = aro
        self.marca = marca
    
    def getAro(self):
        return self.aro
    
    def getMarca(self):
        return self.marca
    
    def setAro(self, aro):
        self.aro = aro
    
    def setMarca(self, marca):
        self.marca = marca

class Carro:
    def __init_(self):
        self.motor = None
        self.modelo = None
    
    def getMotor(self):
        return self.motor
    
    def getModelo(self):
        return self.modelo
    
    def setMotor(self, motor):
        self.motor = motor
    
    def setModelo(self, modelo):
        self.modelo = modelo