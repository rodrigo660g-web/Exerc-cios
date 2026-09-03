#8. Receba o valor de um depósito em poupança. Calcule e mostre o valor após 1 mês de aplicação sabendo que rende 1,3% a. m.
#Declaração de variáveis 
deposito: float = 0.0
rendimento: float = 0.0
#inicio 
deposito = float(input("digite o valor do seu deposito:"))
rendimento = (deposito*0.013) + deposito
print("Seu rendimento após um mês é:",rendimento )
#fim