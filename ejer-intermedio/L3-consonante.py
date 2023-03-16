def consonantes_list(str1):
    """programa que lea un string y guarde en una lista todas las consonantes

    Args:
        str1 (str): texto que se desea precesar

    Returns:
        list: lista integrada por las consonantes de la oracion 
    """
    
    cons = []
    for letter in str1:
        if letter.isalpha() and letter.lower() not in "aeiou":
            cons.append(letter)
    return (cons)

if __name__=="__main__":
    aux = "String de prueba" #oracion alterable
    print(consonantes_list(aux))
    