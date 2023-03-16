""" Vamos a crear una funcion que muestre por pantalla el triangulo de pascal. por parametro se indicara el numero de filas
a mostrar.por degecto n valdra 1, calcular el numero combinatorio en python
"""
import math as ma

def choose(n,k):
    
    """calcula el numero combinarorio n sobre k
"""
    if(n>= k and k>=0):
        return ma.factorial(n) / (ma.factorial(n-k))
    else:
        return "No se  puede calcular el numero dctorial indicado"
def run(n=10):
    print(1)
    for i in range (1,n+1):
        for k in range(i+1):
            print(choose(i,k), end = " ")
        print("")
    
    


if __name__=="__main__":
    run()