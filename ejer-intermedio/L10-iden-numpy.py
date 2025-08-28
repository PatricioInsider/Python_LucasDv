import numpy as np

def iden_numpy():
    """Crea un programa que pida al usuario la dimensión y cree la matriz identidad de orden correspondiente con
numpy, empleando las librerias
    """

    n = int(input("Ingrese la dimensión de la matriz identidad: "))
    
    matriz= np.identity(n)
    for i in range (n):
        for j in range(n):
            matriz[i,j] = int(input(f"Elemento[{i+1}] [{j+1}] : "))
    print(matriz)



if __name__ == "__main__":
    iden_numpy()