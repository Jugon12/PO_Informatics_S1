# Importa las funciones de sus niveles inferiores y la función random.
from grid_generator import generate_grid
from cell_management import create_cell, evolute

from random import randint



# Inicializa el motor generando la cuadrícula inicial.
def start_motor(width, height):

    # Crea la lista con las coordenadas de todas las células y genera la cuadrícula inicial.
    cellList = []
    grid = generate_grid(width, height)

    #Coloca la primera célula en una posición al azar del suelo.
    xInitPlant = randint(int(width/3), 2 * int(width/3))
    create_cell(grid, xInitPlant, height - 6, 25, 3, cellList)

    return grid, cellList



# Procesa todas las acciones individuales de cada célula y las actualiza en la cuadrícula.
def update_motor(grid, cellList):

    # Guarda el número de células activas.
    cellNumber = len(cellList)

    # Evoluciona las células de la lista de células vivas. Esta almacena las coordenadas de cada célula en la forma (y, x).
    for i in range(cellNumber):
        cell = cellList[i]
        evolute(grid, cell[1], cell[0], cellList)

    # Guarda el número de células después de haberlas evolucionado. Añade las creadas y borra las destruidas.
    newCellNumber = len(cellList)

    return grid, cellNumber, newCellNumber
