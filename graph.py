graph = {
    'A': {'B': 1, 'C': 4, 'D': 6},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 3},
    'D': {'A': 6, 'B': 5, 'C': 3}
}

start = 'A'

if __name__ == "__main__":
    from bfs_tsp import bfs_tsp
    from ucs_tsp import ucs_tsp
    from a_star_tsp import a_star_tsp

    path, cost = bfs_tsp(graph, start)
    print(f"BFS Path: {path}, Cost: {cost}")

    path, cost = ucs_tsp(graph, start)
    print(f"UCS Path: {path}, Cost: {cost}")

    path, cost = a_star_tsp(graph, start)
    print(f"A* Path: {path}, Cost: {cost}")
