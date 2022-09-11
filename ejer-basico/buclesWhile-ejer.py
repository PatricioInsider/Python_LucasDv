# Operadores de iteracion
print('Imprimiendo el bucle while')
i = 1
while i <= 10:
    print(i)
    i += 1 
    if i == 9:
        print("Se rompio el bucle")
        break

# contar5 e3n las letras de las en el sistema ASCII
n = int(input("Intruduce una rotacion"))
i = 65
while  i <= 90:
    if (i + n) <= 90:
        print(chr(i) ,(": ")  ,chr(i + n))
        i += 1
    else:
        print("Fin")
        break 
# Bucle FOR
s = "Alo bien si o si mi reina de la gina"
for b in s:
    print(b)
# Vamos a recorrer un string dado con un bucloe for y loo vamos a devolver imperswoi alk re3ves
s = "Hola cabeza de la gran  vrg"
s_inv = " "
for c in s : # Declaramos la variable, que el caracter es guardado en c 
    s_inv = c + s_inv       # Fijemonos en el  orden de la concatenacion, cada palabra que es extraida es gurdada al lado derecha de la funcion s_inv
print(s_inv)



