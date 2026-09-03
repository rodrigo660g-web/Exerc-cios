#7. Receba os valores do comprimento, largura e altura de um paralelepípedo. Calcule e mostre seu volume.
#Decalração de variáveis 
comprimento: float = 0.0
largura: float = 0.0
altura: float= 0.0
volume: float = 0.0
#início 
comprimento = float(input("Digite o valor do comprimento:"))
largura = float(input("Digite o valor da largura:"))
altura = float(input("Digite o valor da altura:"))
volume = (altura*largura*comprimento)
print(" O valor do volume em m³ é:", volume)