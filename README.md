# Traveling Salesman Problem with Time Windows

The Traveling Salesman Problem with Time Windows (TSP-TW) is an extension of the classic Traveling Salesman Problem (TSP) where each city must be visited within a specific time frame. This additional constraint transforms the problem from simpy finding the shortest possible route to also ensuring that each city is visited within its specified time window. This dual objective makes TSP-TW significantly more challenging and relevant for real-world applications such as logistics, delivery routing, and scheduling.

In this project, we address the TSP-TW using two distinct approaches: brute force and genetic algorithms. The brute force approach involves evaluating all possible permutations of city visits to find the optimal route. While this guarantees the identification of the best solution, it is computationally expensive and impractical for large datasets. On the other hand, the genetic algorithm (GA) mimics the process of natural selection to iteratively evolve a population of candidate solutions, offering a more scalable alternative that approximates optimal solutions in a reasonable timeframe.

## Problem Overview

The Traveling Salesman Problem (TSP) is a well-known optimization challenge where the objective is to find the shortest possible route that visits a set of cities exactly once and returns to the starting city. The Traveling Salesman Problem with Time Windows (TSP-TW) adds an extra layer of complexity by introducing time windows for each city. This means that not only must the route be the shortest, but each city must also be visited within a specific time frame.

### The problem is defined by:

<p align="center">
   <img src="images/problem_to_solve.png" width="100%" />
</p>

In the figure, the left side shows the cities and the connections between them, with each city's time window displayed below its name. On the right side, there is a table that presents the distances between each pair of cities.

### To be solved:

1. **Is there any feasible solution to the problem?** <br/> Can the agent leave city A, visit each of the cities exactly once, and return to city A while arriving at each city within its specified time window? It is assumed that no time is spent in each city.

2. **Minimize the total penalty:** <br/> A penalty of 1 unit per city is applied if the agent arrives outside the specified time window. Find the tour that minimizes the total penalty, aiming to have as few cities as possible violate their time windows.

3. **Minimize the total cost:** <br/> The cost of the trip is the length of the trip plus the amount of penalties. For example, if the trip takes 48 units of time and there are two time-window violations, the total cost is 48 + 2 = 50. The objective is to minimize this total cost.
  
### Example:

The following figure illustrates a path (far from optimal) to demonstrate the calculation of costs. <br/> 
(The time window for City D was modified!)

<p align="center">
   <img src="images/example_path.png" width="100%" />
</p>

In the path, you can observe the time window constraints below each city, along with the time taken to travel between them. The red nodes indicate cities where the time constraints are violated.

- **Total penalty:** 6
- **Total time:** 44
- **Total cost:** 50 (44+6)

## Solution Approaches

We approach the TSP-TW problem through two distinct methods, brute force and genetic algorithms. Thanks to that brute force guarantees the identification of the best solution, so we can check the accuracy of the Genetic Algorithm.

- **Brute Force:** <br/> The brute force method exhaustively evaluates all possible permutations of the cities to identify the optimal route. While this guarantees the best solution, its computational demands make it impractical for larger datasets.

- **Genetic Algorithm:** <br/> The genetic algorithm approach employs evolutionary principles to find an optimal solution. It evolves a population of candidate solutions over multiple generations.

### Genetic Algorithm Workflow (TODO)

1. **Population Creation:** Randomly shuffles city orders to create a population of candidate solutions.
2. **Fitness Calculation:** Evaluates fitness based on minimizing total cost and penalty.
3. **Parent Selection:** Choosing individuals that are more fit to encourage better solutions.
4. **Crossover Operation:** Utilizes Partially Matched Crossover (PMX) to generate offspring.
5. **Mutation Operation:** Introduces randomness by swapping two random cities within a path.
6. **Survivor Selection:** Preserves the best solutions from the previous generation using elitism.
7. **Stopping Criterion:** Terminates after a fixed number of generations.

## Feasible path for the Problem

In the Traveling Salesman Problem with time windows (TSP-TW), the objective is to find an optimal route for visiting a set of cities, following to predefined time windows for each city. A feasible path in the TSP-TW context refers to a route that satisfies all time constraints while visiting each city exactly once, starting and ending at a designated origin city.

<p align="center">
   <img src="images/feasible_solution.png" width="100%" />
</p>

No feasible paths exist in the given problem without modifying time window constraints. <br/> The faint line at the top shows an example of the solution with modified time window constraints.

## Running the Code

The `config.py` file contain the parameter for the genetic algorithm, so we could try different variation of the algorithm. It is also contain the problem's parameters so it is possible to run the method on an other excercise.

To run the code, execute the `main.py` file. It will output the results obtained from both brute force and genetic algorithm approaches for the specified problem.

```bash
python main.py
```

## Results

The results display optimal paths from each approach along with their penalties and costs, displaying the order of visited cities.

```text
(1) - Is there any feasible solution to the problem?

No feasible solution exists.

(+) - Minimize Time (without Time Window)

Brute Force:
Path: A -> B -> E -> G -> D -> H -> C -> F -> A
Time: 15
(Penalty: 7)
(Cost: 22)

Genetic Algorithm:
Path: A -> F -> C -> H -> D -> G -> E -> B -> A
Time: 15
(Penalty: 7)
(Cost: 22)

(2) - Minimize Penalty

Brute Force:
Path: A -> E -> F -> H -> B -> D -> C -> G -> A
(Time: 30)
Penalty: 2
(Cost: 32)

Genetic Algorithm:
Path: A -> E -> F -> H -> B -> D -> C -> G -> A
(Time: 30)
Penalty: 2
(Cost: 32)

(3) - Minimize Cost (Time+Penalty)

Brute Force:
Path: A -> E -> B -> H -> D -> G -> C -> F -> A
(Time: 16)
(Penalty: 5)
Cost: 21

Genetic Algorithm:
Path: A -> E -> B -> H -> D -> G -> C -> F -> A
(Time: 16)
(Penalty: 5)
Cost: 21
```

For this result, the following parameters was applied:
 - Population size: 300
 - Elite size: 20
 - Mutation rate: 0.01
 - Generation: 300

### Compare different variations (TODO)
