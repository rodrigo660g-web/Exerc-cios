#Receba 2 valores inteiros e diferentes. Mostre seus valores em ordem crescente.
#declarção de variáveis 
V1: int=0
V2: int =0
def crescente():
    global V1, V2 
    if V1>V2:
        print('Os valores em ordem sãovcrescente :', V2,',', V1)
    else:
        print('Os valores em ordem crescente são:', V1,',', V2)

def main():
    global V1, V2 
    V1 = int(input('Digite um valor:'))
    V2 = int(input('Digite outro valor:'))
    crescente()

if(__name__=='__main__'):
    main()