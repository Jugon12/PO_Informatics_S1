# Importa las funciones de sus niveles inferiores y la función random.
from cell_analyze import checkSelf, checkSorrounded
from cell_math import grow_cell
from enviroment_management import reduce_sun

from random import randint



# Crea una célula en la posición deseada con unos valores establecidos. Y la añade a la lista de todas las células.
def create_cell(grid, x, y, eter, color, cellList):

    # Coloca la célula en la posición inicial con el éter deseado.
    grid[y][x]["cell"] = "Alive"
    grid[y][x]["eter"] = eter

    # Ajusta los colores de las células.
    selectedColor = 0
    if y < 10: # A mucha altura, las células se convierten en hojas/flores (Aleatoriamente).

        if randint(0, 10) > 7:  # Color flor
            selectedColor = 5
        else:                   # Color hoja
            selectedColor = 4

    elif y > 24: selectedColor = 6 # A baja altura, las células se convierten en raíces.

    elif y == 0: selectedColor = 2 # Si superan las barreras, desaparecen.

    else: selectedColor = color # Si no se cumple ninguna condición, adquiere el color por defecto elegido.

    grid[y][x]["color"] = selectedColor

    # Añade las cordenadas de la célula a la lista de todas las células activas.
    cellList.insert(0, [y, x])

    #Reduce el sol de las celdas que haya debajo.
    reduce_sun(grid, x, y)



# Destruye la célula en la posición dada y la elimina de la lista de todas las células.
def destroy_cell(grid, x, y, cellList):

    # Borra los parámetros de la célula.
    grid[y][x]["cell"] = None
    grid[y][x]["minerals"] = -1
    grid[y][x]["eter"] = -1

    # Restablece los colores al original del fondo en función de donde estaba. (Cielo, tierra etc.)
    if y > 24: grid[y][x]["color"] = 0
    else : grid[y][x]["color"] = 1

    #Busca las coordenadas a eliminar en la lista de células y guarda las que siguen activas.
    newCellList = []
    destroyed_coords = [x, y]
    for coord in cellList: 
        if coord != destroyed_coords: 
            newCellList.insert(0, coord)
    cellList = newCellList



# Transifere el exceso de eter a la célula con más preferenncia basado en su posición. (Tiende a donar hacia arriba)
def transferEter(grid, x, y):

    # Establece el eter en exceso como el sobrante. El sobrante es el que haca por encima de la cantidad necesaria para mantenerse.
    cellExcessEter = grid[y][x]["eter"] - 6

    # Establece la lista de prioridades de transferencia (Preferencia hacia arriba), para imitar las propiedades físicas de las plantas.
    priorityTransferList = [[0, 1], [1, 1], [-1, 1], [-1, 0], [1, 0], [0, -1], [1, -1], [-1, -1]]

    # Para cada posición de la lista, comprueba si hay una célula en esa posicón. Si la hay, le da el eter.
    for cellPos in priorityTransferList:
        if grid[y - cellPos[1]][x + cellPos[0]]["cell"] == "Alive":
            grid[y][x]["eter"] -= round(cellExcessEter / 2)
            grid[y - cellPos[1]][x + cellPos[0]]["eter"] += round(cellExcessEter / 2)
            break



# Procesa todos los parámetros, decide la acción realiza, los opera para obtener el modelo de probabilidad y lo ejecuta. Todo apoyándose en las funciones inferiores.
def evolute(grid, x, y, cellList):

    # Comprueba sus propios parámetros y el número de células que le rodean
    action = checkSelf(grid, x, y)
    isSorrounded, sorroundedNumber = checkSorrounded(grid, x, y)

    # Si la célula está bajo tierra (Es una raíz), extrae eter del suelo.
    if grid[y][x]["minerals"] != -1:
        grid[y][x]["eter"] += randint(0, grid[y][x]["minerals"])
        print("Generado eter")

    # Si la célula es una flor y le da el sol, hace la fotosíntesis y consigue éter.
    if grid[y][x]["color"] == 5 and grid[y][x]["sun"] > 3:
        grid[y][x]["eter"] += randint(0, 1)
        print("Generado eter")   

    # Ejecuta las acciones en base a sus parámetros.
    if action == "grow" and isSorrounded == False:

        # Si tiene eter para crecer y no está rodeada, crece en la dirección obtenida en base a los modelos de probabilidad.
        if sorroundedNumber <= 3 or grid[y][x]["eter"] > 30:

            grow_x_par, grow_y_par = grow_cell(grid, x, y)

            cellEter = round(grid[y][x]["eter"]/2)
            create_cell(grid, x + grow_x_par, y - grow_y_par, cellEter, 3, cellList)

            print("Celula creada")

        # Sino, si tiene eter para crecer, pero está rodeada, trasfiere el exceso a una célula adyacente.
        else:

            transferEter(grid, x, y)
            print("Eter transferido")

    # Si no tiene suficiente eter, muere y se destruye la célula.
    elif action == "die":
        destroy_cell(grid, x, y, cellList)
        print("Celula destruida")

    # Si no tiene suficiente para crecer, consume éter para seguir viviendo.
    else:
        grid[y][x]["eter"] -= randint(0, 1)