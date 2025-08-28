#eliminacion de elementos en un diccionario, introduciendo su clave

def run():
    myDicc = {
        "User 1":45,
        "User 2":6,
        "User 3":89,
        
    }
    print(myDicc)
    
    try:
        valu = str(input("Que clave deceas eliminar: "))
        myDicc.pop(valu)
        
        print(myDicc)
        
    except ValueError:
        print("Ingresa un numero un numero")
    
if __name__=='__main__':
    run()