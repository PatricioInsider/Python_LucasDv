from itertools import permutations

def count_swaps(perm):
    """
    Cuenta el mínimo número de intercambios adyacentes necesarios para ordenar
    la primera mitad ascendente y la segunda mitad descendente.
    """
    N = len(perm)
    half = N // 2
    temp = list(perm)
    swaps = 0
    
    # Ordena la primera mitad en orden ascendente
    for i in range(half):
        for j in range(half - i - 1):
            if temp[j] > temp[j + 1]:
                temp[j], temp[j + 1] = temp[j + 1], temp[j]
                swaps += 1
    
    # Ordena la segunda mitad en orden descendente
    for i in range(half, N):
        for j in range(half, N - 1):
            if temp[j] < temp[j + 1]:
                temp[j], temp[j + 1] = temp[j + 1], temp[j]
                swaps += 1
                
    return swaps

def calculate_total_swaps(N, M):
    """
    Calcula la suma total de intercambios mínimos necesarios para todas las permutaciones
    posibles de longitud N, módulo M.
    """
    # Genera números del 1 al N
    numbers = list(range(1, N + 1))
    
    # Genera todas las permutaciones posibles
    total_swaps = 0
    
    # Itera sobre todas las permutaciones
    for perm in permutations(numbers):
        total_swaps = (total_swaps + count_swaps(perm)) % M
        
    return total_swaps

def main():
    # Lee la entrada
    N, M = map(int, input().split())
    
    # Calcula y muestra el resultado
    result = calculate_total_swaps(N, M)
    print(result)

if __name__ == "__main__":
    main()