def secuencia_invertida():
    """_summary_
    Crea un programa que lea una secuencia de caracteres, guarde cada caracter en una posición de una lista y
finalmente muestre la secuencia invertida.

    Args:
    
    
    Return:
    
    """
    x = []
    n = "Secuencia a invertir"
    cont = len(n)
    for i in range(cont):
        x.insert(0,n[i])
    
    
    print(x)
    
    pass

if __name__== "__main__":
    secuencia_invertida()