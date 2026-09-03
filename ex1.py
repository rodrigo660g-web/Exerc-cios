#1. Coletar o valor do lado de um quadrado, calcular sua área e apresentar o resultado.
#declaração de variáveis 
ladoquadrado: float = 0.0
area: float = 0.0

#início
ladoquadrado = float(input("digite o valor do lado do quadrado:"))
area = ladoquadrado**2
print('A area do quadrado é:', area)
#fim