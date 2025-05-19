import pygame
import random
import time

# Inicialización de Pygame
pygame.init()

# Configuración de la pantalla
ANCHO = 800
ALTO = 600
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Visualización de Selection Sort")

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

# Función de Selection Sort con visualización
def selection_sort_visual(vector):
    n = len(vector)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if vector[j] < vector[min_idx]:
                min_idx = j
            dibujar_vector(vector, [i, j, min_idx])
            time.sleep(0.05)  # Pausa para visualización
        vector[i], vector[min_idx] = vector[min_idx], vector[i]
        dibujar_vector(vector, [i, min_idx])
        time.sleep(0.05)  # Pausa para visualización

# Bucle principal ##########################################################################
ejecutando = True
ordenado = False
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    if not ordenado:
        selection_sort_visual(vector)
        ordenado = True

    dibujar_vector(vector)

pygame.quit()
