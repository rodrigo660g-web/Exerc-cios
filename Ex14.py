#14. Receba 2 ângulos de um triângulo. Calcule e mostre o valor do 3o ângulo.
#Declaração de variáveis 
A1: float= 0.0
A2: float = 0.0
A3: float = 0.0
#início
A1 = float(input("Qual o valor do primeiro ãngulo?"))
A2= float(input("Qual o valor do segundo ângulo?"))
A3= 180 -(A1+A2)
print("O valor do 3º ângulo é:", A3)
#fim