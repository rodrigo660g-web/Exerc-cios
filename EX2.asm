#EX22.Uma fábrica de camisetas produz os tamanhos pequeno, médio e grande, cada uma sendo vendida
#respectivamente por 10, 12 e 15 reais. Construa um algoritmo em que o usuário forneça a
#quantidade de camisetas pequenas, médias e grandes referentes a uma venda, e a máquina informe
#quanto será o valor arrecadado.
.data
msg1: .asciiz "\nQuantidade camisetas P (R$10): "
msg2: .asciiz "\nQquantidade de camisetas M (R$12): "
msg3: .asciiz "\nQuantidade de camisetas G (R$15): "
msg4: .asciiz "\nValor total: R$ "
.text
main:
    li $v0, 4; la $a0, msg1
    syscall
    li $v0, 5
    syscall
    mul $t0, $v0, 10         # $t0 = qtdp * 10

    li $v0, 4
    la $a0, msg2
    syscall
    li $v0, 5
    syscall
    mul $t1, $v0, 12         # $t1 = qtdm * 12

    li $v0, 4
    la $a0, msg3
    syscall
    li $v0, 5
    syscall
    mul $t2, $v0, 15         # $t2 = qtdg * 15

    add $t3, $t0, $t1        # $t3 = subtotal (P + M)
    add $t3, $t3, $t2        # $t3 = total P + M + G

    li $v0, 4
    la $a0, msg4
    syscall
    li $v0, 1
    move $a0, $t3
    syscall
    li $v0, 10
    syscall
