def run():
    myList =[1,"Hello",True,4.5] #listas de  objetos
    myDict = {"firstname":"facundo",#Eldiccionario tiene una llaves y valores
              "lastname":"Garcia"}#Guardan el orden de insercion del codigo
   
    superList = [ #Una lista de diccionarios
        {"firstname": "Facundo","lastname":"Garcia"},
        {"firstname": 4654,"lastname":"Garcia"},
        {"firstname": "Facundo","lastname":"Garcia"},
        {"firstname": 2133,"lastname":"Garcia"}
    ]
    
    superDict = {#Un diccionario de listas
        "natural_nums": [1,2,3,4,5],
        "integer_nums": [-1,-2,0,1,2],
        "floating_nums": [1.3,3.5,6.45]
    }
    print("Impresion de una lista cuyo contenido son diccionarios")
    
    for key,value in superDict.items():#impresion del diccionario de listas
            print (key,"-",value)
            
    
    print("Impresion de un diccionario cuyo valor son listas")
    for i in superList:
        for key,value in i.items():
            print (key,"-",value)
            
        
        
if __name__=='__main__':
    run()
    