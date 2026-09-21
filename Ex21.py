#Receba 4 notas bimestrais de um aluno. Calcule e mostre a média aritmética. Mostre a
#mensagem de acordo com a média:
#a. Se a média for >= 6,0 exibir “APROVADO”;
#b. Se a média for >= 3,0 ou < 6,0 exibir “EXAME”;
#c. Se a média for < 3,0 exibir “RETIDO”.
#Declaração de variáveis 
N1: float =0.0
N2: float = 0.0
N3: float = 0.0
N4: float = 0.0
M: float = 0.0
#início 
N1= float(input("Qual a nota da P1:"))
N2= float(input("Qual a nota da P2:"))
N3= float(input("Qual a nota da P3:"))
N4= float(input("Qual a nota da P4:"))
M= (N1+N2+N3+N4)/4
if M >=6:
    print("Parabéns você foi aprovado!!, Sua média é:")
if    6> M >= 3:
    print("Estude para o exame, sua média atual é:")
else: 
    M<3
    print("Você está retido, que pena")
#fim
