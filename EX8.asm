#EX8 Encontrar o dobro de um número caso ele seja positivo e o seu triplo caso seja negativo,
#imprimindo o resultado.
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

    bgez $t0, positivo      # Se $t0 >= 0 salta para positivo

    # Se for negativo:
    mul $t1, $t0, 3
    j fim

positivo:
    mul $t1, $t0, 2

fim:
    li $v0, 4
    la $a0, msg2
    syscall
    li $v0, 1
    move $a0, $t1
    syscall
    li $v0, 10
    syscall
