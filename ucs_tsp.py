import heapq

def ucs_tsp(graph, start):
    queue = [(0, start, [start])]
    min_cost = float('inf')
    best_path = []

    while queue:
        (cost, vertex, path) = heapq.heappop(queue)
        if len(path) == len(graph):
            path_cost = cost + graph[path[-1]][start]
            if path_cost < min_cost:
                min_cost = path_cost
                best_path = path
        else:
            for next_vertex in set(graph) - set(path):
                heapq.heappush(queue, (cost + graph[vertex][next_vertex], next_vertex, path + [next_vertex]))

    return best_path + [start], min_cost

if __name__ == "__main__":
    from graph import graph, start
    path, cost = ucs_tsp(graph, start)
    print(f"UCS Path: {path}, Cost: {cost}")
