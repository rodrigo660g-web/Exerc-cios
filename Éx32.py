#Receba um número inteiro. Calcule e mostre o seu fatorial.
#Declaração de variáveis
N: int=0
R: int=1
#início 
N = int(input("Digite um número:"))
for i in range(1, N+1):
    R*=i
    print(R)
#fim


