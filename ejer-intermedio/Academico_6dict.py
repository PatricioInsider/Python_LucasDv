'''
Crea un programa que permita al usuario introducir los nombres de los alumnos de una clase y las notas que
han obtenido. Cada alumno puede tener distinta cantidad de notas. Guarda la información en un diccionario
cuyas claves serán los nombres de los alumnos y los valores serán listas con las notas de cada alumno.
El programa va a pedir el nombre de un estudiante e irá pidiendo sus notas (del 1 al 10) hasta que introduzcamos un 0. Al final, cuando el nombre que introduzcamos sea un string vacío, el programa nos mostrará la
lista de alumnos y la nota media obtenida por cada uno de ellos.
PISTA: Vas a necesitar la función sum()
'''
def notas(names):
    myDicc= {}
    lisNotas = []
    for name in names:
        print("NOTAS DE (1 al 10)", name)
        aux = 1
        while aux != 0:
            nota = int(input("nota  : "))
            if nota < 11 and nota >0:
                lisNotas.append(nota)
            else:
                print("nota fuera de rango, siguiente alumno")
                aux=0
        myDicc[name] = sum(lisNotas)     
        
    print("Nombre del alumno y notas obtenidas")  
    print(myDicc) 



def run():
    
    names=[]
    
    #Agregar las personas al listado
    for _ in range(1000):
        name = str(input("Ingresa el nombre de los estudiantes (vacio para finalizar): "))
        if name == '':
            break
        else:
            names.append(name) 
    notas(names)
                  
        
        


if __name__=='__main__':
    run()