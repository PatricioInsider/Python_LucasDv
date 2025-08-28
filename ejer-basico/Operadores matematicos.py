#Operadores relacionales
nombre = input("¿Cual es tu nombre?\n")
edad = input(str("¿Cuantos años tienes?\n"))
if edad <= ("18") :
    print("Wow, eres muy joven. Eso me agrada!!")
else:
    print("Estas aprendiendo, me gusta que los humanos aprendan!!")
    
print(("hola, ") + nombre + (" te puedo ayudar en algo?"))

opcion = input(str( nombre + (", Si deseas que yo te ayude a resolver problemas aritmeticos basicos, presiona 1, si no lo quieres presiona 2\n")))
if opcion == ("1"):
    print("Okey me gustaria ayudarte, ")
    opc_int = str(input("ACTIVIDADES: presiona\n Suma = 1\n Resta = 2\n Multiplicacion = 3\n Division = 4\n Literal: "))

    if opc_int == ("1"):
        print("SUMA\n")
        num_uno = float(input("Ingresa un number para sumar"))
        num_dos = float(input("Ingresa otro number para sumar"))
        resultado = (num_uno + num_dos)
        print(("Tu resultado es: "), round((resultado),3))
    elif opc_int == ("2"):
        print("RESTA\n")
        num_uno = float(input("Ingresa un number para restar"))
        num_dos = float(input("Ingresa otro number para restar"))
        resultado = (num_uno - num_dos)
        print(("Tu resultado es: "), round((resultado),3))

    elif opc_int == ("3"):
        print("MULTIPLICACION\n")
        num_uno = float(input("Ingresa un number para nultiplicar"))
        num_dos = float(input("Ingresa otro number para multiplicar"))
        resultado = (num_uno * num_dos)
        print(("Tu resultado es: "), round((resultado),3))
        
    elif opc_int == ("4"):
        print("DIVISION\n")
        num_uno = float(input("Ingresa un number para dividir"))
        num_dos = float(input("Ingresa otro number para dividir"))
        resultado = (num_uno / num_dos)
        print(("Tu resultado es: "), round((resultado),3))

    else:
        print("No has ingresado una orden")


elif opcion == ("2"):
    print ("Bueno, sera para la proxima")

else:
    print(nombre + (", no escribiste uno de los literales"))

print(("Gracias por usar mi sistema ") + nombre)
    
    
