#Calcule e mostre o quadrado dos números entre 10 e 150.
#Declaração de variáveis 
N: int=0
def calcquad(n):
    n: int
    q: int
    #início 
    q = (n*n)
    print(q)



def main():
    global N 
    for N in range(10, 151):
        calcquad(N)


if(__name__=='__main__'):
    main()