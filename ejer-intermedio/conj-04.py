def con_primos(n):
    primes = set(range(2,n+1)) #creamos un conjunto con la funcion set y range (de,hasta,salto)
    numbers = list(range(2,n+1))
    multiples = [True for z in range (len(numbers))] #inicializamos todas las casillas de la lista son verdadero
    
    for i in range (len(numbers)): # Recorremos la lista principal la cual almacenara solo los primos (por aquello los vamos eliminando a los sobrantes)
        if multiples[i] == False:
            continue
        for j in range(i+1,len(numbers)):
            if numbers[j] % numbers[i] == 0:
                multiples[j] = False                
                primes.discard(numbers[j])
            
    
    
    pass

if __name__=="__main__":
    n= int(input("Introduce un numero entero mayor que 2: "))
    con_primos(n)