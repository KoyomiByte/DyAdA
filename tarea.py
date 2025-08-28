def existe_par_suma_fuerza_bruta(arreglo, K):
    n = len(arreglo)
    for i in range(n):
        for j in range(i + 1, n):
            if arreglo[i] + arreglo[j] == K:
                return True
    return False

def existe_par_suma_hash(arreglo, K):
    numeros_vistos = set()
    for numero in arreglo:
        complemento = K - numero
        if complemento in numeros_vistos:
            return True
        numeros_vistos.add(numero)
    return False

# Ejemplo de uso
if __name__ == "__main__":
    arreglo = [1, 5, 7, 3, 8, 2]
    K = 10
    
    print("Usando fuerza bruta:")
    print(existe_par_suma_fuerza_bruta(arreglo, K))  # True (7+3)
    
    print("Usando tabla hash:")
    print(existe_par_suma_hash(arreglo, K))  # True
    
    # Prueba con un caso negativo
    arreglo2 = [1, 2, 3, 4]
    K2 = 10
    
    print("\nPrueba caso negativo (debe dar False):")
    print("Fuerza bruta:", existe_par_suma_fuerza_bruta(arreglo2, K2))
    print("Hash:", existe_par_suma_hash(arreglo2, K2))
