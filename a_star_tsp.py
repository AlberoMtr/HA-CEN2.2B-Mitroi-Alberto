import heapq

def heuristic(graph, current, unvisited):
    if not unvisited:
        return 0
    return min(graph[current][v] for v in unvisited)

def a_star_tsp(graph, start):
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
            unvisited = set(graph) - set(path)
            for next_vertex in unvisited:
                g = cost + graph[vertex][next_vertex]
                h = heuristic(graph, next_vertex, unvisited - {next_vertex})
                heapq.heappush(queue, (g, next_vertex, path + [next_vertex]))

    return best_path + [start], min_cost

if __name__ == "__main__":
    from graph import graph, start
    path, cost = a_star_tsp(graph, start)
    print(f"A* Path: {path}, Cost: {cost}")
