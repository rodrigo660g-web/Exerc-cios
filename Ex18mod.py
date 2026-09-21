#Receba dois valores interios. Calcule e mostre a diferença do maior valor com o menor
#Declaração de variáveis:
N1: float=0.0
N2: float =0.0
def diferença():
    global N1, N2
    calculo: float =0.0
    if N1>N2:
        calculo = (N1-N2)
        print('A diferença entre os valores é:', calculo)
    else:
        calculo = (N2-N1)
        print('A diferença entre os valores é:', calculo)
def main():
    global N1, N2
    N1 = float(input("Digite um número:"))
    N2 = float(input("digite outro número:"))
    diferença()

if(__name__== '__main__'):
    main()