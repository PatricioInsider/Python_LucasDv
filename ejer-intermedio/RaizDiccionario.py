'''Realizar un diccionario en el cual se guarde como llave el numero del 1 al 100 y como valor su raiz cuadrada'''
import math as mat
def run():
    
    dicc ={i:round(mat.sqrt(i),2)#round() Es para redondear las cifras decimales
        for i in range(1.1001) if i%3 !=0}
    print (dicc)

if __name__=='__main__':
    run()