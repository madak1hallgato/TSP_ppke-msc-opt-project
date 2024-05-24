
# Setup the problem to be solved

city_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

start_city = 0
cities = [1, 2, 3, 4, 5, 6, 7]

cost_matrix = [
    [0, 1, 8, 9, 3, 2, 4, 6],
    [1, 0, 7, 4, 1, 3, 9, 2],
    [8, 7, 0, 6, 8, 2, 4, 5],
    [9, 4, 6, 0, 9, 3, 1, 1],
    [3, 1, 8, 9, 0, 4, 2, 7],
    [2, 3, 2, 3, 4, 0, 6, 3],
    [4, 9, 4, 1, 2, 6, 0, 5],
    [6, 2, 5, 1, 7, 3, 5, 0]
]

time_windows = [
    (0, 100),
    (3, 12),
    (32, 40),
    (15, 24),
    (3, 6),
    (6, 10),
    (25, 30),
    (50, 52)
]

penalty_per_city = 1

# GA Settings

generations = 300
population_size = 300
mutation_rate = 0.01
elite_size = 20

