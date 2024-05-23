
from calculations import has_feasible_solution
from brute_force import BruteForce
from genetic_algorithm import GeneticAlgorithm

bf = BruteForce()
ga = GeneticAlgorithm()

print("\n(1) - Is there any feasible solution to the problem?\n")
if has_feasible_solution(): print("Yes, there is a feasible solution to the problem.")
else: print("No feasible solution exists.")

print("\n(+) - Minimize Time (without Time Window)")
bf_t = bf.minimize_time()
print(f"\nBrute Force:\nPath: {' -> '.join(bf_t['path'])}\nTime: {bf_t['time']}\n(Penalty: {bf_t['penalty']})\n(Cost: {bf_t['cost']})")
ga_t = ga.minimize_time()
print(f"\nGenetic Algorithm:\nPath: {' -> '.join(ga_t['path'])}\nTime: {ga_t['time']}\n(Penalty: {ga_t['penalty']})\n(Cost: {ga_t['cost']})")

print("\n(2) - Minimize Penalty")
bf_p = bf.minimize_penalty()
print(f"\nBrute Force:\nPath: {' -> '.join(bf_p['path'])}\n(Time: {bf_p['time']})\nPenalty: {bf_p['penalty']}\n(Cost: {bf_p['cost']})")
ga_p = ga.minimize_penalty()
print(f"\nGenetic Algorithm:\nPath: {' -> '.join(ga_p['path'])}\n(Time: {ga_p['time']})\nPenalty: {ga_p['penalty']}\n(Cost: {ga_p['cost']})")

print("\n(3) - Minimize Cost (Time+Penalty)")
bf_c = bf.minimize_cost()
print(f"\nBrute Force:\nPath: {' -> '.join(bf_c['path'])}\n(Time: {bf_c['time']})\n(Penalty: {bf_c['penalty']})\nCost: {bf_c['cost']}")
ga_c = ga.minimize_cost()
print(f"\nGenetic Algorithm:\nPath: {' -> '.join(ga_c['path'])}\n(Time: {ga_c['time']})\n(Penalty: {ga_c['penalty']})\nCost: {ga_c['cost']}\n")
