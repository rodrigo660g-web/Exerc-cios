#Receba o tipo de investimento (1 = poupança e 2 = renda fixa) e o valor do investimento.
#Calcule e mostre o valor corrigido em 30 dias sabendo que a poupança = 3% e a renda fixa = 5%.
#Demais tipos não serão considerados.
#Declaração de variáveis 
Investimento: int =0
Valorinvest: float =0.0
Valorcorrig: float =0.0
#início 
Investimento = int(input("Digite 1 para poupança ou 2 para renda fixa:"))
Valorinvest = float(input("Qual o valor do seu investimento:"))
if Investimento ==1:
    Valorcorrig = (Valorinvest + (Valorinvest*0.03))
    print("Seu vaor corrigido após trinta dias é:", Valorcorrig)
else:
    Valorcorrig = (Valorinvest+(Valorinvest*0.07))
    print("Seu valor corrigido após trenta dias é:", Valorcorrig)
#fim