#FUNCIONES LAMBDA
"""FUNCIONES LAMBDA
    Son un tipo especial de funciones de Python que tienen la sintaxis siguiente

lambda parámetros: expresión
(p reservada) (el unico parametro de entrada que recibe) (la unica expresion que hace)

Son útiles para ejecutar funciones en una sola línea
Pueden tomar cualquier número de argumentos
Tienen una limitación: solamente pueden contener una expresión
"""
def basico():
    """Funcion que dado un numero , le suma 10 puntos mas"""
    plus10 = lambda x: x+10
    plus10(5)
    
    """corresponde a:
    def plus10(x):
        x += 10
        return x
    """

def basico2():
    prod = lambda x,y:x+y
    print (prod(5,10))
    
def discriminante():
    discri = lambda a,b,c : pow(b,2)- 4*(a*c)
    print (discri(1,2,1)) 
    

if __name__ == "__main__":
    discriminante()

