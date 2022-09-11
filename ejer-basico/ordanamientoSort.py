
desision = bool(input('Ascendente introduce True de lo contrario no presiones nada '))
cadena = []
for i in range(10):
    cadena.append(input('Introduce 10 eleemtos a agregar:  '))
print(cadena)#Para correr estros nuevos programas primeros se los debe cargar en consoloa 
cadena.sort()
print(cadena)
cadena.sort(reverse=desision)
print(cadena)

