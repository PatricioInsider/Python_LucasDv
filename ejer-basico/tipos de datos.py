#esta en un tipo de dato largo

number_uno = 43
number_dos = 23
resultado = (number_uno + number_dos)
resultado = resultado == number_uno
print(resultado, type(resultado))

#resultados independientes programa cajero automatico

saludame = ("Hola papi, como estas?")
saludame += ("Ya comiste?")
date = ("Hoy es jueves listo para trabajar")
espacio = (" ")
saludame = (saludame + espacio + date)
print(saludame)

print("COMPARACION")
busqueda_subcadena = saludame.find("trabajar")
extraer_subcadena = saludame[1:66]
print(busqueda_subcadena)
print(extraer_subcadena)
comparacion = (saludame == date)
print(("saludame + date"),comparacion)
print(comparacion, type(resultado))

#ya ahora si nos ponemos a trabajar
print("plantilla nueva lista para trabajar")

