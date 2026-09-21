#Receba o número de voltas, a extensão do circuito (em metros) e o tempo de duração
#(minutos). Calcule e mostre a velocidade média em km/h.
#Declaração de variaveis
Nvoltas: float= 0.0
ExtC: float =0.0
TemT: float = 0.0
TemH: float =0.0
Dist: float =0.0
VM: float =0.0
#início 
Nvoltas = float(input("Quantas voltas a corrida teve?"))
ExtC = float(input("Qual a extensão do circuito?"))
TemT = float(input("Qual o tempo total de duração da prova em minutos?"))
Dist =((Nvoltas*ExtC)/1000)
VM =(Dist/(TemT/60))
print("a velocidade média em Km/h é:", VM)