import itertools
from config import cities, start_city
from calculations import calculate_cost, calculate_penalty

def brute_force_tsp_1():
    permutations = itertools.permutations(cities)
    min_penalty = float('inf')
    min_cost = float('inf')
    best_path = None
    for perm in permutations:
        path = [start_city] + list(perm) + [start_city]
        penalty = calculate_penalty(path)
        cost = calculate_cost(path)
        if cost < min_cost:
            min_penalty = penalty
            min_cost = cost
            best_path = path
    return best_path, min_penalty, min_cost

def brute_force_tsp_2():
    permutations = itertools.permutations(cities)
    min_penalty = float('inf')
    min_cost = float('inf')
    best_path = None
    for perm in permutations:
        path = [start_city] + list(perm) + [start_city]
        penalty = calculate_penalty(path)
        cost = calculate_cost(path)
        if penalty < min_penalty or (penalty == min_penalty and cost < min_cost):
            min_penalty = penalty
            min_cost = cost
            best_path = path
    return best_path, min_penalty, min_cost

def brute_force_tsp_3():
    permutations = itertools.permutations(cities)
    min_penalty = float('inf')
    min_cost = float('inf')
    best_path = None
    for perm in permutations:
        path = [start_city] + list(perm) + [start_city]
        penalty = calculate_penalty(path)
        cost = calculate_cost(path) + penalty
        if cost < min_cost:
            min_penalty = penalty
            min_cost = cost
            best_path = path
    return best_path, min_penalty, min_cost
