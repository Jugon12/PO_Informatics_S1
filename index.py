import pygame
from grid_generator import generate_grid
from colors import colors
import random

# Inicialización de Pygame
pygame.init()

# Dimensiones de la ventana principal
window_width, window_height = 1920, 992
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Cuadrícula de Colores")

# Tamaño de los cuadrados
square_size = 32
grid_width = int(window_width / square_size)
grid_height = int(window_height / square_size)
grid = generate_grid(grid_width, grid_height, square_size)

# Colocamos la inicial
xInitPlant = random.randint(int(grid_width/3), 2 * int(grid_width/3))
grid[grid_height - 7][xInitPlant]["cell"] = "Alive"
grid[grid_height - 7][xInitPlant]["eter"] = 10
grid[grid_height - 7][xInitPlant]["color"] = 3
grid[grid_height - 7][xInitPlant]["minerals"] = -1

intervalo_tiempo = 1000  # Ejecución cada 1000 ms (1 segundo)
tiempo_anterior = pygame.time.get_ticks()
showNoiseMap = True

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Verifica si la tecla 'a' se ha presionado
            if event.key == pygame.K_SPACE:
                showNoiseMap = not showNoiseMap  # Cambia el valor de la variable cuando se pulsa 'a'
            elif event.key == pygame.K_a:
                grid = generate_grid(grid_width, grid_height, square_size)  # Cambia el valor de la variable cuando se pulsa 'a'

    # Obtener el tiempo actual
    tiempo_actual = pygame.time.get_ticks()

    # Comprobar si ha pasado el intervalo de tiempo
    if tiempo_actual - tiempo_anterior >= intervalo_tiempo:
        # Aquí puedes realizar alguna acción o proceso a ejecutar a intervalos regulares

        # Actualizar el tiempo anterior
        tiempo_anterior = tiempo_actual

    # Dibuja la cuadrícula
    for y in range(grid_height):
        for x in range(grid_width):
            cell = grid[y][x]
            if showNoiseMap : 
                if cell["minerals"] == -1: color = colors.get(cell["color"], (0, 0, 0))
                else: color = colors.get(cell["minerals"] + 5, (0, 0, 0))
            else : color = colors.get(cell["color"], (0, 0, 0))
            
            pygame.draw.rect(screen, color, (x * square_size, y * square_size, square_size, square_size))

    # Actualiza la pantalla
    pygame.display.flip()

# Cerrar Pygame
pygame.quit()