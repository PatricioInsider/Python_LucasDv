#EJERCICIO PRACTICO 4

print("number MAYOR DE TRES VALORES")
print("//////////////////////////////")

num_uno = float(input("Ingresa el primer number: "))
num_dos = float(input("Ingresa el segundo number: "))
num_tres = float(input("Ingresa el tercer number: "))

coma = (",")
print(("Los numbers a comparar son: "), num_uno,(" , ") , num_dos,(" y "),  num_tres)

print("COMPARANDO...")


if num_uno > num_dos and num_uno > num_tres :
    print(("El number mayor es "), num_uno,)
else:
    if num_dos > num_tres:
        print(("El number mayor es "), num_dos,)
    else:
        print(("El number mayor es "), num_tres,)
    
    
