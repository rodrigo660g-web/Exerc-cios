#3. Receba a base e a altura de um triângulo. Calcule e mostre a sua área.
#Declaração de variáveis 
base: float= 0.0
altura : float = 0.0
area: float = 0.0
#início 
base = float(input("Digite o valor da base do triângulo:"))
altura = float(input("Digite o valor de altura do triângulo:"))
area = base*altura/2
print("A area do triângulo é:", area)
#fim 