# Importa las funciones matemáticas y la función de ruido de Perlin.
import random
from math import ceil
from perlin_noise import PerlinNoise

# Genera la cuadrícula inicial.
def generate_grid(grid_width, grid_height):

    #Establecemos parámetros deseados.
    sunHeight = 1
    dirtHeight = 6
    
    #Generamos las listas de cada clase con valores iniciales.
    sunGrid = [[{"color": 2, "cell": None, "eter": -1, "height": grid_height - dirtHeight - y, "sun": 4, "minerals": -1} for _ in range(grid_width)] for y in range(sunHeight)]
    skyGrid = [[{"color": 1, "cell": None, "eter": -1, "height": grid_height - dirtHeight - sunHeight - y, "sun": 4, "minerals": -1} for _ in range(grid_width)] for y in range(grid_height - sunHeight - dirtHeight)]
    dirtGrid = [[{"color": 0, "cell": None,"eter": -1, "height": -1, "sun": 0, "minerals": 0} for _ in range(grid_width)] for y in range(dirtHeight)]

    # Concatenamos todas las listas.
    grid = sunGrid + skyGrid + dirtGrid

    # Generamos mediante la función de ruido de Perlin valores aleatorios suavizados para el valor de los minerales del suelo.
    noise = PerlinNoise(octaves=6, seed=random.randint(0, 10000))
    for y in range(grid_height - dirtHeight, grid_height):
        for x in range(grid_width):
            noise_value = ceil((noise([x / 30, y / 30]) * 3) + 2)
            grid[y][x]["minerals"] = noise_value

    return grid