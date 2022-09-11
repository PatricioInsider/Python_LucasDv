# Tablas de multiplicar
for i in range(1,11): #iNDICA LAS TABLAS QUE SE VAN A TOMAR
    print("\nTabla del multiplicar del {}".format(i))
    continue
    for j in range(1,13): # TOMA EL NUMERO POR LOS CUALES SE VAN A MULTIPLICAR
        print("{} x {} = {} ".format(i,j,i*j))
print("Hello my mom {}")

#Realizar un ejercicio para entender mejor for 

for i in range(1,20,2):
    print (i, 'and', i*2)

# TAREA DEL EJERCICIO

# Haz que el usuario introduzca números ente1ros por teclado. Mientras el usuario no introduzca el 0, muestra
# si el número introducido es par o impar. :
print('Ingesa unh numero entero que no sea 0')
num = int(input('x = '))
arg = ('El numero {} es '.format(num))
if num != 0 :
    if (num %2) == 0:
        print(arg,'par')
    else:
        print(arg,'impar')
print('Recuerda que el numero debe ser diferente a 0')

# EJERCICIO 2
#Haz que el usuario introduzca una palabra y una letra por teclado. Comprueba si la palabra contiene la
#letra o no e indícaselo al usuario por pantalla.

print('Introduce una palabra y una letra final por teclado')
res = str(input("Respuesta = "))
solve = ('La respuesta es:')
long = len(res)
res.islower(); letter = res[(long-1):long]
if res.endswith('a') or res.endswith('e') or res.endswith('i') or res.endswith('o') or res.endswith('u'):
    print(solve, 'Correcta y la letra es', letter )
else:
    print(solve, 'incorrecta, por que no contiene la letra y tiene una consonante ' + letter)

#EJERCICIO 3
""" Haz que el usuario introduzca precios por teclado (si introduce 0, entonces es que ha finalizado). Si el usuario
pasa de 200€, entonces ya no debe poder introducir más precios pues se ha pasado de presupuesto. Sea cual
sea el resultado (o bien el precio final o bien que no tiene más presupuesto), indícaselo por pantalla al usuario. """
user = str(input('Introduce tu nombre de usuario\n'))
print('Vamos a introducir los precios por teclado \n')
limit = float(input('Introduce el limite en Euros : ..\n.'))
total = 0
i = float(input('Introduce el precio: \n'))
while i != 0:               #Se ingresa los valores i, que es el ingreso de la variable precio
    total += i
    i = float(input('Introduce el precio: \n'))
    if total >= limit:
        print('Haz sobre pasado el presupuesto', total)
        break
print('Terminaste de agregar valores, teniendo un total de',total)
 

# Ejercicio 4
""" Haz que el usuario introduzca números enteros por teclado. Mientras el usuario no introduzca el 0, calcula
cuántos números positivos y cuántos negativos ha introducido y muéstraselo al final. """
print('Introduzca un numero positivo o negativo, al colocar 0 termina el conteo')
numPos = 0
numNeg = 0
x = int(input('Introduce un numero positivo o negativo = \n '))
while x != 0:
    x = int(input('Introduce un numero positivo o negativo = \n '))
    if x >= 0:
        numPos += 1
    elif x <= 0:
        numNeg += 1
    else:
        print('No es un numero aceptable')

print('TEermino el conteo..\nNumeros Positivos = {}\nNumeros negativos = {}'.format(numPos, numNeg))
 
#EJERCIOCIO 5
""" Haz que el usuario introduzca números por teclado. Mientras el usuario no introduzca el 0, pídele otro
número. Cuando el usuario introduzca el 0, muéstrale la media aritmética de los números que ha introducido. """

print('Introduzca numeros enteros, y al presionar 0 se sacara la media aritmetica de los numeros ya procesados')
medArit = 0
numdat = 0
x = int(input('Introduce un numero = \n '))
while x != 0:
    medArit += x
    numdat += 1
    x = int(input('Introduce otro numero o 0 para cancelar = \n '))

if x == 0:
    res = medArit/numdat
    print('La media aritmetica es: ',(medArit/numdat) )

#EJERCICIO 6
"""Haz que el usuario introduzca dos números enteros por teclado. El primero será el extremo izquierdo del
intervalo y, el segundo, el extremo derecho. Imprime todos los números que se encuentren entre los dos
números introducidos por el usuario (los extremos incluidos).  """

print('Introduce 2 numeros enteros para formar intervalos')
xizq = int(input('Numero (extremo izquierdo) = \n')) 
xder = int(input('Numero (extremo derecho) = \n'))
for i in range(xizq, (xder+1)):
    print(i, end="- ")

#EJERCICIO 7
""" Haz que el usuario introduzca dos números enteros por teclado. El primero será el extremo izquierdo del
intervalo y, el segundo, el extremo derecho. Imprime la suma de todos los múltiplos de 3 que se encuentren
entre los dos números introducidos por el usuario (los extremos incluidos). Finalmente, muestra por pantalla
el resultado de la suma. """

print('Introduce 2 numeros enteros para formar intervalos(Se sumira los multiplos de 3)')
xizq = int(input('Numero (extremo izquierdo) = \n')) 
xder = int(input('Numero (extremo derecho) = \n'))
sum_tot = 0
for i in range(xizq, (xder+1)):
    if (i % 3) ==0:
        sum_tot += i
print('La suma total de los multiplos de 3 es', sum_tot)

# EJERCICIO 8
# Pídele al usuario cuántos números va a introducir. Con un bucle for, solicítale esa cantidad de números y
# calcula su producto.
print('Ingresa cuantos numeros deseas introducir')
desea = int(input('Cantidad de numeros a introducir = '))
product = 0

for i in range(0, desea):
    product += i
print(product)

 #EJERCICIO 9
# Haz que el usuario introduzca su edad y el año actual. Imprime todos los años que han pasado desde su año
# de nacimiento hasta el año actual (ambos incluidos).

age = int(input('Edad =  '))
year = int(input('Año actual =  '))
for i in range(year-age,year+1):
    print(i, end = '- ')

#EJERCICIO 10
#""" Haz que el usuario introduzca un número entero. Muestra un cuadrado y luego un triángulo rectángulo de
#lado y altura, respectivamente, el número entero introducido. Por ejemplo, si el usuario introduce como
#número 5, se deberá mostrar: """

x = int(input("Introduce un numero entero para formar las figuras"))
for i in range(0, x):
    i = "*"
    print(i*x) 

s = int (input('Introduce un numero para el triiangulo rectangulo'))
for j in range (0, s):
    l = '*'
    j = l
    print(j)
    j = (j + l)

# Cancion de pyratilla
""" De tantas solicitudes que ha recibido, Pyratilla no cabe en sí de la emoción y se pone a cantar

"99 bottles of rum on the wall, 99 bottles of rum.
Take one down, pass it around, 98 bottles of rum on the wall.
98 bottles of rum on the wall, 98 bottles of rum.
Take one down, pass it around, 97 bottles of rum on the wall..." """
#While

print('******************************\nCancion de PYRATILA')


botellas = int(input('Introduce el numero de botellas'))

while botellas != 0:
    print('{} bottles of rum on the wall, {} bottles of rum.'.format(botellas, botellas))
    botellas -= 1
    print('Take one down, pass it around, {} bottles of rum on the wall.'.format(botellas))


#for
botellas = int(input('Introduce el numero de botellas'))
for i in range(botellas):
    print('{} bottles of rum on the wall, {} bottles of rum.'.format(botellas, botellas))
    botellas -= 1
    print('Take one down, pass it around, {} bottles of rum on the wall.'.format(botellas))



 #For tabla de multiplicar
for i in range(99,0,-1):
  print("{} bottles of rum on the wall, {} bottles of rum.\n".format(i,i))
  print("Take one down, pass it around, {} bottles of rum on the wall.".format(i-1))  