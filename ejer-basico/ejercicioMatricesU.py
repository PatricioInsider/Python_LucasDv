#FvAMOS A CREAR MANUALMENTE UNA MATRIZ DE TAMAÑP 4X4 BY GUARDARLA EN UNA LISTA
from sqlite3 import Row
#las matricez se clasifican en n x m

# matriz = []
# for i in range (4):
#     matriz.append([])
#     print('Ingresa: ', i)
#     for j in range(4):
#         matriz[i].append(float(input('Introduce el elemento {}, {} :'.format(i,j))))
# for row in matriz:
#     print(row)



#Suma de matricez dadas por el usuario
n = int (input('Numero de filas: '))
m = int (input('Numero de columnas: '))

matrizResul = []

print('Primera matriz')
matrizUno = []
for i in range (n):
    matrizUno.append([])
    print('Ingresa: ', i)
    for j in range(m):
        matrizUno[i].append(float(input('Introduce el elemento {}, {} :'.format(i,j))))

for row in matrizUno:
    print(row)
    print('Segunda matriz')

matrizDos = []
for k in range (4):
    matrizDos.append([])
    print('Ingresa: ', k)
    for l in range(4):
        matrizDos[k].append(float(input('Introduce el elemento {}, {} :'.format(k,l))))

for row in matrizDos:
    print(row)
#Proceso de suma de matrices
