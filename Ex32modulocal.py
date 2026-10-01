#Receba um número inteiro. Calcule e mostre o seu fatorial.
#Declaração de variáveis
N: int=0
def calcfat(n):
    c: int= 0
    f: int = 1
    for c in range(n, 0, -1):
        f= f* c
        print(f)

def main():
    global N 
    N= int(input('Digite um núemro:'))
    calcfat(N)
    

if(__name__=='__main__'):
    main()