#5. Receba os coeficientes A, B e C de uma equação do 2o grau (AX2+BX+C=0). Calcule e mostre as raízes reais (considerar que a equação possui 2 raízes reais).
#Declaração de variáveis 
A: int = 0
B: int = 0
C: int = 0
delta: int = 0
raiz1 : int = 0
raiz2 : int = 0
#início 
A = int(input("Digite o valor de A:"))
B = int(input("Digite o valor de B:"))
C = int(input("Digite o valor de C:"))
delta = ((B**2)-4*A*C)
print("O valor de Delta é:", delta)
raiz1= ((- B) + (delta**0.5))/(2*A)
raiz2= ((- B) - (delta**0.5))/(2*A)
print("As raízes da equação são:", raiz1, raiz2)
#fim