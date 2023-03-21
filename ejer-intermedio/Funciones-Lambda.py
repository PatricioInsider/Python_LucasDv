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
    
def basico3():
    discriminante = lambda a,b,c : pow(b,2)- 4*(a*c)
    print (discriminante(1,2,1)) 
    
def basico4():
    """crear una tupla con un numero ingresado, que guarde el numero, su doble, y su exponente
    """
    double_square = lambda x:(x,2*x,x**2)
    print(double_square(3))    
    
"""
La función filter()

Aplica una función a todos los elementos de un objeto iterable
Devuelve un objeto generador, de ahí que usemos la función list() para convertirlo a lista
Como output, devuelve los elementos para los cuales el aplicar la función ha devuelto True
Con la ayuda de las funciones lambda, apliquemos filter() para quedarnos con los números múltiplos de 7 de la siguiente lista llamada nums
    """
def fun_filter():
    nums = [49, 57,62,147,2101,22]
    print(int(filter(lambda x: (x%7 ==0), nums)))
    

if __name__ == "__main__":
    fun_filter()

