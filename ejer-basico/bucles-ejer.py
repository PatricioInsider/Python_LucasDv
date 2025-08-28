#Encontrar los numeros primos, (dividible  par la unidad y a si mismo)
from re import I

def primo(i):
    if (i / 1) == i and (i / i) == 1 :
        return print('El numero {} es primo'.format(i))
    else:
        print('x')



def run():
    limite = int(input('Escribe el numero maximo de busqueda: '))
    contador = 0
    for i in range(1,limite):
        
        primo(i)

if __name__ == '__main__':
    run()
