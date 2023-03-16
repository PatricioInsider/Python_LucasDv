def max_fila(m1):
    maximos = []
    
    for fila in m1:
        aux = min(fila)
        maximos.append(aux)
    return maximos

if __name__=="__main__":
    #matriz cuadrada ingresa el numero 3x3
    m1 =[[5,3,6],[9,0,4],[2,4,6]]
    print(max_fila(m1))