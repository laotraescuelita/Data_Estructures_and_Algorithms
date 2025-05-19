def bubble_sort(vector):
    n = len(vector)
    # Recorre todos los elementos de la lista
    for i in range(n):
        # La bandera para verificar si hubo intercambio
        swapped = False
        # Los últimos i elementos ya están en su lugar
        for j in range(0, n-i-1):
            # Recorre la lista de 0 a n-i-1
            # Intercambia si el elemento encontrado es mayor
            # que el siguiente elemento
            if vector[j] > vector[j+1]:
                vector[j], vector[j+1] = vector[j+1], vector[j]
                swapped = True
        # Si no hubo intercambio, la lista ya está ordenada
        if not swapped:
            break
    return vector

# Ejemplo de uso
vector = [70,50,30,10,20,40,60]
print("Lista sin ordenar:", vector)
vector_ordenado = bubble_sort(vector)
print("Lista ordenada:", vector_ordenado)
