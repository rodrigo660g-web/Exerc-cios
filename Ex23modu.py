#Receba 3 valores obrigatoriamente em ordem crescente e um 4o valor não necessariamente
#em ordem. Mostre os 4 números em ordem crescente.
#Declaração de variáveis 
V1: float=0.0
V2: float=0.0
V3: float=0.0
V4: float=0.0
def ordem():
    global V1, V2, V3,V4
    if V4<V1:
        print("Sua ordem é:", V4, V1, V2, "e", V3)
    elif V1<V4<V2:
        print("Sua ordem é:", V1, V4, V2, "e", V3)
    elif V2<V4<V3: 
        print("Sua ordem é:", V1, V2, V4, "e", V3)
    else:
        print("Sua ordem é:", V1, V2, V3, "e", V4) 
def main():
    global V1, V2, V3,V4
    V1= float(input("Digite o 1º valor:"))
    V2= float(input("Digite o 2º valor:"))
    V3= float(input("Digite o 3º valor:"))
    V4= float(input("Digite o 4º valor:"))
    ordem()

if(__name__=='__main__'):
    main()