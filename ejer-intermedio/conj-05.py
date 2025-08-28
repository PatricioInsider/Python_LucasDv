def maximo():
    """Vamos a crear un programa que nos devuelva el elemento maximo de unn conjunto sin utilizar la funcion max()
    """
    
    myset = {2,3,5,10,9,-1,-5,-3}
    max  =-99999#se emplea un numero menor en la variable para asegurarnos que esta no podra ser menor a una cantidad del conjunto
    for e in myset:
        if e> max:
            max =  e
    
    print(f"el maximo de {myset} es {max}")
    pass

if __name__ == "__main__":
    maximo()