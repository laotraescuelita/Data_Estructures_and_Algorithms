import pygame
import random
import time

# Inicialización de Pygame
pygame.init()

# Configuración de la pantalla
ANCHO = 800
ALTO = 600
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Visualización de Merge Sort")

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)

# Configuración de la vector
NUM_ELEMENTOS = 50
MAX_VALOR = 100
vector = [random.randint(1, MAX_VALOR) for _ in range(NUM_ELEMENTOS)]

# Función para dibujar la vector
def dibujar_vector(vector, indices_coloreados=[]):
    VENTANA.fill(NEGRO)
    ancho_bloque = ANCHO // NUM_ELEMENTOS
    for i, val in enumerate(vector):
        x = i * ancho_bloque
        y = ALTO - val * (ALTO // MAX_VALOR)
        color = VERDE if i in indices_coloreados else BLANCO
        pygame.draw.rect(VENTANA, color, (x, y, ancho_bloque, val * (ALTO // MAX_VALOR)))
    pygame.display.update()

# Función para merge sort con visualización
def merge_sort_visual(vector, inicio, fin):
    if inicio < fin:
        medio = (inicio + fin) // 2

        # Ordenar la primera mitad
        merge_sort_visual(vector, inicio, medio)
        # Ordenar la segunda mitad
        merge_sort_visual(vector, medio + 1, fin)

        # Combinar las dos mitades ordenadas
        merge(vector, inicio, medio, fin)

def merge(vector, inicio, medio, fin):
    L = vector[inicio:medio + 1]
    R = vector[medio + 1:fin + 1]

    i = j = 0
    k = inicio

    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            vector[k] = L[i]
            i += 1
        else:
            vector[k] = R[j]
            j += 1
        k += 1
        dibujar_vector(vector, list(range(inicio, fin + 1)))
        time.sleep(0.05)  # Pausa para visualización

    while i < len(L):
        vector[k] = L[i]
        i += 1
        k += 1
        dibujar_vector(vector, list(range(inicio, fin + 1)))
        time.sleep(0.05)  # Pausa para visualización

    while j < len(R):
        vector[k] = R[j]
        j += 1
        k += 1
        dibujar_vector(vector, list(range(inicio, fin + 1)))
        time.sleep(0.05)  # Pausa para visualización

# Bucle principal
ejecutando = True
ordenado = False
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    if not ordenado:
        merge_sort_visual(vector, 0, len(vector) - 1)
        ordenado = True

    dibujar_vector(vector)

pygame.quit()
