def posicion(n):
    """Programa que lea una matriz 3 x 3 y devuelva el máximo de cada fila

    Args:
        n (int): extension de la matriz cuadrada

    Returns:
        matriz : Secuencia de numeros dentro de una matriz 
    """
    
    matriz = []
    l=0
    for i in range(n):
        aux=[]
        matriz.append(aux)
        for i in range(n):
            aux.append(l);l +=1
    return matriz

if __name__=="__main__":
    n = int(input("Ingresa el n de la matriz"))
    print(posicion(3))