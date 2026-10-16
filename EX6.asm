#Ex5 5.Faça um algoritmo que receba o valor dos catetos de um triângulo, calcule e mostre o valor da
#hipotenusa.
.data
msg1: .asciiz "Digite o valor do cateto oposto: "
msg2: .asciiz "Digite o valor do cateto adjacente: "
msg3: .asciiz "Resultado da hipotenusa é: "
.text
main:
    li $v0, 4
    la $a0, msg1
    syscall
    li $v0, 5
    syscall
    move $t1, $v0

    li $v0, 4
    la $a0, msg2
    syscall
    li $v0, 5
    syscall
    move $t2, $v0
    
    mul $t1, $t1, $t1               # CO^2
    mul $t2, $t2, $t2               # CA^2
    add $t3, $t1, $t2               # CA^2 + CO^2
    sqrt , $t3                # sqrt(CO^2 + CA^2) -> 

    li $v0, 4
    la $a0, msg3
    syscall
    li $v0, 1
    syscall                
    li $v0, 10
    syscall

 # .data
#msg_c1: .asciiz "Cateto 1: "
#msg_c2: .asciiz "Cateto 2: "
#msg_hip: .asciiz "Hipotenusa: "

#.text
#main:
 #   li $v0, 4; la $a0, msg_c1; syscall
  #  li $v0, 6; syscall                # Read float -> $f0
   # mov.s $f1, $f0

    #li $v0, 4; la $a0, msg_c2; syscall
    #li $v0, 6; syscall                # Read float -> $f0
    #mov.s $f2, $f0

    #mul.s $f1, $f1, $f1               # c1^2
    #mul.s $f2, $f2, $f2               # c2^2
    #add.s $f3, $f1, $f2               # c1^2 + c2^2
    #sqrt.s $f12, $f3                  # sqrt(c1^2 + c2^2) -> $f12

   #li $v0, 4; la $a0, msg_hip; syscall
    #li $v0, 2; syscall                # Print float em $f12
    #li $v0, 10; syscall