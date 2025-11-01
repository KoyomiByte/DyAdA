def mergeSort(lista):
    if len(lista) > 1:
        # Dividir
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]

        # Llamada recursiva
        mergeSort(izquierda)
        mergeSort(derecha)

        # Combinar
        i = j = k = 0
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1

        # elementos restantes
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1


numeros = [38, 27, 43, 3, 9, 82, 10]
mergeSort(numeros)
print("Lista ordenada:", numeros)
