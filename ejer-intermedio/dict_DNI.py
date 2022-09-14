'''
Vamos a solicitar al usuario 8 números enteros del 0 al 9. Se supone que son los números de su DNI, que guardaremos cada uno de los digitos de una entrada en una lista.
A continuación, con esos números calcularemos la letra correspondiente y la guardaremos en una variable.
Finalmente, crearemos un diccionario con dos claves, cada una guardará, respectivamente, los números y la letra del DNI. Finalmente, mostraremos el diccionario resultante.
'''

LETTERS = {0: "T", 1: "R", 2: "W", 3: "A", 4: "G", 5: "M", 6: "Y",
           7: "F", 8: "P", 9: "D", 10: "X", 11: "B", 12: "N", 13: "J",
           14: "Z", 15: "S", 16: "Q", 17: "V", 18: "H", 19: "L", 20: "C",
           21: "K", 22: "E"}

def conversion_cadena(dniSep,extension):
    #Cambiamos de nuevo a un string
    num=""
    for i in range(extension):
        num += dniSep[i] 
    letter = LETTERS[int(num)%23]
    DNI ={"numbers":dniSep,"letter":letter}
    print(DNI)
    pass
    
    

def run():
    
    try:
        try:
            dni =str(input("Ingresa tu DNI sin (-) : "))
            dniSep = []
            lar=len(dni)
            if lar!=10:
                raise ValueError("Los dijitos deben ser 10")
            for i in range (lar): #cuando no te interesa guardar la variable i, se puede cambiar por una _
                dniSep.append(dni[i])
            conversion_cadena(dniSep,lar)
        except ValueError as noCantidad:
            print(noCantidad)
    except ValueError:
        print("No se ingreso correctamente")
    
    
    
    
    
if __name__=='__main__':
    run()