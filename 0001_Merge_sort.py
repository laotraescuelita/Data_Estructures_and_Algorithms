def merge_sort(vector):
    if len(vector) > 1:
        mid = len(vector) // 2  # Encontrar el valor del medio.
        left_half = vector[:mid]  # Dividir el vector en dos partes.
        right_half = vector[mid:]

        # Llamada reursiv para dividir cada segmento en dos partes hasta que haya solo un elemento.
        merge_sort(left_half)
        merge_sort(right_half)

        # Juntar las dos mitades de manera ordenada.
        i = j = k = 0  
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                vector[k] = left_half[i]
                i += 1
            else:
                vector[k] = right_half[j]
                j += 1
            k += 1

        # Agragar los elementos restante en cualquiera de las dos mitades.
        while i < len(left_half):
            vector[k] = left_half[i]
            i += 1
            k += 1
        
        while j < len(right_half):
            vector[k] = right_half[j]
            j += 1
            k += 1

    return vector
    
# Ejemplo de uso
vector = [70,50,30,10,20,40,60]
print("Lista sin ordenar:", vector)
vector_ordenado = merge_sort(vector)
print("Lista ordenada:", vector_ordenado)
