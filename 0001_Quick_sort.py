def partition(vector, low, high):
    pivot = vector[high]  # Escojer el ultimo elemento de manera arbritraria como pivote.
    i = low - 1  # Indice del elemento mas pequeño.

    for j in range(low, high):
        if vector[j] < pivot:
            i += 1
            vector[i], vector[j] = vector[j], vector[i]  # Cambiar elementos si es mas pequeño que el pivote.

    vector[i + 1], vector[high] = vector[high], vector[i + 1]  # Colocar el elemento pivote en us posicion correcta.
    return i + 1  # Devolver el indice de partición.

def quick_sort(vector, low, high):
    if low < high:
        # Partir el vector y obtener el indice de particion.
        pi = partition(vector, low, high)

        # recursivamente ordenar los elementos antes y despues de la particion.
        quick_sort(vector, low, pi - 1)
        quick_sort(vector, pi + 1, high)

    return vector


# Ejemplo de uso
vector = [70,50,30,10,20,40,60]
print("Lista sin ordenar:", vector)
vector_ordenado = quick_sort(vector, 0, len(vector)-1)
print("Lista ordenada:", vector_ordenado)

