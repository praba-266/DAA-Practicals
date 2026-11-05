# Kruskal's Algorithm

def find(parent, vertex):
    if parent[vertex] != vertex:
        parent[vertex] = find(parent, parent[vertex])
    return parent[vertex]


def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)

    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else:
        parent[root_y] = root_x
        rank[root_x] += 1


def kruskal(vertices, edges):
    edges.sort(key=lambda x: x[2])

    parent = {}
    rank = {}

    for vertex in vertices:
        parent[vertex] = vertex
        rank[vertex] = 0

    mst = []
    total_cost = 0

    for u, v, weight in edges:
        root_u = find(parent, u)
        root_v = find(parent, v)

        # Add edge if it does not create a cycle
        if root_u != root_v:
            mst.append((u, v, weight))
            total_cost += weight
            union(parent, rank, root_u, root_v)

    return mst, total_cost


# Vertices
vertices = ['A', 'B', 'C', 'D']

# Edges: (vertex1, vertex2, weight)
edges = [
    ('A', 'B', 2),
    ('A', 'C', 3),
    ('B', 'C', 1),
    ('B', 'D', 1),
    ('C', 'D', 4)
]


mst, cost = kruskal(vertices, edges)

print("Minimum Spanning Tree:")

for edge in mst:
    print(edge)

print("Total Cost:", cost)