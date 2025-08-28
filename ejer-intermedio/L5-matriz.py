def max_fila(m1):
    """programa que lea una matriz 3 x 3 y devuelva el máximo de cada fila

    Args:
        m1 (int): matriz ingresada que se evalua  

    Returns:
        maximos: lista que contiene el numero mayor de cada fila de la matriz ingresada
    """
    
    maximos = []
    
    for fila in m1:
        aux = max(fila) #obtiene el maximo de la fila, y si lo cambiamos por min, obtenemos el minimo de la misma 
        maximos.append(aux)
    return maximos

if __name__=="__main__":
    #matriz cuadrada ingresa el numero 3x3
    m1 =[[5,3,6],[9,0,4],[2,4,6]]
    print(max_fila(m1))