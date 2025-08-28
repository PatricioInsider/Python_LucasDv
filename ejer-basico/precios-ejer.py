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