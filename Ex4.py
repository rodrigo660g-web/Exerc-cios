#Receba a temperatura em graus Celsius. Calcule e mostre a sua temperatura convertida em fahrenheit F = (9*C+160) /5.
#Declaração de varáveis 
Celcius: float = 0.0
Fahrenheit: float = 0.0
#início 
Celcius =  float(input("Digite o valor da temperatura:"))
Fahrenheit = (((9*Celcius) + 160)/5)
print("A temperatura em fahrenheit é:", Fahrenheit)
#fim 