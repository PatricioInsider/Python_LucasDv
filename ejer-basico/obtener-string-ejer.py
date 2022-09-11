print("Ejercicios de clase 31 substring \"Udemy\"")
frase = ("Hola mundo, nosotros somos la rebelion")
print(frase)
datoingresado=input("ingresa una e_sub de la oracion\n")
respuesta = frase.find(datoingresado) #compara la e_sub que ingresara y le dara la posicion
print("De {} caracteres, la e_sub que seleccionaste esta en el caracter {}".format(len(frase), respuesta) )
datin=frase.find(datoingresado)
e_subeliminada = frase[0:datin] + frase[(datin + len(datoingresado))+1: ]  # Eliminamos la e_sub con la longitud que nos da len
print("Si eliminamos la e_sub tu oracion queda:\n {}".format(e_subeliminada))

# EJERCICIO DOS. 
print("Comprobar si un number es par o impar utilizando el operador terceario")
number = input("ingresa un number entero")

def es_numerico(cadena):
    try:
        int(cadena)
        return True
    except ValueError:
        return False

if es_numerico(number) :
    x = 1
    number = int(number)
    if (number% 2) == 0 and x <=5:
        x += 1
        answer_possitive = (("El number {}, es un number par").format(number))
        print(answer_possitive)
        
    else:
        answer_negative = (("El number {}, es un number inpar").format(number))
        print(answer_negative)
   
        # print(answer_possitive) if ( number% 2) == 0 else print(answer_negative)
    
else:
    print(("El number {}, no cumple las caracteristicas como entero").format(number))

# SEGUNDA OPCION
number = input("Ingresa un number entero")
if number.isdigit():
    number= int(number)
    if number% 2 == 0 :

        answer_possitive = (("El number {}, es un number par").format(number))
        print(answer_possitive)
        
    else:
        answer_negative = (("El number {}, es un number inpar").format(number))
        print(answer_negative)
   
        # print(answer_possitive) if ( number% 2) == 0 else print(answer_negative)print("Si funciona jefe")

else:
    print("Ni sabe")

year = int(input("Año: "))
if year % 4 == 0 and year % 100 == 0 and year %400 == 0:
    print("Si es el año biciesto")
else:
    print("no es el año biciesto")
