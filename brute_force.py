
import itertools
from typing import Callable
from config import cities, start_city, city_labels
from calculations import calculate_time, calculate_penalty

class BruteForce:

    def __init__(self) -> None:
        self.reset_values()

    def reset_values(self) -> None:
        self.permutations = itertools.permutations(cities)
        self.min_time = float('inf')
        self.min_penalty = float('inf')
        self.min_cost = float('inf')
        self.best_path = None

    def update_values(self) -> None:
        self.min_time = self.time
        self.min_penalty = self.penalty
        self.min_cost = self.cost
        self.best_path = self.path

    def solve(self, new_best_solution: Callable) -> dict:
        for perm in self.permutations:
            self.path = [start_city] + list(perm) + [start_city]
            self.time = calculate_time(self.path)
            self.penalty = calculate_penalty(self.path)
            self.cost = self.time + self.penalty
            if new_best_solution(): self.update_values()
        self.best_path = [city_labels[i] for i in self.best_path]
        result = {'path':self.best_path,'time':self.min_time,'penalty':self.min_penalty,'cost':self.min_cost }
        self.reset_values()
        return result

    def new_min_time(self) -> bool: return self.time < self.min_time
    def minimize_time(self) -> dict: return self.solve(lambda:self.new_min_time())

    def new_min_penalty(self) -> bool: return self.penalty < self.min_penalty or (self.penalty == self.min_penalty and self.time < self.min_time)
    def minimize_penalty(self) -> dict: return self.solve(lambda:self.new_min_penalty())

    def new_min_cost(self) -> bool: return self.cost < self.min_cost
    def minimize_cost(self) -> dict: return self.solve(lambda:self.new_min_cost())
        