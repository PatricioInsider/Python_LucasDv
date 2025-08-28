'''
Crea un programa que pida el número de palabras a introducir. Crear un diccionario de clave la palabra y
de valor el número de vocales de la palabra.
'''

#Contador de letras en una cadena
def cont(key):
    contador = 0
    for letra in key:
        if letra.lower()in "aeiou":
            contador +=1
    return contador

def run():
    myDicc = {}
    keys = []
    s = int(input("Introduce el numero de palabras de uno en uno"))
    for _ in range(s):
        keys.append(str(input(" ")))
        
    for key in keys:
        myDicc[key]= cont(key)
    print(myDicc)

if __name__=='__main__':
    run()