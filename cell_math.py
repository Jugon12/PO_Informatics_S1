from math import exp, log
from random import choices

def mineral_distribution(minerals): # 0.2 - 1
    A = 0.2
    B = log(5)/3
    result = A * exp(B * (minerals - 1))
    return round(result, 3)

def sun_distribution(sun): # 0 - 1
    return (sun - 1) / 2

def height_distribution(height): # 0.368 - 1
    x = (height - 13)/12
    result = exp(-(x**2))
    return round(result, 3)

def model_prob(cell_data): #Fibonacci
    return 0

def env_prob(env_data, cell_data): 
    print(cell_data)
    for value in env_data.values():
        minerals, sun, height, cell, color = value

        if cell is not None : env_probability = 0
        else:
            normalized_minerals = mineral_distribution(minerals)
            normalized_sun = sun_distribution(sun)
            normalized_height = height_distribution(height)

            env_probability = normalized_minerals * 0,3 + normalized_sun * 0,2 + normalized_height * 0,5
        print(env_probability)
    # Total probability = env_probability * 0,6 + model_probability * 0,4

def weighted_selection(probability):
    suma_total = sum(probability)
    prob_normalized = [valor / suma_total for valor in probability]

    elemento_elegido = choices(range(len(prob_normalized)), weights=prob_normalized, k=1)[0]
    return elemento_elegido, probability[elemento_elegido]