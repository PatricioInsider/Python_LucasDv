def identidad():
    """Crear un programa determina si la matriz introducida manualmente (tanto sus dimensiones como los elementos) se trata de la matriz identidad. Recuerda que la matriz identidad debe ser una matriz cuadrada.
    Args: 
    """
    print("Elementos de una matriz ")
    n = int(input("n = "))
    m = int(input("m = "))
    
    matriz = []
    if n != m :
        exit()
    else:
        print("Es una matriz identidad o cuadrada")
    
    for i in range (n):
        aux =[]
        matriz.append(aux)
        for j in range(m):
            aux.append(int(input(f"Elemento[{i+1}] [{j+1}] : ")))
    print(matriz)

if __name__ == "__main__":
    identidad()