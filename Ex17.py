#17. Calcule a quantidade de litros gastos em uma viagem, sabendo que o automóvel faz 12 km/l. Receber o tempo de percurso e a velocidade média.
#Declaração de variáveis 
Tempodeviagem : float = 0.0
Velocidademédia: float = 0.0
percurso: float= 0.0
consumo: float=0.0

#início
Tempodeviagem = float(input("Qual o tempo gasto na viagem?"))
Velocidademédia = float(input("Qual foi sua velocidade média?"))
percurso = Tempodeviagem*Velocidademédia
consumo = percurso/12
print("Você realizou uma viagem de", percurso, "kms e seu consumo total foi de", consumo, "litros")