#16. Receba a quantidade de horas trabalhadas, o valor por hora, o percentual de desconto e o
#número de descendentes. Calcule o salário que serão as horas trabalhadas x o valor por hora.
#Calcule o salário líquido (= Salário Bruto – desconto). A cada dependente será acrescido R$ 100
#no Salário Líquido. Exiba o salário a receber.
#Declaração de variáveis 
HT: int=0
HS: int=0
VH: int =0
PD: float= 0 
numerodedencendentes: int= 0
salárioBruto: int = 0 
salariolíquido: int=0
ST: int= 0
#início 
HT= int(input("Qual a quantidade de horas trabalhadas no mês?"))
HS= int(input("Qual a quantidade de horas trabalhadas por semana"))
VH= HT/HS
PD = int(input("Qual a porcentagem de descontos do seu salário?"))
numerodedencendentes = int(input("Quantos filhos você tem?"))
salárioBruto= HT*VH
salariolíquido= (salárioBruto)- ((PD/100)*salárioBruto)
ST= salariolíquido + (numerodedencendentes*100)
print('O seu salário a receber é:', ST)
#fim

