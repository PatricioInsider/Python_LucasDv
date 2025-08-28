def palindromo_list(str1):
    """Crea un programa que lea una palabra, la guarde en una lista y compruebe si se trata de un palíndromo.

    Args:
        str1 (str): cadena ingresada

    Returns:
        list: lista del palindromo separado por letras
    """
    str1 = str1.replace(" ", "").lower()
    
    if str1 == str1[::-1]:
        print("La cadena es un palíndromo.")
        return list(str1)
    else:
        print("La cadena no es un palíndromo.")
        exit()
    

if __name__=="__main__":
    str1= "Dabale arroz a la zorra el abad"
    print(palindromo_list(str1))