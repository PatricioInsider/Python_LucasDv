def matriz_transpuesta():
    """Realiza un programa que calcule la matriz transpuesta
    """
    print("Elementos de una matriz ")
    n = int(input("n = "))
    m = int(input("m = "))
    
    if n != m :
        exit()
    else:
        print("Es una matriz identidad o cuadrada")
    
    matriz = []
    for i in range (n):
        aux =[]
        matriz.append(aux)
        for j in range(m):
            aux.append(int(input(f"Elemento[{i+1}] [{j+1}] : ")))
    print(matriz)
    #matriz transpuesta
    
    matrizTrans = []
    for i in range (n):
        aux =[]
        matrizTrans.append(aux)
        for j in range(m):
            aux.append(matriz[j][i])
    print(matrizTrans)
    
    pass

if __name__ == "__main__":
    matriz_transpuesta()