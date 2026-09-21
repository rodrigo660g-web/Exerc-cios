#Receba um valor inteiro. Verifique e mostre se é divisível por 2 e 3.
#Declaração de variáveis 
V: int= 0
def analise():
    global V
    if V % 2==0 and V%3==0:
        print("O valor", V, "é divisível por 2 e 3.")
    elif V % 2 != 0 and V%3==0:
        print("O valor", V, "é divisível por 3, mas não por 2.")
    elif V % 2== 0 and V%3 !=0:
        print("O valor", V, "é divisível por 2, mas não por 3.")
    else:
        print("O valor não é divisevel por 2 e 3.")

def main():
    global V
    V= int(input('Digite um valor a ser analisado:'))
    analise()
if (__name__=='__main__'):
    main()