from numpy import array
from random import randint

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
            

def checkSelf(grid, x, y):
    if grid[y][x]["eter"] < 3: #Condicion para morir
        return "die"
    elif grid[y][x]["eter"] > 7: # Condicion para reproducirse
        return "grow"
    else : # Condición para mantenerse
        return None
    
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

def analyze_env(grid, x, y):
    # Indices de los bloques alrededor
    #Eje x (hacia derecha)
    #Eje Y (hacia abajo)

    # 0    1     2
    # 3  centro  4
    # 5    6     7
    up = array([0, -1])
    right = array([1, 0])

    # obtenemos lista con las coordenadas de los bloques alrededor
    centro = array([x, y])
    bloques = [centro + up - right, centro + up, centro + up + right,
               centro - right,  centro + right,
               centro - up - right, centro - up, centro - up + right]
    

    # creamos diccionario con (indice de bloque: su posicion)
    i = [0, 1, 2, 3, 4, 5, 6, 7]
    bloques_dict = {indice: bloque for (indice, bloque) in zip(i, bloques)}
    

    #Output: output -> 0:[eter_0, minerales_0, sol_0, cell_0, color0], 1:[eter_1, minerales_1, sol_1, cell_1, color_1]...
    #parametros ={0:, 1:, 2:, 3:, 4:, 5:, 6:, 7:}
    env_data ={}
    indices =[0,1,2,3,4,5,6,7]
    
    for a, bloque in enumerate(bloques_dict.values()):
        (w,h) = (bloque)
        cell = grid[h][w]
        
        L = [cell["minerals"], cell["sun"], cell["height"], cell["cell"], cell["color"]]    
        env_data[a]= L

    #Devuelve un diccionario del formato {0:[eter_0, minerales_0, sol_0, cell_0, color0]...}
    #Donde el key es el índice del bloque adyacente (0,1,2,3,4...)


    cell_pos = grid[y][x]
    cell_data = {"sun": cell_pos["sun"], "x": x, "height": cell_pos["height"], "color": cell_pos["color"]}

    return env_data, cell_data

def calc_prob(env_data, cell_data): 
    print(cell_data)
    for value in env_data.values():
        minerals, sun, height, cell, color = value

        if cell is not None : env_probability = 0
        else:
            normalized_minerals = minerals
            normalized_sun = sun
            normalized_height = height

            env_probability = normalized_minerals * 0,3 + normalized_sun * 0,2 + normalized_height * 0,5
        print(env_probability)
    # Total probability = env_probability * 0,6 + model_probability * 0,4