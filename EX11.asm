#EX11 11.Escrever um algoritmo que leia uma quantidade desconhecida de números e conte quantos deles
#estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deve terminar
#uando for lido um número negativo.
#*Sabe-se que a entrada deve ser um número entre 0 e 100, validar a entrada para que não permita
#números fora deste intervalo
.data
msg1: .asciiz "\nDigite um numero 0-100, exeto negativos: "
msg2: .asciiz "\n[0-25]: "
msg3: .asciiz "\n[26-50]: "
msg4: .asciiz "\n[51-75]: "
msg5: .asciiz "\n[76-100]: "
.text
main:
    li $t1, 0 # 1
    li $t2, 0 # 2
    li $t3, 0 # 3
    li $t4, 0 # 4

loop:
    li $v0, 4
    la $a0, msg1
    syscall
    li $v0, 5
    syscall
    move $t0, $v0

    bltz $t0, fim            # Se < 0, encerra a leitura
    bgt $t0, 100, loop       # Valida limite maior >100 descarta não valida 

    ble $t0, 25, inc1
    ble $t0, 50, inc2
    ble $t0, 75, inc3
    j inc4
    
inc1: addi $t1, $t1, 1
j loop
inc2: addi $t2, $t2, 1
j loop
inc3: addi $t3, $t3, 1
j loop
inc4: addi $t4, $t4, 1
j loop

fim:
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
