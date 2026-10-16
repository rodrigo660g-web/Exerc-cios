#EX9 Fazer um algoritmo que leia 2 números inteiros e exiba a divisão destes. Sabe-se que o 2o número
#não pode ser zero, portanto, deve-se insistir na solicitação do 2o número até ele ser diferente de 0
.data
msg1: .asciiz "\nDigite o primeiro numero: "
msg2: .asciiz "\nDigite o segundo numero (diferente de zero): "
msg3: .asciiz "\nValor invalido! O numero não pode ser zero"
msg4: .asciiz "\nResultado da divisao: "

.text
main:
    li $v0, 4
    la $a0, msg1
    syscall
    li $v0, 5
    syscall
    move $t0, $v0

segundo:
    li $v0, 4
    la $a0, msg2
    syscall
    li $v0, 5
    syscall
    move $t1, $v0

    bne $t1, $zero, fazdiv   # Se $t1 != 0 prossegue

    li $v0, 4
    la $a0, msg3
    syscall
    j segundo                 # Loop de repetição 

fazdiv:
    div $t0, $t1
    mflo $t2
    li $v0, 4
    la $a0, msg4
    syscall
    li $v0, 1
    move $a0, $t2
    syscall
    li $v0, 10
    syscall
