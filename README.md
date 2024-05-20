# Traveling Salesman Problem with Time Windows

This project aims to solve the Traveling Salesman Problem (TSP) with time windows using both brute force and genetic algorithm approaches.

## Problem Description

The TSP with time windows involves finding the shortest route that visits a set of cities while respecting the specified time windows for each city. The problem is defined by:

- **Cities:** A, B, C, D, E, F, G, H
- **Start City:** A
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

## Running the Code

To run the code, execute the `main.py` file. It will output the results obtained from both brute force and genetic algorithm approaches for the specified problem.

```bash
python main.py
```

## Results

The results include the optimal paths obtained from each approach along with their respective penalties and costs. The paths are displayed in the order of cities visited.
