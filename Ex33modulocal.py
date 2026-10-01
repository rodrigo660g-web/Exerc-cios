#Receba um número. Calcule e mostre a série 1 + 1/2 + 1/3 + ... + 1/N.
#Declaração de variáveis 
N: int=0
def calserie(n):
    c: int=0
    q: int=0
    while q<=n:
        c=(1/(1+q))
        q+= 1
        print(c)

def main():
    global N
    N= int(input('Digite um número:'))
    calserie(N)


    
if(__name__=='__main__'):
    main()