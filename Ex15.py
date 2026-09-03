#15. Receba os valores de 2 catetos de um triângulo retângulo. Calcule e mostre a hipotenusa.
#Declaração de variavéis 
C1: float=0.0
C2: float= 0.0
H: float = 0.0
#início 
C1= float(input("Qaul o valor do primerio cateto?"))
C2= float(input("QUal o valor do segundo cateto?"))
H = ((C1**2)+(C2**2))**0.5
print("O valor da Hipotenusa é:", H)
#fim