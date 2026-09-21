#Receba dois valores interios. Calcule e mostre a diferença do maior valor com o menor
#Declaração de variáveis:
N1: int =0
N2: int = 0 
Diferença: int=0
#início 
N1 = int(input("digite um número:"))
N2 = int(input("digite outro número:"))
if N1>N2 :
  Diferença = N1-N2
  print('A diferença entre os números é:', Diferença)
else: 
   Diferença = N2- N1
   print('A diferença entre os números é:', Diferença)
#fim
