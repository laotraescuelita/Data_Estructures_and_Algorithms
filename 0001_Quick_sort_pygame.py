import pygame
import random
import time

# Inicialización de Pygame
pygame.init()

# Configuración de la pantalla
ANCHO = 800
ALTO = 600
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Visualización de Quick Sort")

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

# Función para particionar la vector
def particion(vector, bajo, alto):
    i = bajo - 1  # Índice del elemento más pequeño
    pivot = vector[alto]  # Pivote

    for j in range(bajo, alto):
        if vector[j] < pivot:
            i = i + 1
            vector[i], vector[j] = vector[j], vector[i]
            dibujar_vector(vector, [i, j])
            time.sleep(0.05)  # Pausa para visualización

    vector[i + 1], vector[alto] = vector[alto], vector[i + 1]
    dibujar_vector(vector, [i + 1, alto])
    time.sleep(0.05)  # Pausa para visualización
    return i + 1

# Función de Quick Sort con visualización
def quick_sort_visual(vector, bajo, alto):
    if bajo < alto:
        pi = particion(vector, bajo, alto)

        # Ordenar los elementos por separado antes y después de la partición
        quick_sort_visual(vector, bajo, pi - 1)
        quick_sort_visual(vector, pi + 1, alto)

# Bucle principal
ejecutando = True
ordenado = False
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    if not ordenado:
        quick_sort_visual(vector, 0, len(vector) - 1)
        ordenado = True

    dibujar_vector(vector)

pygame.quit()
