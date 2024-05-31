# Homework Assignment - Traveling Salesman Problem

This repository contains the code for solving the Traveling Salesman Problem (TSP) using three different search strategies: Breadth-First Search (BFS), Uniform Cost Search (UCS), and A* Search.

## Problem Statement
TSP involves finding the shortest route that visits a list of cities exactly once and returns to the origin city, minimizing the total travel cost.

## Installation and Usage
1. Clone this repository.
2. Navigate to the repository directory.
3. Run the following command to execute each algorithm:
   - Breadth-First Search (BFS): `python bfs_tsp.py`
   - Uniform Cost Search (UCS): `python ucs_tsp.py`
   - A* Search: `python a_star_tsp.py`
   - All Algorithms: `python graph.py`
     
## Input Data Format
The input data is represented as a graph in the `graph.py` file. Modify this file to change the input graph.

## Output Data Format
The output will be displayed in the console, showing the shortest path found by each algorithm and its total cost.

## Evaluation
- BFS: Simple but may not be efficient for large datasets.
- UCS: Considers cost, improving efficiency, but lacks heuristic guidance.
- A*: Most efficient due to heuristic function, reducing search space.

## Conclusion
Successfully implemented three search algorithms for solving TSP. Each algorithm has its strengths and limitations, providing insights into their practical applications.
