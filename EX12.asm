#EX12.Desenvolver um algoritmo que leia a altura, em centímetros de 15 pessoas. Este programa deverá
#calcular e mostrar:
#a. A menor altura do grupo;
#b. A maior altura do grupo;
.data
msg1: .asciiz "\nDigite a altura em cm: "
msg2 : .asciiz "\nMenor altura: "
msg3: .asciiz "\nMaior altura: "

.text
main:
    li $t0, 15               # Contador do loop
    li $t1, 999              # Menor (começa alto)
    li $t2, 0                # Maior (começa baixo)

loopalt:
    beq $t0, $zero, exiberes
    li $v0, 4
    la $a0, msg1
    syscall
    li $v0, 5
    syscall
    move $t3, $v0

    bge $t3, $t1, checarmax
    move $t1, $t3            # Atualiza menor
checarmax:
    ble $t3, $t2, deloop
    move $t2, $t3            # Atualiza maior

deloop:
    subi $t0, $t0, 1
    j loopalt

exiberes:
    li $v0, 4
    la $a0, msg2
    syscall
    li $v0, 1
    move $a0, $t1
    syscall
    li $v0, 4
    la $a0, msg3
    syscall
    li $v0, 1
    move $a0, $t2
    syscall
    li $v0, 10
    syscall
