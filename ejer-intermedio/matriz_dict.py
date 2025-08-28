'''
Dada una matriz, crea un diccionario que guarde el número de filas, el de columnas y cada fila en una entrada
de un diccionario
'''

def run():
    
    matriz=[["a1","a2"],
            ["b1","b2"],
            ["c1","c2"]]
    confilas=0
    concolumnas=0
    for i in matriz:
        confilas+=1
        for _ in i:
            concolumnas +=1
    myDicc = {"Numero filas":confilas,"Numero Columnas":concolumnas}
    print(myDicc)
        

if __name__=='__main__':
    run()