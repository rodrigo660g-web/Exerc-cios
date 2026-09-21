#20. Receba 3 coeficientes A, B, e C de uma equação do 2o grau da fórmula AX2+BX+C=0. Verifique
#e mostre a existência de raízes reais e se caso exista, calcule e mostre.
#Declaração de variáveis 
A: float=0
B: float=0
C: float= 0
Delta: float = 0
X1: float = 0
X2: float = 0 
X: float = 0
#início 
A = float(input("QUal o valor do coeficente A:"))
B = float(input("Qual o valor do coeficente B:"))
C = float(input("Qual o valor do coeficnete C:"))
Delta = (B**2) - (4*A*C)
if Delta>0:
    print('A equação possui duas raizes naturais e diferentes')
    X1 = (-B + (Delta**0.5))/(2*A)
    X2 = (-B - (Delta**0.5))/(2*A)
    print("A solução das equações é:", X1, "e", X2)
elif Delta == 0:
    print("A raiz pussui apenas uma raiz real, ou duas raizes de mesmo valor:")
    X = (-B + (Delta**0.5))/(2*A)
    print("A solução da equação é:", X)
else:
    print("A equação não possui raizes no campo dos reais.")
    
#fim 
 

