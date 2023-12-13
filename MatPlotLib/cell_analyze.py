# Importa numpy
from numpy import array

# Comprueba los parámetros de una propia célula y decide como evolucionará.
def checkSelf(grid, x, y):

    # Establece los valores que debe tener una célula para crecer o morir por defecto.
    die_par = 3
    grow_par = 7

    # Cambia los valores necesarios para las raíces. (Reproducción más lenta y tendencia a transferir el éter)
    if grid[y][x]["minerals"] != -1: 
        die_par = 5
        grow_par = 20

    # Cambia los valores necesarios para la copa del árbol. (Reproducción más rápida)
    if y < 10:
        die_par = 2
        grow_par = 5


    #Condicion para morir
    if grid[y][x]["eter"] < die_par or y <= 1 or y >= 30 : 

        return "die"
    
    # Condicion para reproducirse
    elif grid[y][x]["eter"] > grow_par: 

        return "grow"
    
    # Condición para mantenerse
    else :
        return None


# Comprueba si una célula está rodeada de otras.
def checkSorrounded(grid, x, y):

    # Inicializa los datos sobre si la célula está rodeada.
    isSorrounded = True
    sorroundedNumber = -1 # Se inicia en -1 porque la función va a contar a la propia célula inicial como 1.

    # Para cada celda alrededor comprueba si existe célula.
    for x_check in range (-1, 2):
        for y_check in range(-1, 2):
            if grid[y + y_check][x + x_check]["cell"] == None: 
                isSorrounded = False
            else:
                sorroundedNumber += 1

    return isSorrounded, sorroundedNumber


# Comprueba los parámetros de las celdas adyacentes a la célula.
def analyze_env(grid, x, y):

    # Obtiene las coordenadas a analizar mediante cálculo matricial
    up = array([0, -1]) # -1 Porque el 0,0 se encuentra en la esquina superior izquierda.
    right = array([1, 0])
    center = array([x, y])

    coordsToAnalyze = [center + up - right, center + up, center + up + right,
             center - right,  center + right,
             center - up - right, center - up, center - up + right]
    
    # Crea un diccionario con los datos y los extrae de cada coordenada.
    env_data = {}
    
    for index, coords in enumerate(coordsToAnalyze):

        (x,y) = (coords)
        cell = grid[y][x]
        
        cellData = [cell["minerals"], cell["sun"], cell["height"], cell["cell"], cell["color"]]    
        env_data[index] = cellData

    # Exporta también los datos de la propia célula.
    cell_pos = grid[y][x]
    cell_data = {"sun": cell_pos["sun"], "x": x, "height": cell_pos["height"], "color": cell_pos["color"]}

    return env_data, cell_data