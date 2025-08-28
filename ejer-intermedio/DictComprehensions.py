#Dictionary comprehensions
'''Diccionarios cuyas llaves sehan los 100 primeros numeros naturales y sus valores los 100 primeros numeros al cubo
que no sehan divisinle entre 3'''
def run ():
    
    myDict ={i:i**3 for i in range(1,100) if i%3!=0}
    myDict ={i:i**3 for i in range(1,100) if i%3!=0}
    
    for key,val in myDict.items(): #impresion de los diccionarios con .items()
        print(key,('-'),val)
    
if __name__=='__main__':
    run()