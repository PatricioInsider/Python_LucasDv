def fiesta_lista():
    
    #lista de comprad de pyratilla
    fiesta = []
    print("Elementos de una matriz ")
    

    shopping_list = []
    opc =1
    while opc != 2:
        n = str(input("ingresa el producto: "))
        carrito = []
        carrito.append(n)
        shopping_list= shopping_list+carrito
        
        #ingreso de c
        print("1)ingresar elemento    2) Finalizar compra")
        opc = int(input())
        if opc == 2:
            continue
    print(shopping_list)
    #Ordenamos la lista
    #determinamos otra lista con los ya contados
    #estamos que count cuente las aparicines del primer elemetn
    shoppingList = []
    for element in shopping_list:
        
        if all(element == shopping_list[0][0] for x in shopping_list):
            aux= []
            shoppingList.append(aux)
            aux.append(element)
            aux.append(shopping_list.count(element))
        
    print(element)
    print(shoppingList)
        
    

if __name__=="__main__":
    fiesta_lista()