# Hablaremos de la funcion range 

for i in range(45, 3, -2):
  
    print(i)
#Segunda funcion range print del 0 al 100 que no sonb divisibles entre 2 ni entre 5
for i in range(101):
    print(i)
    if i % 2 == 0  or i % 5 ==0:
        continue
                # no se pone un elfe, porque CONTINUE, por que le saca de la iteracion y continua con la siguiente iteracion
    print(i)

#, ejercicio para eliminar una letra de un string 
s = "Hola madre como estas"
print("Frase original", s)

letter = input("Introduce la letra que deseas eliminar")
for c in s:
    if c == letter:
        continue
    print(c, end = "") 