#Receba a hora de início e de final de um jogo (HH,MM), calcular o tempo do jogo em horas e
#minutos, sabendo que o tempo máximo é menor que 24 horas e pode começar num dia e
#terminar noutro.
#Declaração de variáveis:
Hinicial: int=0
Imin: int=0
Hfinal: int=0
Fmin: int=0
Tempo: int=0
Tempof: int=0
Total: int=0
TH: int=0
#Início 
Hinicial = int(input("Qual a hora de início do jogo:"))
Imin= int(input("Qual os minutos inciais do jogo:"))
Hfinal = int(input("Qual a hora de final do jogo:"))
Fmin= int(input("Qual os minutos finais do jogo:"))
Tempo = Hinicial*60 + (Imin)
Tempof = Hfinal*60 +(Fmin)
if Tempof<= Tempo:
    Tempof += 24*60
Total = Tempof-Tempo
TH = Total/60
print( "A duração do jogo é de:", Total, "minutos, ou", TH, "horas")
