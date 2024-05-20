import random
from config import cities, start_city, pop_size, elite_size, mutation_rate, generations
from calculations import calculate_cost, calculate_penalty

def create_individual():
    individual = cities[:]
    random.shuffle(individual)
    return individual

def create_population():
    return [create_individual() for _ in range(pop_size)]

def fitness_1_2(individual):
    path = [start_city] + individual + [start_city]
    penalty = calculate_penalty(path)
    cost = calculate_cost(path)
    return penalty, cost

def fitness_3(individual):
    path = [start_city] + individual + [start_city]
    penalty = calculate_penalty(path)
    cost = calculate_cost(path) + penalty
    return penalty, cost

def selection_1_3(population, fitnesses, num_parents):
    selected = random.choices(population, weights=[1 / f for f in fitnesses], k=num_parents)
    return selected

def selection_2(population, fitnesses, num_parents):
    selected = random.choices(population, weights=[1 / (f[0] * 1000 + f[1]) for f in fitnesses], k=num_parents)
    return selected

def crossover(parent1, parent2):
    gene_a = int(random.random() * len(parent1))
    gene_b = int(random.random() * len(parent1))
    start_gene = min(gene_a, gene_b)
    end_gene = max(gene_a, gene_b)
    child_p1 = parent1[start_gene:end_gene]
    child_p2 = [item for item in parent2 if item not in child_p1]
    child = child_p1 + child_p2
    return child

def mutate(individual):
    for swapped in range(len(individual)):
        if random.random() < mutation_rate:
            swap_with = int(random.random() * len(individual))
            city1 = individual[swapped]
            city2 = individual[swap_with]
            individual[swapped] = city2
            individual[swap_with] = city1
    return individual

def genetic_algorithm_tsp_1():
    pop = create_population()
    for _ in range(generations):
        fitnesses = [fitness_1_2(ind)[1] for ind in pop]
        new_population = []
        elite_indices = sorted(range(len(pop)), key=lambda x: fitnesses[x])[:elite_size]
        elite_individuals = [pop[i] for i in elite_indices]
        new_population.extend(elite_individuals)
        parents = selection_1_3(pop, fitnesses, len(pop) - elite_size)
        for i in range(0, len(parents) - 1, 2):
            parent1 = parents[i]
            parent2 = parents[i + 1]
            child1 = crossover(parent1, parent2)
            child2 = crossover(parent2, parent1)
            new_population.append(mutate(child1))
            new_population.append(mutate(child2))
        pop = new_population
    best_individual = pop[sorted(range(len(pop)), key=lambda x: fitnesses[x])[0]]
    best_path = [start_city] + best_individual + [start_city]
    best_penalty, best_cost = fitness_1_2(best_individual)
    return best_path, best_penalty, best_cost

def genetic_algorithm_tsp_2():
    pop = create_population()
    for _ in range(generations):
        fitnesses = [fitness_1_2(ind) for ind in pop]
        new_population = []
        elite_indices = sorted(range(len(pop)), key=lambda x: fitnesses[x])[:elite_size]
        elite_individuals = [pop[i] for i in elite_indices]
        new_population.extend(elite_individuals)
        parents = selection_2(pop, fitnesses, len(pop) - elite_size)
        for i in range(0, len(parents) - 1, 2):
            parent1 = parents[i]
            parent2 = parents[i + 1]
            child1 = crossover(parent1, parent2)
            child2 = crossover(parent2, parent1)
            new_population.append(mutate(child1))
            new_population.append(mutate(child2))
        pop = new_population
    best_individual = pop[sorted(range(len(pop)), key=lambda x: fitnesses[x])[0]]
    best_path = [start_city] + best_individual + [start_city]
    best_penalty, best_cost = fitness_1_2(best_individual)
    return best_path, best_penalty, best_cost

def genetic_algorithm_tsp_3():
    pop = create_population()
    for _ in range(generations):
        fitnesses = [fitness_3(ind)[1] for ind in pop]
        new_population = []
        elite_indices = sorted(range(len(pop)), key=lambda x: fitnesses[x])[:elite_size]
        elite_individuals = [pop[i] for i in elite_indices]
        new_population.extend(elite_individuals)
        parents = selection_1_3(pop, fitnesses, len(pop) - elite_size)
        for i in range(0, len(parents) - 1, 2):
            parent1 = parents[i]
            parent2 = parents[i + 1]
            child1 = crossover(parent1, parent2)
            child2 = crossover(parent2, parent1)
            new_population.append(mutate(child1))
            new_population.append(mutate(child2))
        pop = new_population
    best_individual = pop[sorted(range(len(pop)), key=lambda x: fitnesses[x])[0]]
    best_path = [start_city] + best_individual + [start_city]
    best_penalty, best_cost = fitness_3(best_individual)
    return best_path, best_penalty, best_cost
