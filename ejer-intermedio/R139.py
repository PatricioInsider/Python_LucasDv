
#Forma correcta de realizar una documentacion de una funcion dispuesta por microsoft
def euclidean_division(x,y):
    """Esta funcion calcula el cociente y el resto de la division entera de x entre y

    Args:
        x (_type_): dividendo
        y (_type_): divisor(que no puede ser cero)
    Returns:
    (q,r) tupla con el valor de (cociente, residuo)
    
    """
    q = x//y
    r= x %y
    print(euclidean_division.__doc__)

if __name__=="__main__":
    euclidean_division(x=1,y=1)