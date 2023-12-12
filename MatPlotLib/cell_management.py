from numpy import array
from random import randint
from cell_analyze import checkSelf, checkSorrounded
from cell_math import grow_cell
from enviroment_management import reduce_sun

def create_cell(grid, x, y, eter, color, cellList):
    grid[y][x]["cell"] = "Alive"
    grid[y][x]["eter"] = eter
    reduce_sun(grid, x, y)

    selectedColor = 0
    if y < 10:

        if randint(0, 10) > 7:
            selectedColor = 5
        else:
            selectedColor = 4

    else: selectedColor = color

    if y > 24: selectedColor = 6
    if y == 0: selectedColor = 2


    grid[y][x]["color"] = selectedColor
    cellList.insert(0, [y, x])

def destroy_cell(grid, x, y, cellList):
    grid[y][x]["cell"] = None
    grid[y][x]["minerals"] = -1
    grid[y][x]["eter"] = -1

    if y > 24: grid[y][x]["color"] = 0
    else : grid[y][x]["color"] = 1

    newCellList = []
    coordenadas_a_eliminar = [x, y]
    for coord in cellList: 
        if coord != coordenadas_a_eliminar: 
            newCellList.insert(0, coord)
    cellList = newCellList

def transferEter(grid, x, y):

    cellExcessEter = grid[y][x]["eter"] - 6

    priorityTransferList = [[0, 1], [1, 1], [-1, 1], [-1, 0], [1, 0], [0, -1], [1, -1], [-1, -1]]
    for cellPos in priorityTransferList:
        if grid[y - cellPos[1]][x + cellPos[0]]["cell"] == "Alive":
            grid[y][x]["eter"] -= round(cellExcessEter / 2)
            grid[y - cellPos[1]][x + cellPos[0]]["eter"] += round(cellExcessEter / 2)
            break

    
def evolute(grid, x, y, cellList):

    if y > 30 or y < 0 or x < 0 or x > 59:
        print(x, y)
        return

    action = checkSelf(grid, x, y)
    isSorrounded, sorroundedNumber = checkSorrounded(grid, x, y)

    if grid[y][x]["minerals"] != -1:
        grid[y][x]["eter"] += randint(0, grid[y][x]["minerals"])
        print("Generado eter")

    if action == "grow" and isSorrounded == False:

        if sorroundedNumber <= 3 or grid[y][x]["eter"] > 30:

            grow_x_par, grow_y_par = grow_cell(grid, x, y)

            cellEter = round(grid[y][x]["eter"]/2)
            create_cell(grid, x + grow_x_par, y - grow_y_par, cellEter, 3, cellList)
            print("Celula creada")

        else:

            transferEter(grid, x, y)
            print("Eter transferido")


    elif action == "die":
        destroy_cell(grid, x, y, cellList)
        print("Celula destruida")

    else:
        grid[y][x]["eter"] -= randint(0, 1)