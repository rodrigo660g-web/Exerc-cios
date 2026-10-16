#A imobiliária Imóbilis vende apenas terrenos retangulares. Faça um algoritmo para ler as
#dimensões de um terreno e depois exibir a área do terreno.
.data
msg1: .asciiz"\n Qual o comprimento?"
msg2: .asciiz"\n Qual a largura?"
msg3: .asciiz"\n A área total é:"
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
	
	mul $t2, $t1, $t0
	
	li $v0, 4
	la $a0, msg3
	syscall
	
	li $v0, 1
	move $a0, $t2
	syscall
	
	li $v0, 10 
	syscall
	