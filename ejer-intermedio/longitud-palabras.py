'''
Crea un programa que pida el número de palabras a introducir. Crear un diccionario de clave la palabra y
de valor la longitud de dicha palabra
'''

def run():
    myDicc = {}
    keys = []
    s = int(input("Introduce el numero de palabras de uno en uno"))
    for _ in range(s):
        keys.append(str(input(" ")))
    
    for key in keys:
        myDicc[key]= len(key)
    
    print(myDicc)

if __name__=='__main__':
    run()