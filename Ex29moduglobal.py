#Receba o tipo de investimento (1 = poupança e 2 = renda fixa) e o valor do investimento.
#Calcule e mostre o valor corrigido em 30 dias sabendo que a poupança = 3% e a renda fixa = 5%.
#Demais tipos não serão considerados.
#Declaração de variáveis 
Tinvest: int=0
Vinvestido: float=0
def calculareajuste():
    global Tinvest, Vinvestido 
    Vajustado: float=0.0
    if Tinvest ==1:
        Vajustado= (Vinvestido*0.03) + Vinvestido
        print('O valor ajustado é:', Vajustado)
    else:
        Vajustado = (Vinvestido*0.05) + Vinvestido
        print('O valor ajustadp é:', Vajustado)

def main():
    global Tinvest, Vinvestido
    Tinvest = int(input('Qual é o tipo de investimento?'))
    Vinvestido = float( input('Qual o valor a ser investido?'))
    calculareajuste()

if(__name__=='__main__'):
    main()