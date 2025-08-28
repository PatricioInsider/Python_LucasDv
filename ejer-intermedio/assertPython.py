
from lib2to3.pytree import NegatedPattern


def finish():
    print("Gracias por usar nuestro programa")

def divisor(num):
    divisors=[]
    for i in range(1,num+1):
        if num%i == 0:
            divisors.append(i)
    return divisors

def run():
    
    try:
        num = input("Ingresa un numero: ")
        #assert statements
        '''
        La diferencia fundamental con la funcion try-except es que es nos imprime en pantalla el error sirve para que el usuario pueda entender, por que si lo hacemos con el assert (diriamos que es una alerta para nosotros los programadores)
        '''
        #Como la condicion se cumple seguimos con el flujo normal de python
        
        assert num.isnumeric(), "Debes ingresar un numero "
        if int(num)<0:
            raise ValueError("Debe ser un numero positivo")
        print (divisor(int(num)))
        finish()
    except ValueError as errorNega:
        print(errorNega)
    
    


if __name__=='__main__':
    run()