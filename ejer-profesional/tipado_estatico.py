#Python es uno de los lenguajes de tipado dinamico entonces los errores nos refleja en tiempo de ejecucion y no al momento de compilacion
'''
De esta manera se declara una variable, se colocan los dos puntos (:), el tipo de dato y para finalizar se usa el signo igual para asignar el valor a la variable.
'''
def palindrome(dato: str) -> bool:
    dato = dato.replace(" ","").lower()
    return dato == dato[::-1]
    
def run():
    print (palindrome(1000))
  
#Variables en tipado estatico  
def varia():
    a: int =5
    print(a)
    
    b : str = 'Hola'
    print(b)
    
    c: bool = True
    print(c)

#Funciones con argumentos y retorno de una cariable con tipado estatico
def suma(a:int,b:int) -> int:
    return a+b

# diccionario,list
from typing import Dict,List

positives: list[int] =[1,2,4,5]
users : dict[str,int] = {
    "argentina":1,
    "mexico": 34,
    "colombia" :45,
}
countries: list[dict[str,str]] = {
    {
        "name": "Argentina",
        "people": "450000",
    },
    {
        "name": "Mexico",
        "people": "90000",
    },
    {
        "name": "Colombia",
        "people": "9555",
    }
}

#Tuplas tambien se pueden establecer lenguaje de tipado estatico
from typing import Tuple
numbers : Tuple[int,float,int] = (1,0.5,1)

    
if __name__=='__main__':
    run()
    
    