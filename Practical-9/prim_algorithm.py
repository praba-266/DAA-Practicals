import heapq

def prim(graph, start):
    visited = set()
    min_heap = [(0, start, None)]  # (weight, vertex, parent)

    total_cost = 0
    mst = []

    while min_heap:
        weight, current, parent = heapq.heappop(min_heap)

        if current in visited:
            continue

        visited.add(current)
        total_cost += weight

        if parent is not None:
            mst.append((parent, current, weight))

        for neighbor, edge_weight in graph[current]:
            if neighbor not in visited:
                heapq.heappush(
                    min_heap,
                    (edge_weight, neighbor, current)
                )

    return mst, total_cost


# Graph represented using an adjacency list
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 1)],
    'C': [('A', 3), ('B', 1), ('D', 4)],
    'D': [('B', 1), ('C', 4)]
}

mst, cost = prim(graph, 'A')

print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

print("Total Cost:", cost)