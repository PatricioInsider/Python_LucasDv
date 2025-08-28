""" Crea un programa que lea dos strings de la misma longitud, los guarde intercalados en una lista. Por último,
mostrar el contenido de la lista.
Por ejemplo, si introducimos hola caracola y adios marieta, debería mostrarse haodleao sc
amraarcioeltaa.
 """
def iguales(oracion_uno, oracion_dos):
    oracion=len(oracion_uno)
    oracion2 = len(oracion_dos)

    if oracion == oracion2:
        return True
    else:
        return False


if __name__=='__main__': 
    pass

content = []
oracion_uno = str(input("Oracion 1: \n"))
oracion_dos = str(input("Oracion 2: \n"))
if iguales(oracion_uno, oracion_dos):
    
    for i,j in oracion_uno,oracion_dos:
        content.append(i)
        content.append(j)
        
    print(content)

else:
    print("Las cadenas no son iguales")