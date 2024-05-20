# Traveling Salesman Problem with Time Windows

This project focuses on solving the Traveling Salesman Problem (TSP) with time windows using both brute force and genetic algorithm approaches.

## Problem Overview

The TSP with time windows involves finding the shortest path that visits a set of cities while respecting the specified time windows for each city. The problem is defined by:

- **Cities:**
  
  | A | B | C | D | E | F | G | H |
  |---|---|---|---|---|---|---|---|

- **Distances (Costs) Matrix:**
  
  |   | A | B | C | D | E | F | G | H |
  |---|---|---|---|---|---|---|---|---|
  | A | X | 1 | 8 | 9 | 3 | 2 | 4 | 6 |
  | B | 1 | X | 7 | 4 | 1 | 3 | 9 | 2 |
  | C | 8 | 7 | X | 6 | 8 | 2 | 4 | 5 |
  | D | 9 | 4 | 6 | X | 9 | 3 | 1 | 1 |
  | E | 3 | 1 | 8 | 9 | X | 4 | 2 | 7 |
  | F | 2 | 3 | 2 | 3 | 4 | X | 6 | 3 |
  | G | 4 | 9 | 4 | 1 | 2 | 6 | X | 5 |
  | H | 6 | 2 | 5 | 1 | 7 | 3 | 5 | X |

- **Time Windows:**
  
  |     | A   | B  | C  | D  | E  | F  | G  | H  |
  |-----|-----|----|----|----|----|----|----|----|
  | Min | 0   | 3  | 32 | 15 | 3  | 6  | 25 | 50 |
  | Max | 100 | 12 | 40 | 24 | 6  | 10 | 30 | 52 |

## Solution Approaches

The following figure illustrates a path (far from optimal) to demonstrate the calculation of costs.

<p align="center">
   <img src="images/example_path.png" width="100%" />
</p>

In the path, you can observe the time window constraints beneath each city, along with the time taken to travel between them. The red nodes indicate cities where the time constraints are violated, incurring penalties.

### Brute Force

The brute force approach evaluates all possible permutations of the cities and selects the path with the minimum total cost. The following strategies are employed:

1. **Minimize Total Cost:** Selects the path with the lowest total cost.
2. **Minimize Penalty:** Selects the path with the fewest time window violations.
3. **Minimize Total Cost with Penalty:** Considers both total cost and penalty in the path selection.

### Genetic Algorithm

The genetic algorithm approach employs evolutionary principles to find an optimal solution. It evolves a population of candidate solutions over multiple generations. The following strategies are employed:

1. **Minimize Total Cost:** Applies genetic operations to minimize the total cost.
2. **Minimize Penalty:** Applies genetic operations to minimize the penalty.
3. **Minimize Total Cost with Penalty:** Considers both total cost and penalty in the evolution process.

### Genetic Algorithm Workflow

1. **Population Creation:** Randomly shuffles city orders to create a population of candidate solutions.
2. **Fitness Calculation:** Evaluates fitness based on minimizing total cost and penalty.
3. **Parent Selection:** Choosing individuals that are more fit to encourage better solutions.
4. **Crossover Operation:** Utilizes Partially Matched Crossover (PMX) to generate offspring.
5. **Mutation Operation:** Introduces randomness by swapping two random cities within a path.
6. **Survivor Selection:** Preserves the best solutions from the previous generation using elitism.
7. **Stopping Criterion:** Terminates after a fixed number of generations.

### Feasible Paths

In the Traveling Salesman Problem with time windows (TSP-TW), the objective is to find an optimal route for visiting a set of cities, following to predefined time windows for each city. A feasible path in the TSP-TW context refers to a route that satisfies all time constraints while visiting each city exactly once, starting and ending at a designated origin city.

<p align="center">
   <img src="images/feasible_solution.png" width="100%" />
</p>

No feasible paths exist in the given problem without modifying time window constraints. The faint line at the top shows an example of the solution with modified time window constraints.

## Running the Code

To run the code, execute the `main.py` file. It will output the results obtained from both brute force and genetic algorithm approaches for the specified problem.

```bash
python main.py
```

## Results (Output)

The results display optimal paths from each approach along with their penalties and costs, displaying the order of visited cities.

```text
Is there a feasible solution to the problem?
No feasible solution exists.

Brute Force Approach (without Time Window):
Path: A -> B -> E -> G -> D -> H -> C -> F -> A
Penalty: 7
Cost: 15

Brute Force Approach (minimize the Penalty):
Path: A -> E -> F -> H -> B -> D -> C -> G -> A
Penalty: 2
Cost: 30

Brute Force Approach (minimize the Cost):
Path: A -> E -> B -> H -> D -> G -> C -> F -> A
Penalty: 5
Cost: 21(16+5)

Genetic Algorithm Approach (without Time Window):
Path: A -> F -> C -> H -> D -> G -> E -> B -> A
Penalty: 7
Cost: 15

Genetic Algorithm Approach (minimize the Penalty):
Path: A -> E -> F -> H -> B -> D -> C -> G -> A
Penalty: 2
Cost: 30

Genetic Algorithm Approach (minimize the Cost):
Path: A -> E -> B -> H -> D -> G -> C -> F -> A
Penalty: 5
Cost: 21(16+5)
```
