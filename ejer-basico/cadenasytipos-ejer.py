# Ejercicios basicos 1
#EJERCICIO 1
s1 = "Había una vez, "
s2 = "un barquito chiquitito "
s3 = "que no podía, "
s4 = "que no podía navegar."
print((s1+s2)*2+s3*2+s4)

# EJERCICIO 2
print("Érase un hombre a una nariz pegado,\nÉrase una nariz superlativa,\nÉrase una alquitara medio viva,\nÉrase un peje espada mal barbado;")

# EJERCICIO 3
s = "me encantan las matemáticas"
print(s.upper())

#Ejercicio 4
s = "Mi pasión por el chocolate es superior a mis fuerzas"
print(len(s))

#Ejercicio 5
palabra= "chocolate"
inicio =len(palabra)
e_sub = s.find("chocolate",0)
print(e_sub)
print(s[e_sub:(e_sub+inicio)])

# EJERCICIO 6
nombre=input("Introduce tu nombre ..")

# EJERCICIO 7
apellido=input("Introduce tu apellido ..")

# EJERCICIO 8
edad=str(input("Introduce tu edad"))

# EJERCICIO 9
ciudad=str(input("Introduce tu ciudad de residencia"))

# EJERCICIO 10

#Ejercicios de transformacion de la cadenas
nombre=input("Introduce tu nombre :").capitalize()
apellido=input("Introduce tu apellido :").capitalize()
edad=str(input("Introduce tu edad :")).capitalize()
ciudad=str(input("Introduce tu ciudad de residencia :")).capitalize()
print("Su nombre es {} {}, tiene {} años y actualmente vive en {}".format(nombre,apellido,edad,ciudad))
print("hola mi amigo"+"mascara")

title= "se busca tripulante\n"
message1 = "se ofrece puesto en la tripulación del capitán pyratilla para llevar a cabo labores de marinero.\n"
message2 = "comida y bebida garantizada a lo largo de toda la aventura.\n"
contact = "para más información, ir al puerto y buscar al capitán pyratilla, ya famoso en este pueblo costero (evitar preguntar en el casino).\n"
message1, message2 =message1.capitalize(), message2.capitalize()
message1 =message1.replace("pyratilla", "PYRATILLA")
message = (message1+message2) 
contact = contact.replace("pyratilla", "PYRATILLA")

print(title.upper()+ message+ contact.capitalize())
message1 =message1.replace("pyratilla", "PYRATILLA")
palabra = message1[message1.find("pyratilla",0):message1.find("pyratilla",0)+9].upper()
message1, message2 =message1.replace("pyratilla", palabra), message2.replace("pyratilla", palabra)