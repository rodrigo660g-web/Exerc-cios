#Ex4 4.Faça um algoritmo que calcule e mostre a área de um trapézio usando apenas números inteiros.
#Sabe-se que: A = (base maior + base menor) * altura)/2
.data
msg1: .asciiz "\n Qual o valor da base maior: "
msg2: .asciiz "\nQual o valor da base menor: "
msg3: .asciiz "\nQual o valor da altura: "
msg4: .asciiz "Area do trapezio é: "
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

    li $v0, 4
    la $a0, msg3
    syscall
    li $v0, 5
    syscall
    move $t2, $v0

    add $t3, $t0, $t1         # $t3 = base maior + base menor
    mul $t3, $t3, $t2         # $t3 = (base maior + base menor) * altura
    li $t4, 2
    div $t3, $t4              # Divisão inteira por 2
    mflo $t5                  #Quociente da divisão

    li $v0, 4
    la $a0, msg4
    syscall
    li $v0, 1
    move $a0, $t5
    syscall
    li $v0, 10
    syscall
