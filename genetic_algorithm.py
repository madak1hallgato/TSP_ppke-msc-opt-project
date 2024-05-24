
import random
from config import cities, start_city, city_labels
from config import population_size, generations, mutation_rate, elite_size
from calculations import calculate_time, calculate_penalty

class GeneticAlgorithm:

    def __init__(self):
        self.pop_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.elite_size = elite_size

    def create_individual(self):
        individual = cities[:]
        random.shuffle(individual)
        return individual
    
    def create_population(self):
        population = [self.create_individual() for _ in range(self.pop_size)]
        return population
    
    def calculate_fitness(self, individual):
        path = [start_city] + individual + [start_city]
        time = calculate_time(path)
        penalty = calculate_penalty(path)
        cost = time + penalty
        return time, penalty, cost
    
    def selection(self, population, fitnesses, num_parents):
        selected = random.choices(population, weights=[1 / f for f in fitnesses], k=num_parents)
        return selected
    
    def crossover(self, parent1, parent2):
        gene_a = int(random.random() * len(parent1))
        gene_b = int(random.random() * len(parent1))
        start_gene = min(gene_a, gene_b)
        end_gene = max(gene_a, gene_b)
        child_p1 = parent1[start_gene:end_gene]
        child_p2 = [item for item in parent2 if item not in child_p1]
        child = child_p1 + child_p2
        return child

    def mutate(self, individual):
        for swapped in range(len(individual)):
            if random.random() < self.mutation_rate:
                swap_with = int(random.random() * len(individual))
                city1 = individual[swapped]
                city2 = individual[swap_with]
                individual[swapped] = city2
                individual[swap_with] = city1
        return individual
    
    def solve(self, fitness_idx):
        pop = self.create_population()
        for _ in range(self.generations):
            fitnesses = [self.calculate_fitness(ind)[fitness_idx] for ind in pop]
            new_pop = []
            elite_indices = sorted(range(len(pop)), key=lambda x: fitnesses[x])[:elite_size]
            elite_individuals = [pop[i] for i in elite_indices]
            new_pop.extend(elite_individuals)
            parents = self.selection(pop, fitnesses, len(pop) - self.elite_size)
            if len(parents) == 1: new_pop = parents
            for i in range(0, len(parents)-1, 2):
                parent1 = parents[i]
                parent2 = parents[i + 1]
                child1 = self.crossover(parent1, parent2)
                child2 = self.crossover(parent2, parent1)
                new_pop.append(self.mutate(child1))
                new_pop.append(self.mutate(child2))
            pop = new_pop
        best_individual = pop[sorted(range(len(pop)), key=lambda x: fitnesses[x])[0]]
        best_path = [start_city] + best_individual + [start_city]
        best_path = [city_labels[i] for i in best_path]
        min_time, min_penalty, min_cost = self.calculate_fitness(best_individual)
        result = {'path':best_path,'time':min_time,'penalty':min_penalty,'cost':min_cost }
        return result

    def minimize_time(self) -> dict: return self.solve(0)
    def minimize_penalty(self) -> dict: return self.solve(1)
    def minimize_cost(self) -> dict: return self.solve(2)
