from numpy import array

def create_cell(grid, x, y, eter, color, cellList):
    grid[y][x]["cell"] = "Alive"
    grid[y][x]["minerals"] = -1
    grid[y][x]["eter"] = eter
    grid[y][x]["color"] = color
    cellList.insert([y, x])

def destroy_cell(grid, x, y):
    print("Do some code...")

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