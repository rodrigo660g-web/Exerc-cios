#Receba 2 valores reais. Calcule e mostre o maior deles.
#declaração de variáveis 
V1: float=0.0
V2: float = 0.0
def maior():
    global V1, V2
    if V1>V2:
        print('O maior númeoro é:', V1)
    else:
        print('O maior número é:', V2)

def main():
    global V1, V2
    V1= float(input('Digite um núemro:'))
    V2 = float(input('Digite outro número:'))
    maior()

if(__name__ == '__main__'):
    main()