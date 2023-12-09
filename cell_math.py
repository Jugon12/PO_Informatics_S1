from math import exp, log
from random import choices
from cell_analyze import analyze_env
from numpy import array

def mineral_distribution(minerals): # 0.2 - 1
    A = 0.2
    B = log(5)/3
    result = A * exp(B * (minerals - 1))
    return round(result, 3)


def sun_distribution(sun): # 0 - 1
    return sun


def height_distribution(height): # 0.368 - 1
    x = (height - 13)/12
    result = exp(-(x**2))
    return round(result, 3)


def model_prob(cell_data):

    minerals, sun, height, cell, color = cell_data[3]

    if height < 10:
        return [0.3, 0.3, 0.3, 1, 1, 0.2, 0.2, 0.2]
    if height > 25:
        return [1, 0.5, 1, 0.3, 0.3, 0.65, 0.3, 0.65]


def grow_prob(env_data, cell_data): 

    env_prob = []
    model_prob = [0, 0, 0, 0, 0, 0, 0, 0]

    for value in env_data.values():

        minerals, sun, height, cell, color = value

        env_probability = 0

        if cell is None :
            normalized_minerals = mineral_distribution(minerals)
            normalized_sun = sun_distribution(sun)
            normalized_height = height_distribution(height)

            env_probability = normalized_minerals * 0.3 + normalized_sun * 0.1 + normalized_height * 0.6
        
        env_prob.append(env_probability)
    
    env_prob_array = array(env_prob)
    model_prob_array = array(model_prob)

    total_probability = (env_prob_array * 0.6 + model_prob_array * 0.4)
    
    print(total_probability)
    return total_probability
        

def weighted_selection(probability):
    print(probability)
    suma_total = sum(probability)
    if suma_total == 0: return 0
    prob_normalized = [valor / suma_total for valor in probability]

    elemento_elegido = choices(range(len(prob_normalized)), weights=prob_normalized, k=1)[0]
    return elemento_elegido

def grow_cell(grid, x, y):

    from cell_analyze import analyze_env

    analyze_env_list = analyze_env(grid, x, y)
    env_data, cell_data = analyze_env_list

    grow_prob_list = grow_prob(env_data, cell_data)
    cell_selected = weighted_selection(grow_prob_list)

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
