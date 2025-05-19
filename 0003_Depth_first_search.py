def dfs_recursive(graph, start, goal, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start)
    print(start, end=' -> ')    

    if start == goal:
        return True
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            if dfs_recursive(graph, neighbor, goal, visited):
                return True
    
    return False

# Perform DFS starting from vertex 'A'
#dfs_recursive(graph, 'A', 'E' )



def dfs_iterative(graph, start, goal):
    #inicializa los datos de la lista.
    stack = [start]
    # Inicializar un conjunto para rastrear los nodos visitados
    visited = set([start])
    path = []
    parent = {start:None}

    
    # Mientras la pila no esté vacía
    while stack:
        # Extraer el primer nodo de la pila 
        current = stack.pop()
        
        path.append(current)
        # Verificar si hemos alcanzado el nodo meta
        if current == goal:
            print( f'Path {path}, Parents {parent} ')
        
        # Obtener todos los vecinos del nodo actual
        for neighbor in graph[current]:
            # Si el vecino no ha sido visitado
            if neighbor not in visited:
                # Marcarlo como visitado
                visited.add(neighbor)
                # Agregarlo a la cola
                stack.append(neighbor)
                # Identificar su padre
                parent[neighbor] = current
    
    # Si hemos salido del bucle, significa que no hemos encontrado la meta
    return False    


# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Perform DFS starting from vertex 'A'
dfs_iterative(graph, 'A', 'E')
