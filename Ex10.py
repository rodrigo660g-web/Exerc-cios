#10. Receba 2 números reais. Calcule e mostre a diferença desses valores.
#Declarão de variáveis
N1: float = 0.0
N2: float = 0.0
diferença: float= 0.0
resultado: float = 0.0
#início 
N1 = float(input("Digite o valor de N1:"))
N2 = float(input("Digite o valor de N2:"))
diferença = N1 - N2
resultado = abs(diferença)
print("A diferença entre os números são:", resultado)
