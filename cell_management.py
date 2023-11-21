from numpy import array
from random import randint
from cell_analyze import checkSelf, analyze_env
from cell_math import height_distribution, calc_prob

def create_cell(grid, x, y, eter, color, cellList):
    grid[y][x]["cell"] = "Alive"
    grid[y][x]["minerals"] = -1
    grid[y][x]["eter"] = eter
    grid[y][x]["color"] = color
    cellList.insert(0, [y, x])

def destroy_cell(grid, x, y, cellList):
    grid[y][x]["cell"] = "Dead"
    grid[y][x]["minerals"] = -1
    grid[y][x]["eter"] = -1
    grid[y][x]["color"] = 1
    newCellList = []
    coordenadas_a_eliminar = [x, y]
    for coord in cellList: 
        if coord != coordenadas_a_eliminar: 
            newCellList.insert(0, coord)
    cellList = newCellList
    
def evolute(grid, x, y, cellList):

    action = checkSelf(grid, x, y)
    print(action)
    print(x, y)

    if action == "grow":
        grow_x_par = 0
        grow_y_par = 0
        #Los grow parameters serán los resultados de la función calc probability, irán en valores entre -1 y +1
        if grid[y-1][x]["cell"] == None:
            grow_y_par = -1
        elif grid[y][x - 1]["cell"] == None:
            grow_x_par = -1
        elif grid[y][x + 1]["cell"] == None:
            grow_x_par = 1
        else: return None

        cellEter = randint(5,10)
        create_cell(grid, x + grow_x_par, y + grow_y_par, cellEter, 3, cellList)
        print("Celula creada")

    elif action == "die":
        destroy_cell(grid, x, y, cellList)