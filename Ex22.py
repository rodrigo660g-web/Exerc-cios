#Receba 2 valores inteiros e diferentes. Mostre seus valores em ordem crescente.
#declarção de variáveis 
N1: int=0
N2: int=0
#início 
N1=int(input("Digite o valor do primeiro número:"))
N2=int(input("Digite o valor do segundo número:"))
if N1>N2:
    print("Os valores em ordem crescente são:", N2,"e", N1)
else:
    print("Os valores em ordem cresente são:", N1,"e", N2)
#fim