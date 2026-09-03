#13. Receba a quantidade de alimento em quilos. Calcule e mostre quantos dias durará esse alimento sabendo que a pessoa consome 50g ao dia.
#Declaração de variáveis 
Quilos: float= 0.0
dias: int = 0
#início 
Quilos = float(input("Quantos quilos possuem todos os alimentos juntos:"))
dias = (Quilos*1000)/50
print("A quantidade de dias que seus alimentos duram é:", dias)
#fim
