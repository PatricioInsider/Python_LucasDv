#Listas de objetos de las cadenas de los caracteres antes menciuonados 
l = ['Maria', 'Carlos','JUan','Patricio','DEcadencia','Aristocracia', 'Porala']
print(l[-1]) #Se imprime la posicion 
l.append('Final de linea agregado') #Se anade un objeto al final de la lista
print(l)
l.insert(5,"Inicio agregado poosicion 5") #Comando para anadir un objeto a la lista colocando la posicion
print(l)
 #Longuitud de una lista, con loas ordenes de los usuarios

n = int(input('Introduce la longitud de la lista :  ')) ; lista = [] 
for i in range(n): #Aqui se pide el numero de los datos introducidos por el usuario
    lista.append(str(input('Introduce el nombre para agregar\n :' )))
print('Tu lista es',lista)


# Bucles con listas
 
l = ['Juan', 'Pedro', 10, 25]
for i in range(len(l)):
    print(i)

print('Aqui cambiamos de metodo de impresion')

for j in range(len(l)): #La misma funcion, pero mucho codigoi
    print(l[j])

for i in l: # Simplificacion de codigo para imprmir los elementoi sde una lista
    print(i)
 
#Listas anidadas

element1 = [['Maria', 'Pedro', 'Juan'],
            ["juan", [25,45,23],25],2
            ]
            
print(element1)
element1.insert(0,'Andres')

print(element1)

#FUNCION COUNT

counted = ['Maria',1,2,3,4,5,6,7,'Andres']
counted.count(2) #Cuenta los elemenris de la lista 
for i in range(5): #El ultimo numero en el range no es tomado en cuenta 
    print(counted.pop()) #REcoge el ultimo elemento de la lista y lo elimina
print(counted)

#Ejerciom, le damos una lista y el usuario sabe cual quiere eliminar

number = int(input('Numero de elemntos :  '))
lista = []
for i in range (number):
    add = str(input('Introduce un elemento a la lista :  '))
    lista.append(add)
print('Tu lista actual : ', lista)
delete = str(input('Que elemento deseas eliminar'))
for e in lista:
    if e == delete:
        lista.remove(e)
print('Lista nueva', lista)

#Ejercicio, 10 variables ingresadas, orden ascendente o descendente

# desision = bool(input('Ascendente introduce True o descendente False'))
# cadena = []
# for i in range(10):
#     cadena.append(input('Introduce 10 eleemtos a agregar:  '))
# print(cadena.sort())
# print(cadena.sort(reverse=desision))
# print(cadena de caracteres)

print('Sistema decimal a binario')
x = input('agregar el numero  de SD')

if x.isdigit() :
    print('hola')
    while x != 1:
        cod = x % 2
        print(cod, sep= "")
        x /= 2
