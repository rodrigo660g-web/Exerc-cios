#úmero é múltiplo do menor.Receba 2 números inteiros. Verifique e mostre se o maior n
#Declaração de variáveis 
V1: int=0
V2: int=0
S: int=0
#inicio 
V1= int(input("Digite o valor do primeiro número:"))
V2= int(input("Digite o valor do segundo número:"))

if V1>V2:
    S= ((V1%V2)==0)
    print(V1, "é multiplo de", V2)
elif V2>V1:
    S=((V2%V1)==0)
    print(V2, "é multiplo de", V1)
else:
    print(V1, "e", V2, "não são multiplos.")

    