import random
import math
from perlin_noise import PerlinNoise

def generate_grid(grid_width, grid_height, square_size):

    #Establecemos parámetros iniciales
    sunHeight = 1
    dirtHeight = 6
    mineralRange = 5
    
    #Generamos las listas de cada clase con valores iniciales
    sunGrid = [[{"color": 2, "cell": None, "eter": -1, "height": grid_height - dirtHeight - y, "sun": grid_height - dirtHeight - y, "minerals": -1} for _ in range(grid_width)] for y in range(sunHeight)]
    skyGrid = [[{"color": 1, "cell": None, "eter": -1, "height": grid_height - dirtHeight - sunHeight - y, "sun": grid_height - dirtHeight - sunHeight - y, "minerals": -1} for _ in range(grid_width)] for y in range(grid_height - sunHeight - dirtHeight)]
    dirtGrid = [[{"color": 0, "cell": None,"eter": -1, "height": -1, "sun": -1, "minerals": 0} for _ in range(grid_width)] for y in range(dirtHeight)]

    grid = sunGrid + skyGrid + dirtGrid # Concatenamos todas las listas

    # Generamos mediante la función de ruido de Perlin valores aleatorios suavizados para el valor de los minerales de las últimas capas
    noise = PerlinNoise(octaves=6, seed=random.randint(0, 10000))
    for y in range(grid_height - dirtHeight, grid_height):
        for x in range(grid_width):
            noise_value = math.ceil((noise([x / 30, y / 30]) * 3) + 2)
            grid[y][x]["minerals"] = noise_value
    return grid