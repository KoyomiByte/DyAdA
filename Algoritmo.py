def busqueda_lineal(arr, valor):
    comparaciones = 0
    for elemento in arr:
        comparaciones += 1  # T(n): n comparaciones (peor caso)
        if elemento == valor:
            break
    return comparaciones  # T(n) total: O(n)

# Ejemplo de uso
arreglo = [3, 1, 4, 1, 5, 9, 2, 6]
valor_buscar = 5
comparaciones = busqueda_lineal(arreglo, valor_buscar)
print(f"Se realizaron {comparaciones} comparaciones")
