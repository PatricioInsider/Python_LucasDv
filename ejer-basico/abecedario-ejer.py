import random
import re

def gennerador_contrasena():
    MAYUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    CHARS = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']
    caracteres = MAYUS + MINUS + NUMS + CHARS
    
    contrasena = []
    for i in range(10):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)
        # Union de los datos de una cadena en un string
    contrasena = ''.join(contrasena)
    return contrasena



def run():
    contrasena = gennerador_contrasena()
    print('Tu contraseña es :', contrasena)

if __name__=='__main__':
    run()    


    #En python no existe el do while