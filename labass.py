import heapq

cost_graph = {
    'S': [('A', 2), ('B', 1)],
    'A': [('C', 2), ('D', 4)],
    'B': [('E', 3)],
    'C': [('G', 3)],
    'D': [('G', 1)],
    'E': [('G', 5)],
    'G': []

}
def ucs(graph, start, goal):
    pq = [(0, start, [])]
    visited = set()

    while pq:
        (cost, node, path) = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)
        path = path + [node]

        if node == goal:
            return (cost, path)

        for neighbor, edge_cost in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(pq, (cost + edge_cost, neighbor, path))

print("UCS Result:", ucs(cost_graph, 'S', 'G'))