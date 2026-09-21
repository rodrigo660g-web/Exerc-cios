#Receba um número. Calcule e mostre a série 1 + 1/2 + 1/3 + ... + 1/N.
#Declaração de variáveis 
N: int=0
R: float=0.0
i: int =1
#inpicio
N = int(input("Digite um número:"))
while i<=N:
    R+=(1/i)
    i+=1
    print(R)


