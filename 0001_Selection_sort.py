def selection_sort(vector):
    n = len(vector)
    # Recorre todos los elementos de la lista
    for i in range(n):
        # Encuentra el elemento mínimo en la lista desordenada
        min_idx = i
        for j in range(i+1, n):
            if vector[j] < vector[min_idx]:
                min_idx = j
        # Intercambia el elemento mínimo encontrado con el primer elemento
        vector[i], vector[min_idx] = vector[min_idx], vector[i]
    return vector

# Ejemplo de uso
vector = [70,50,30,10,20,40,60]
print("Lista sin ordenar:", vector)
lista_ordenada = selection_sort(vector)
print("Lista ordenada:", lista_ordenada)
