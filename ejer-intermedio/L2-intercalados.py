def intercalar_lista(s1,s2):
    """programa que lea dos strings de la misma longitud, los guarde intercalados en una lista. Por último,
mostrar el contenido de la lista

    Args:
        s1 (str): Primera lista a intercalar en una lista
        s2 (str): Segunda lista a intercalar en una lista
    """
    
    if len(s1) != len(s2):
        print("Los strings deben tener la misma longitud.")
        exit()
    
    res = []
    for i in range (len(s1)):
        res.append(s1[i])
        res.append(s2[i])
    return res
    

if __name__=="__main__":
    s1= "hola caracola"
    s2= "adios marieta"
    print (intercalar_lista(s1,s2))