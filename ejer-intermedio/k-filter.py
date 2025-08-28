def filtrar():
    """Funcion lambda empleada con filter, para filtrar los numeros positivos de una matriz, y agregarla en otra matriz
    """
    nums = [[-5,-3,5],{2,1,3,-2,-9},[-0.4,-0.01]]
    mat = []
    for e in nums:
        mat.append(list(filter(lambda x:(x>0),e)))
    print (mat)

if __name__ == "__main__":
    filtrar()