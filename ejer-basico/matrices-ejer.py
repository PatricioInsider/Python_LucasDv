#VAmos a sumar dos matrices con  numpy. Ambas matrices las proporcionara el usuario, asi como sus dimensiones
#aplicaciones de escritorios
from re import A
import numpy as np



n = int(input("Ingresa el numero de filas de la matriz- "))
m = int(input("Ingresa el numero de columnas de la matriz- "))
m1 = np.empty((n,m))
for i in range(n):
    for j in range(m):
        m1[i,j] = float(input('Ingresa los datos ({}, {})'.format(i,j) ))

print(m1)
print('+')

n = int(input("Ingresa el numero de filas de la matriz- "))
m = int(input("Ingresa el numero de columnas de la matriz- "))
m2 = np.empty((n,m))
for i in range(n):
    for j in range(m):

        m2[i,j] = float(input('Ingresa los datos ({}, {})'.format(i,j) ))
        
print(m2)

print('Resultado')
resul = m1.dot(m2)
print(resul)

