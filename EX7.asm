#EX7 Faça um algoritmo que leia uma variável e some 5, caso seja par ou some 8, caso seja ímpar,
#imprimir o resultado desta operação.
.data
msg1: .asciiz "\nDigite um numero: "
msg2: .asciiz "\nResultado: "
.text
main:
    li $v0, 4
    la $a0, msg1
    syscall
    li $v0, 5
    syscall
    move $t0, $v0

    andi $t1, $t0, 1          # ponto a ponto: $t1 = $t0 & 1
    beq $t1, $zero, par       # Se o ponto for 0, é par 

    # Se for ÍMPAR:
    addi $t2, $t0, 8
    j fim

par:
    addi $t2, $t0, 5
fim:
    li $v0, 4
    la $a0, msg2
    syscall
    li $v0, 1
    move $a0, $t2
    syscall
    li $v0, 10
    syscall
