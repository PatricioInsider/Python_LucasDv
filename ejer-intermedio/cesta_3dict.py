'''
Escribe un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar
el artículo y su precio por unidad. El artículo será la clave y el valor el precio, hasta que el usuario decida
terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato
'''
def menu():
    print("Deceas agregar un articulo a la cesta de compras")
    print("0 = si")
    print("1 = no")
    
def formato(cesta):
     # Impresion del diccionario en el formato solicitado
    prieceTotal=0
    
    print("----------------\n Lista de Compras\n------------------")
    for key,valu in cesta.items():
        prieceTotal += valu
        print(key+"\t",valu)
    print("Total\t ", prieceTotal)    

def run():
    
    cesta = {}
    opc =0
    while opc == 0:
        menu()
        try:
            opc= int(input("eleccion: "))
            if opc==1:
                break
            nameProduct = str(input("Ingresa el articulo: "))
            cesta[nameProduct] = float(input("Precio: "))
        except ValueError: 
            print("No se siguieron las ordenes solicitadas--Cierre de programa")   
            
    formato(cesta)

if __name__=='__main__':
    run()