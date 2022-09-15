'''
Crea un programa que lea números enteros hasta que introduzca el 0 y devuelva un diccionario con la
cantidad números positivos y negativos introducidos.

'''
def run():
    contPositivo =0
    contNegativo =0
    opc = 1
    resul={}
    
    while opc!=0:
        num = int(input("Ingresa un numero positivo o negativo(si se ingresa 0 paramos): "))
        if num > 0:
            contPositivo +=1
        elif num<0:
            contNegativo +=1
        else:
            opc = 0        
            print("gracias por participar")
    resul= {"Numeros Positivos": contPositivo,
            "Numeros Negativos": contNegativo}
    print (resul)

if __name__=='__main__':
    run()