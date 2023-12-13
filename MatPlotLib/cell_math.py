# Importa las funciones matemáticas.
from math import exp, log
from random import choices
from numpy import array



# Distribución exponencial para los minerales. N [1, 5] -> Q [0.2, 1]
def mineral_distribution(minerals): # 0.2 - 1

    A = 0.2
    B = log(5)/3
    result = A * exp(B * (minerals - 1))

    return round(result, 3)



# Distribución lineal para el sol. N [0, 4] -> Q [0, 1]
def sun_distribution(sun): # 0 - 1

    result = (sun + 1)/5

    return round(result, 3)



# Distribución exponencial (Campana de Gauss) para la altura. N [1, 32] -> Q [0.368, 1]
def height_distribution(height): # 0.368 - 1

    x = (height - 13)/12
    result = exp(-(x**2))

    return round(result, 3)



# Ajustes de probabilidad basados en los datos empíricos del crecimiento de las plantas.
def model_prob(cell_data):

    minerals, sun, height, cell, color = cell_data[3]

    # Las raíces tienden a crecer en diagonal hacia abajo.
    if height < 10:

        return [0.3, 0.3, 0.3, 1, 1, 0.2, 0.2, 0.2]
    
    # Las copas de los árboles tienden a extenderse hacia los lados, en vez de seguir creciendo hacia arriba.
    if height > 25:

        return [1, 0.5, 1, 0.3, 0.3, 0.65, 0.3, 0.65]



# Cálcula la lista de probabilidades de crecimiento basado en todos los parámetros.
def grow_prob(env_data): 

    # Crea las listas donde se almacenarán los datod.
    env_prob = []
    model_prob = [0] * 8

    # Para cada celda que rodea a la célula, extrae sus parámetros y hace el calculo de probabilidad.
    for value in env_data.values():

        minerals, sun, height, cell, color = value

        env_probability = 0

        if cell is None :
            normalized_minerals = mineral_distribution(minerals)
            normalized_sun = sun_distribution(sun)
            normalized_height = height_distribution(height)

            env_probability = normalized_minerals * 0.3 + normalized_sun * 0.1 + normalized_height * 0.6
        
        env_prob.append(env_probability)
    
    # Convierte ambas listas en matrices para poder operarlas. (Multiplicación por escalar y suma entre ellas)
    env_prob_array = array(env_prob)
    model_prob_array = array(model_prob)

    total_probability = (env_prob_array * 0.6 + model_prob_array * 0.4)
    
    return total_probability



# Elige un número al azar de una lista, ponderando sus probabilidades al valor de la celda. 
def weighted_selection(probability):

    # Normaliza los valores para que sean probabilidades.
    sum_total = sum(probability)
    if sum_total == 0: return 0
    prob_normalized = [valor / sum_total for valor in probability]

    # Elige un elemento al azar y devuelve el índice.
    elemento_elegido = choices(range(len(prob_normalized)), weights=prob_normalized, k=1)[0]

    return elemento_elegido



# Hace crecer la célula elegida, invocando otras funciones del mismo nivel para hacer los cálculos.
def grow_cell(grid, x, y):

    # Analiza el entorno de la célula.
    from cell_analyze import analyze_env

    env_data, cell_data = analyze_env(grid, x, y)

    # Procesa los parámetros y elige hacia donde crecerá.
    grow_prob_list = grow_prob(env_data)
    cell_selected = weighted_selection(grow_prob_list)

    # Convierte el índice de crecimiento en unas coordenadas relativas.
    grow_x_par = 0
    grow_y_par = 0

    if cell_selected in [2, 4, 7]:
            grow_x_par = 1
    elif cell_selected in [1, 6]:
            grow_x_par = 0
    elif cell_selected in [0, 3, 5]:
            grow_x_par = -1

    if cell_selected in [0, 1, 2]:
            grow_y_par = 1
    elif cell_selected in [3, 4]:
            grow_y_par = 0
    elif cell_selected in [5, 6, 7]:
            grow_y_par = -1

    return grow_x_par, grow_y_par
