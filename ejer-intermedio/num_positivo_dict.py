'''
Crea un programa que pida un número entero positivo por teclado y que cree un diccionario cuyas claves
sean desde el número 1 hasta el número indicado. Los valores de cada clave serán las propias claves elevadas
al cubo
'''

def proceso(end):
    
    myDict = {}
    for i in range(end):
        myDict[i]= i**2
    print(myDict)
        

def run ():
    
    try:
        print("Ese no es un numero positvo")
        try:
            end = int(input("Ingresa un numero entero positivo: "))
            if end<0:
                raise ValueError("Este numero no es positivo")
            proceso(end)
        
        except ValueError as nega:
            print(nega)
    except ValueError:
       print("Algo salio mas dentro del programa")
if __name__=='__main__':
    run()