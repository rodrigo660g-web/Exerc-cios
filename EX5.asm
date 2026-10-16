#EX6 Faça um algoritmo que leia dois valores inteiros A e B se os valores forem iguais deverá se somar
#os dois, caso contrário multiplique A por B. Ao final de qualquer um dos cálculos deve-se atribuir o
#resultado para uma variável C e mostrar seu conteúdo na tela.
.data
msg1: .asciiz "\nDigite o valor de A: "
msg2: .asciiz "\nDigite o valor de B: "
msg3: .asciiz "\n O resultado C: "
.text
main:
    li $v0, 4
    la $a0, msg1
    syscall
    li $v0, 5
    syscall
    move $t0, $v0

    li $v0, 4
    la $a0, msg2
    syscall
    li $v0, 5
    syscall
    move $t1, $v0

    beq $t0, $t1, iguais      # Se $t0 == $t1 vai para  modulo 'iguais'
    
    # Se diferentes:
    mul $t2, $t0, $t1         # C = A * B
    j fim

iguais:
    add $t2, $t0, $t1         # C = A + B

fim:
    li $v0, 4
    la $a0, msg3
    syscall
    li $v0, 1
    move $a0, $t2
    syscall
    li $v0, 10
    syscall
