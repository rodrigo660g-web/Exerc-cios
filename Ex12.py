#12. Receba o ano de nascimento e o ano atual. Calcule e mostre a sua idade e quantos anos terá daqui a 17 anos.
#declaração de variáveis
nascimento: int=0
anoatual: int=0
futuro: int=0
idade: int=0
#inicio
anoatual = int(input("QUal é o ano atual?"))
nascimento = int(input("Qual seu ano de nascimento?"))
idade = anoatual - nascimento
futuro = idade + 17
print("A sua idade atual é:", idade,"anos e sua idade futura daqui a 17 anos é", futuro, "anos")
#fim
