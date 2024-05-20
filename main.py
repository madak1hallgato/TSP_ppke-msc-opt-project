
from config import city_labels
from calculations import has_feasible_solution
from brute_force import brute_force_tsp_1, brute_force_tsp_2, brute_force_tsp_3
from genetic_algorithm import genetic_algorithm_tsp_1, genetic_algorithm_tsp_2, genetic_algorithm_tsp_3

# Check if there is a feasible solution
print("\nIs there a feasible solution to the problem?")
if has_feasible_solution(): print("Yes, there is a feasible solution to the problem.")
else: print("No feasible solution exists.")

# Get the results from the approaches
brute_force_path_1, brute_force_penalty_1, brute_force_cost_1 = brute_force_tsp_1()
brute_force_path_2, brute_force_penalty_2, brute_force_cost_2 = brute_force_tsp_2()
brute_force_path_3, brute_force_penalty_3, brute_force_cost_3 = brute_force_tsp_3()
genetic_algorithm_path_1, genetic_algorithm_penalty_1, genetic_algorithm_cost_1 = genetic_algorithm_tsp_1()
genetic_algorithm_path_2, genetic_algorithm_penalty_2, genetic_algorithm_cost_2 = genetic_algorithm_tsp_2()
genetic_algorithm_path_3, genetic_algorithm_penalty_3, genetic_algorithm_cost_3 = genetic_algorithm_tsp_3()

# Convert path indices back to city labels for display
brute_force_path_1 = [city_labels[i] for i in brute_force_path_1]
brute_force_path_2 = [city_labels[i] for i in brute_force_path_2]
brute_force_path_3 = [city_labels[i] for i in brute_force_path_3]
genetic_algorithm_path_labels_1 = [city_labels[city] for city in genetic_algorithm_path_1]
genetic_algorithm_path_labels_2 = [city_labels[city] for city in genetic_algorithm_path_2]
genetic_algorithm_path_labels_3 = [city_labels[city] for city in genetic_algorithm_path_3]

# Print results
print(f"\nBrute Force Approach (without Time Window):\nPath: {' -> '.join(brute_force_path_1)}\nPenalty: {brute_force_penalty_1}\nCost: {brute_force_cost_1}")
print(f"\nBrute Force Approach (minimize the Penalty):\nPath: {' -> '.join(brute_force_path_2)}\nPenalty: {brute_force_penalty_2}\nCost: {brute_force_cost_2}")
print(f"\nBrute Force Approach (minimize the Cost):\nPath: {' -> '.join(brute_force_path_3)}\nPenalty: {brute_force_penalty_3}\nCost: {brute_force_cost_3}({brute_force_cost_3-brute_force_penalty_3}+{brute_force_penalty_3})")
print(f"\nGenetic Algorithm Approach (without Time Window):\nPath: {' -> '.join(genetic_algorithm_path_labels_1)}\nPenalty: {genetic_algorithm_penalty_1}\nCost: {genetic_algorithm_cost_1}")
print(f"\nGenetic Algorithm Approach (minimize the Penalty):\nPath: {' -> '.join(genetic_algorithm_path_labels_2)}\nPenalty: {genetic_algorithm_penalty_2}\nCost: {genetic_algorithm_cost_2}")
print(f"\nGenetic Algorithm Approach (minimize the Cost):\nPath: {' -> '.join(genetic_algorithm_path_labels_3)}\nPenalty: {genetic_algorithm_penalty_3}\nCost: {genetic_algorithm_cost_3}({genetic_algorithm_cost_3-genetic_algorithm_penalty_3}+{genetic_algorithm_penalty_3})\n")
