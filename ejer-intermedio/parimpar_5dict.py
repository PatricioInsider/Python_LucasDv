'''
Crea un programa que lea números enteros hasta que introduzca el 0 y devuelva un diccionario con la
cantidad números pares e impares introducidos
'''

def run ():
    contpar =0
    contimpar =0
    opc = 1
    resul={}
    
    while opc!=0:
        num = int(input("Ingresa un numero(si se ingresa 0 paramos): "))
        
        if num == 0:
            break
        elif num%2 == 0:
            contpar +=1
        elif num%2 == 1:
            contimpar +=1
        else:     
            print("gracias por participar")
    resul= {"Numeros Pares": contpar,
            "Numeros Impares": contimpar}
    print (resul)
    
    pass

if __name__=="__main__":
    run()