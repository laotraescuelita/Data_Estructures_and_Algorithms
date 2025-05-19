from collections import deque

def bfs(graph, start, goal):
    # Inicializar la cola con el nodo inicial
    queue = deque([start])
    # Inicializar un conjunto para rastrear los nodos visitados
    visited = set([start])
    path = []
    parent = {start:None}

    # Mientras la cola no esté vacía
    while queue:
        # Extraer el primer nodo de la cola
        current = queue.popleft()
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
                queue.append(neighbor)
                # Identificar su padre
                parent[neighbor] = current
    
    # Si hemos salido del bucle, significa que no hemos encontrado la meta
    return False

# Ejemplo de uso
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start = 'A'
goal = 'F'

bfs(graph, start, goal)
