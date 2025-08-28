'''Crea un programa que lea una secuencia de caracteres, guarde cada caracter en una posición de una lista '''

from ast import For
from random import randint
oracion = str(input("Esctibe una secuencia de caracteres \n"))
secuencia = []
posicion = 0
for caracter in oracion:
   posicion += 1
   secuencia.append(" {} , se guardo en la posicion {} \n".format(caracter, posicion))

print(secuencia)

dic = [1,"a",3,1]
print(dic.pop(1))#Imprimir del array la posicion 1 (En python se comienza desde 0)
print(dic,"🔥")

# Operadores de iteracion
print('Imprimiendo el bucle while')
i = 1
while i <= 10:
    print(i)
    i += 1 
    if i == 9:
        print("Se rompio el bucle")
        break

#Contar el numero de letras dentro de una cadena de texto 
s = "Decadencia"
print(s)