from numpy import array

def checkSelf(grid, x, y):

    die_par = 3
    grow_par = 7

    if grid[y][x]["minerals"] != -1: 
        die_par = 5
        grow_par = 20
        
    if y < 10:
        die_par = 2
        grow_par = 5

    if grid[y][x]["eter"] < die_par or y == 1 or y > 30 : #Condicion para morir
        return "die"
    elif grid[y][x]["eter"] > grow_par: # Condicion para reproducirse
        return "grow"
    else : # Condición para mantenerse
        return None

def checkSorrounded(grid, x, y):

    sorrounded = True
    sorroundedNumber = -1

    for x_check in range (-1, 2):
        for y_check in range(-1, 2):
            if grid[y + y_check][x + x_check]["cell"] == None: 
                sorrounded = False
            else:
                sorroundedNumber += 1

    return sorrounded, sorroundedNumber


def analyze_env(grid, x, y):

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