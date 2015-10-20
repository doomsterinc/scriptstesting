# -*- coding: latin -*-
'''
exiebe somente mensagem
'''
msg = 1

print(msg)

tipo = type(msg)

print(tipo)

#inteiro
var1= 2
#float
var2= 3.14
#complexo
var3= 3 + 4j

print ("Inteiro = ", var1)
print ("Float = ", var2)
print ("Complexo = ", var3)

#convertendo real para inteiro
print ("int(var2) = ", int(var2))

#convertendo interio para real
print("float(var1) = ", float(var1))

#operacoes com numeros complexos
print ("parte real = ", var3.real)
print ("parte imaginaria = ", var3.imag)
print ("conjugado = ", var3.conjugate())

i = 5
j = 7
x = 3.14
y = 2.75 

#somando
print("i + j = ", i+j)
print("x + y = ", x+y)

#subtraindo
print("i - j = ", i-j)
print("x - y = ", x-y)

#multiplicando
print("i * j = ", i*j)
print("x * y = ", x*y)

#dividindo
print("i / j = ", i/j)
print("x / y = ", x/y)

#divisao inteira
print("i // j = ", i//j)
print("x // y = ", x//y)

#modulo da divisao
print("i % j = ", i%j)
print("x % y = ", x%y)

#potencia
print("i ** j = ", i**j)
print("x ** y = ", x**y)

i = 40;
j = 25;

#Decobrindo os valores binários das variáveis
print("i em binário é", bin(i))
print("j em binário é", bin(j))

#Descolamento à esquerda
print("i << 1 = ", bin(i << 1))

#Descolamento à direita
print("j >> 1 = ", bin(j >> 1))

#Operação bit-a-bit E (AND)
print("j & i = ", bin(j & i))

#Operação bit-a-bit Ou (OR)
print("j | i = ", bin(j | i))

#Operação bit-a-bit Ou Exclusivo (XOR)
print("j ^ i = ", bin(j ^ i))

#Operação bit-a-bit Inversão (NOT)
print("~i = ", bin(~i))