'''
Vamos a leer un string por teclado y vamos a devolver un diccionario con la cantidad de apariciones de cada caracter en el string proporcionado por el usuario.
'''

def seens(cadena):
    
    cadena =cadena.lower()
    myList=[]
    dicc = {}
    
    for i in cadena:
        if i not in myList and i != " ":
            #Metodo .upper(capitalizar un caracter) / Metodo .count(variable) sirve para contar las apariciones en un string el caracter variable
            dicc[i.upper()] = cadena.count(i)
            myList.append(i)
    print(dicc)

def run():
    
    cadena = str(input("Ingresa un string por teclado : "))
    seens(cadena)

if __name__=='__main__':
    run()