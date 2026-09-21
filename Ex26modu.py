#Receba 2 números inteiros. Verifique e mostre se o maior número é múltiplo do menor
#Declaração de variáveis 
V1: int=0
V2: int=0
def verifica():
    global V1, V2
    S: int=0
    if V1>V2:
        S= V1//V2 ==0
        print(V1, "é multiplo de", V2)
    elif V2>V1:
        S= V2//V1 ==0
        print(V2, "é multiplo de", V1)
    else:
        print(V1, "e", V2, "não são multiplos.")

def main():
    global V1, V2
    V1= int(input('Digite o primeiro valor:'))
    V2= int(input('Digite o segundo valor:'))
    verifica()

if(__name__=='__main__'):
    main()