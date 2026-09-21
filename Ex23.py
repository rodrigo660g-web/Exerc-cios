#Receba 3 valores obrigatoriamente em ordem crescente e um 4o valor não necessariamente
#em ordem. Mostre os 4 números em ordem crescente.
#Declaração de variáveis 
V1: float=0.0
V2: float=0.0
V3: float=0.0
V4: float=0.0
#início 
V1= float(input("Digite o primeiro valor:"))
V2= float(input("Digite o segundo valor"))
V3= float(input("Digite o terceiro valor"))
V4= float(input("Digite o quarto valor:"))
print("Sua ordem é:", V1, V2, "e", V3, "vamos analisar o quarto valor")
if V4<V1:
    print("Sua ordem é:", V4, V1, V2, "e", V3)                  
elif V1<V4<V2:
   print("Sua ordem é:", V1, V4, V2, "e", V3)  
elif V2<V4<V3: 
   print("Sua ordem é:", V1, V2, V4, "e", V3) 
else:
    print("Sua ordem é:", V1, V2, V3, "e", V4) 
#fim  


     