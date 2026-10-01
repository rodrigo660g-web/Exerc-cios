#Receba o número de voltas, a extensão do circuito (em metros) e o tempo de duração
#(minutos). Calcule e mostre a velocidade média em km/h.
#Declaração de variaveis
Nvoltas: int
Extensão: float 
Tempodura: float

def calcvm():
    global Nvoltas, Extensão, Tempodura
    Dista: float =0.0
    VM: float =0.0
    Dista = ((Nvoltas*Extensão)/1000)
    VM= (Dista/(Tempodura/60))
    print('A velocidade média é: ', VM,'Km/h')

def main():
    #inicio
    global Nvoltas, Extensão, Tempodura
    Nvoltas= float(input('Quantas voltas a corrida teve?'))
    Extensão = float(input('Qual a extensão do circuito em metros?'))
    Tempodura = float(input('Qula a duração da corrida em minutos?'))
    calcvm()


if(__name__=='__main__'):
    main()