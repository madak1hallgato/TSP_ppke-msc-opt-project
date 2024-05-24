

from brute_force import BruteForce
from genetic_algorithm import GeneticAlgorithm
from config import population_size, generations, mutation_rate, elite_size

bf = BruteForce()
ga = GeneticAlgorithm()

t_ok = 0
p_ok = 0
c_ok = 0

it_num = 30

for i in range(it_num):
    bf_t = bf.minimize_time()['time']
    ga_t = ga.minimize_time()['time']
    if bf_t == ga_t: t_ok += 1
    bf_p = bf.minimize_penalty()['penalty']
    ga_p = ga.minimize_penalty()['penalty']
    if bf_p == ga_p: p_ok += 1
    bf_c = bf.minimize_cost()['cost']
    ga_c = ga.minimize_cost()['cost']
    if bf_c == ga_c: c_ok += 1

print(f"\nGeneration={generations}, Population={population_size}, Mutation={mutation_rate}, Elit={elite_size}")
print(f"BF == GA (Minimize Time): {t_ok}/{it_num}")
print(f"BF == GA (Minimize Penalty): {p_ok}/{it_num}")
print(f"BF == GA (Minimize Cost): {c_ok}/{it_num}\n")