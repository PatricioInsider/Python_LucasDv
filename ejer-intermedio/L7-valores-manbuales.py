#Crea una matriz de n × m y asigna los valores manualmente. El programa debe indicar si la suma de cada
#columna es el mismo valor.
def mismo_valor(n,m):
    """
    Crea una matriz de n × m y asigna los valores manualmente. El programa debe indicar si la suma de cada
#columna es el mismo valor.
    
    Arg:
    n (int) : filas
    m (int) : columnas
    """
    matriz = []
    
    l=0
    for i in range (n):
        aux =[]
        matriz.append(aux)
        for j in range(m):
            aux.append(int(input(f"Elemento[{i+1}] [{j+1}]2 : "))); l +=1
    print(matriz)
    
    sumColumna = []
    #suma de cada uno de las columnas
    for i in range(m):
        suma =0
        for j in range (n):
            suma += matriz[j][i]
        sumColumna.append(suma)
    print (sumColumna)
    
    #verificar si cada columna es del mismo valor
    """Finalmente, el programa utiliza la función all() para verificar
    si todos los elementos de la lista sumas son iguales al primer elemento de la lista sumas.
    """
    if all(x == sumColumna[0] for x in sumColumna):
    
        print("La suma de cada columna es el mismo valor: ", sumColumna[0])
    else:
        print("La suma de cada columna no es el mismo valor")

if __name__=="__main__":
    print("Elementos de una matriz ")
    n = int(input("n = "))
    m = int(input("m = "))
    mismo_valor(n,m) 
