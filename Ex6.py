#6. Receba os valores em x e y. Efetua a troca de seus valores e mostre seus conteúdos.
#Decalração de variáveis 
X: float = 0.0
Y: float = 0.0
troca1: float = 0.0
troca2: float = 0.0
#início 
X = float(input('Digite o valor de X:'))
Y = float(input('Digite o valor de Y:'))
print("Os valores correspondentes são: X", X, "e Y", Y, "fazendo a troca temos:")
troca1 = Y
troca2 = X
print('Os valores trocados são:', troca1,"e", troca2)
#fim 