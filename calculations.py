
from config import cost_matrix, time_windows, penalty_per_city

def calculate_time(path):
    cost = 0
    for path_idx in range(len(path) - 1):
        cost += cost_matrix[path[path_idx]][path[path_idx + 1]]
    return cost

def calculate_penalty(path):
    penalty = 0
    for i in range(len(path)):
        min_time, max_time = time_windows[path[i]]
        arrival_time = calculate_time(path[0:i+1])
        if arrival_time < min_time or arrival_time > max_time:
            penalty += penalty_per_city
    return penalty

import itertools
from config import start_city, cities, time_windows

def is_feasible_permutation(permutation):
    current_time = 0 
    for city in permutation:
        min_time, max_time = time_windows[city]
        current_time += cost_matrix[start_city][city]
        if current_time < min_time or current_time > max_time:
            return False
    return True

def has_feasible_solution():
    for permutation in itertools.permutations(cities):
        if is_feasible_permutation(permutation):
            return True
    return False