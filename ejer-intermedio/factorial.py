def factorial(n):
    """
    calcula el factorial de un numero entero positivo
    Args:
    n: Numero entero positivo
    
    Returns:
    Factorial de n
    
    """
    if n==0:
        return 1
    return n*(n-1)


if __name__ == "__main__":
    n =int(input("Numero, para realizar el factorial: "))
    fact=factorial(n)
    print("El numero factorial de {} es: {}".format(n,fact))