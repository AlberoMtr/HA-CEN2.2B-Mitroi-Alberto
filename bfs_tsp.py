from collections import deque

def bfs_tsp(graph, start):
    queue = deque([(start, [start], 0)])
    min_cost = float('inf')
    best_path = []

    while queue:
        vertex, path, cost = queue.popleft()
        if len(path) == len(graph):
            total_cost = cost + graph[path[-1]][start]
            if total_cost < min_cost:
                min_cost = total_cost
                best_path = path
        else:
            for next_vertex in set(graph) - set(path):
                queue.append((next_vertex, path + [next_vertex], cost + graph[vertex][next_vertex]))

    return best_path + [start], min_cost

if __name__ == "__main__":
    from graph import graph, start
    path, cost = bfs_tsp(graph, start)
    print(f"BFS Path: {path}, Cost: {cost}")
