#Imprimir del numero 1 al 100 y sus cuadrados guardados en una lista, que no sehan divisibles entre 3
from ast import If


def run():
    square =[]
    for i in range(1,101):
        #condicion que no sehan  divisibles para 3
        if (i%3) ==0:
            pass #Le dice al programa que continue su ejecucion
        else:
            square.append(i**2)
            print("Numero {} , al cuadrado es = {}".format(i,i**2))
        
    print("Impresion de los numeros naturales que cumplen la condicion")
    print(reduce(square))

if __name__ == '__main__':
    run()    