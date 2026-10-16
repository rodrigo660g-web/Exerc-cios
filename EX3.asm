#EX3 3.A empresa Hipotheticus paga R$10,00 por hora normal trabalhada, e R$15,00 por hora extra. Faça
#um algoritmo para calcular e imprimir o salário bruto e o salário líquido de um determinado
#funcionário. Considere, também, uma entrada de desconto para calcular o salário líquido.
.data
msg1: .asciiz "\nHoras normais: "
msg2: .asciiz "\nHoras extras: "
msg3: .asciiz "\nValor do desconto: "
msg4: .asciiz "\nSalario Bruto: R$ "
msg5: .asciiz "\nSalario Liquido: R$ "
.text

main:
    li $v0, 4
    la $a0, msg1
    syscall
    li $v0, 5  
    syscall
    mul $t0, $v0, 10          # Valor horas normais

    li $v0, 4
    la $a0, msg2
    syscall
    li $v0, 5     
    syscall
    mul $t1, $v0, 15          # Valor horas extras

    li $v0, 4
    la $a0, msg3
    syscall
    li $v0, 5
    syscall
    move $t2, $v0             # Desconto

    add $t3, $t0, $t1         # Salario Bruto = Normais + Extras
    sub $t4, $t3, $t2         # Salario Liquido = Bruto - Desconto

    li $v0, 4
    la $a0, msg4
    syscall
    li $v0, 1
    move $a0, $t3
    syscall

    li $v0, 4
    la $a0, msg5
    syscall
    li $v0, 1
    move $a0, $t4
    syscall

    li $v0, 10
    syscall
