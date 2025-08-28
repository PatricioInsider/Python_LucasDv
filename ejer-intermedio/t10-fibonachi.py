
def fibonacci(index):
    """
    Seria de fibonacci, cuando se ingrea un numero menor
    
    Args:
    n : numero maximo en la sucesion de fibonacci
    Return:
    sucesion  
    """
    if index ==0 or index ==1:
        return 1
    return fibonacci (index -1) + fibonacci(index -2)


if __name__ == "__main__":
    print(fibonacci(7))
    