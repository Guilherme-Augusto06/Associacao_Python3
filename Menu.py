from Classes import*

carro = Carro()                                 #Instanciando a classe Carro
carro_carlos = Carro()                          #Instanciando a classe Carro
carro_Thiago = Carro()                          #Instanciando a classe Carro
carro_Giulia = Carro()                          #Instanciando a classe Carro
carro_Pablo = Carro()                           #Instanciando a classe Carro
carro_zezin = Carro()                           #Instanciando a classe Carro

roda = Roda(17, 'BBS')                          #Instanciando a classe Roda
roda_Carlos = Roda(17, 'Scud')                  #Instanciando a classe Roda

motor = Motor('1.4', 1400, '75Litros')          #Instanciando a classe Motor
motor_Carlos = Motor('2.0', 2000, '80Litros')   #Instanciando a classe Motor
motor_Thiago = Motor('1.6', 1600, '70Litros')   #Instanciando a classe Motor




carro.setMotor(motor)                           #Setando o motor do carro
carro.setModelo('Camaro')                       #Setando o modelo do carro

carro_carlos.setMotor(motor_Carlos)             #Setando o motor do carro
carro_carlos.setModelo('Fusca')                 #Setando o modelo do carro

carro_Thiago.setMotor(motor_Thiago)             #Setando o motor do carro
carro_Thiago.setModelo('Gol')                   #Setando o modelo do carro

carro_Giulia.setMotor(motor)                    #Setando o motor do carro
carro_Giulia.setModelo('Camaro')                #Setando o modelo do carro

carro_Pablo.setMotor(motor)                     #Setando o motor do carro
carro_Pablo.setModelo('Camaro')                 #Setando o modelo do carro

carro_zezin.setMotor(motor)                     #Setando o motor do carro
carro_zezin.setModelo('Camaro')                 #Setando o modelo do carro

print(f'Carro: {carro.getModelo()}')            #Printando o modelo do carro
print(f'Motor: {carro.getMotor().getPotencia()}')    #Printando a potencia do motor
print(f'Cilindrada: {carro.getMotor().getCilindrada()}')    #Printando a cilindrada do motor
print(f'Combustivel: {carro.getMotor().getCombustivel()}')  #Printando o combustivel do motor
print(f'Rodas: {roda.getAro()}')            #Printando o aro da roda
print(f'Marca: {roda.getMarca()}')          #Printando a marca da roda
print('---------------------------')    
print(f'Carro: {carro_carlos.getModelo()}')           #Printando o modelo do carro
print(f'Motor: {carro_carlos.getMotor().getPotencia()}')    #Printando a potencia do motor
print(f'Cilindrada: {carro_carlos.getMotor().getCilindrada()}')   #Printando a cilindrada do motor
print(f'Combustivel: {carro_carlos.getMotor().getCombustivel()}')       #Printando o combustivel do motor
print(f'Rodas: {roda_Carlos.getAro()}')           #Printando o aro da roda
print(f'Marca: {roda_Carlos.getMarca()}')           #Printando a marca da roda
print('---------------------------')
print(f'Carro: {carro_Thiago.getModelo()}')         #Printando o modelo do carro
print(f'Motor: {carro_Thiago.getMotor().getPotencia()}')    #Printando a potencia do motor
print(f'Cilindrada: {carro_Thiago.getMotor().getCilindrada()}')  #Printando a cilindrada do motor
print(f'Combustivel: {carro_Thiago.getMotor().getCombustivel()}')   #Printando o combustivel do motor
print(f'Rodas: {roda.getAro()}')        #Printando o aro da roda
print(f'Marca: {roda.getMarca()}')      #Printando a marca da roda
print('---------------------------')
print(f'Carro: {carro_Giulia.getModelo()}')     #Printando o modelo do carro
print(f'Motor: {carro_Giulia.getMotor().getPotencia()}')    #Printando a potencia do motor
print(f'Cilindrada: {carro_Giulia.getMotor().getCilindrada()}')     #Printando a cilindrada do motor
print(f'Combustivel: {carro_Giulia.getMotor().getCombustivel()}')       #Printando o combustivel do motor
print(f'Rodas: {roda.getAro()}')                    #Printando o aro da roda
print(f'Marca: {roda.getMarca()}')                  #Printando a marca da roda
print('---------------------------')
print(f'Carro: {carro_Pablo.getModelo()}')          #Printando o modelo do carro
print(f'Motor: {carro_Pablo.getMotor().getPotencia()}')   #Printando a potencia do motor
print(f'Cilindrada: {carro_Pablo.getMotor().getCilindrada()}')  #Printando a cilindrada do motor
print(f'Combustivel: {carro_Pablo.getMotor().getCombustivel()}')    #Printando o combustivel do motor
print(f'Rodas: {roda.getAro()}')        #Printando o aro da roda
print(f'Marca: {roda.getMarca()}')    #Printando a marca da roda
print('---------------------------')
print(f'Carro: {carro_zezin.getModelo()}')        #Printando o modelo do carro
print(f'Motor: {carro_zezin.getMotor().getPotencia()}')   #Printando a potencia do motor
print(f'Cilindrada: {carro_zezin.getMotor().getCilindrada()}')  #Printando a cilindrada do motor
print(f'Combustivel: {carro_zezin.getMotor().getCombustivel()}')    #Printando o combustivel do motor
print(f'Rodas: {roda.getAro()}')    #Printando o aro da roda
print(f'Marca: {roda.getMarca()}')  #Printando a marca da roda
print('---------------------------')

