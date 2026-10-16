#RX10. No Assembly MIPS, existe a operação REM que apresenta o resto da divisão de 2 valores inteiros.
SEM UTILIZAR A OPERAÇÃO
.data
msg1: .asciiz "\nDigite N1: "
msg2: .asciiz "\nDigite N2: "
msg3: .asciiz "\nResto da divisao é: "
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

    # Organiza : $t2 = Maior, $t3 = Menor
    bge $t0, $t1, n1maior
    move $t2, $t1
    move $t3, $t0
    j calcula
N1maior:
    move $t2, $t0
    move $t3, $t1

calcula:
    div $t2, $t3             # Maior / Menor
    mflo $t4                 # Quociente
    mul $t5, $t4, $t3        # Quociente * Menor
    sub $t6, $t2, $t5        # Resto = Maior - (Quociente * Menor)

    li $v0, 4
    la $a0, msg3
    syscall
    li $v0, 1
    move $a0, $t6
    syscall
    li $v0, 10
    syscall
