'''
Crea un programa que pida un número entero positivo por teclado y que cree un diccionario cuyas claves
sean desde el número 1 hasta el número indicado. Los valores de cada clave serán tantos símbolos "*" como
indique la clave.
'''


def claves(num):
    x= ""
    for i in range(num):
        x += "*"
    return x
def run():
    
    myDicc = {}
    aux =0
    
    while aux == 0:
        num = int(input("Ingresa un numero: "))
        if num>0:
            aux=1
    
    for i in range(num+1):
        myDicc[i]= claves(i)
            
    print(myDicc)

if __name__=='__main__':
    run()